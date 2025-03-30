# FairAutoCleaner 2025

import os
import pathlib
import sys
from timeit import default_timer as timer
from datetime import datetime
import pandas as pd
from loguru import logger
import ydata_profiling
from FairAutoCleaner.normalizer import DataNormalizer
from FairAutoCleaner.modules import *
import json


class AutoClean:

    def __init__(
        self,
        input_data,
        output_folder=None,
        # mode="auto",
        # duplicates=False,
        # missing_num=False,
        # missing_categ=False,
        # encode_categ=False,
        # extract_datetime=False,
        # outliers=False,
        # outlier_param=1.5,
        # logfile=True,
        # verbose=False,
        audit_logger=None,
        config={},
    ):
        """
        input_data (dataframe)..........Pandas dataframe
        output_folder (str)............Path to folder where output will be saved
        mode (str)......................define in which mode you want to run AutoClean
                                        'auto' = sets all parameters to 'auto' and let AutoClean do the data cleaning automatically
                                        'manual' = lets you choose which parameters/cleaning steps you want to perform

        duplicates (str)................define if duplicates in the data should be handled
                                        duplicates are rows where all features are identical
                                        'auto' = automated handling, deletes all copies of duplicates except one
                                        False = skips this step
        missing_num (str)...............define how NUMERICAL missing values are handled
                                        'auto' = automated handling
                                        'linreg' = uses Linear Regression for predicting missing values
                                        'knn' = uses K-NN algorithm for imputation
                                        'mean','median' or 'most_frequent' = uses mean/median/mode imputatiom
                                        'delete' = deletes observations with missing values
                                        False = skips this step
        missing_categ (str).............define how CATEGORICAL missing values are handled
                                        'auto' = automated handling
                                        'logreg' = uses Logistic Regression for predicting missing values
                                        'knn' = uses K-NN algorithm for imputation
                                        'most_frequent' = uses mode imputatiom
                                        'delete' = deletes observations with missing values
                                        False = skips this step
        encode_categ (list).............encode CATEGORICAL features, takes a list as input
                                        ['auto'] = automated encoding
                                        ['onehot'] = one-hot-encode all CATEGORICAL features
                                        ['label'] = label-encode all categ. features
                                        to encode only specific features add the column name or index: ['onehot', ['col1', 2]]
                                        False = skips this step
        extract_datetime (str)..........define whether DATETIME type features should be extracted into separate features
                                        to define granularity set to 'D'= day, 'M'= month, 'Y'= year, 'h'= hour, 'm'= minute or 's'= second
                                        False = skips this step
        outliers (str)..................define how outliers are handled
                                        'winz' = replaces outliers through winsorization
                                        'delete' = deletes observations containing outliers
                                        oberservations are considered outliers if they are outside the lower and upper bound [Q1-1.5*IQR, Q3+1.5*IQR], where IQR is the interquartile range
                                        to set a custom multiplier use the 'outlier_param' parameter
                                        False = skips this step
        outlier_param (int, float)......define the multiplier for the outlier bounds
        logfile (bool)..................define whether to create a logile during the AutoClean process
                                        logfile will be saved in working directory as "autoclean.log"
        verbose (bool)..................define whether AutoClean logs will be printed in console
        config (dict)...................define a custom configuration for AutoClean
        audit_logger (AuditLogger)......define a custom audit logger

        OUTPUT (dataframe)..............a cleaned Pandas dataframe, accessible through the 'output' instance
        """
        self.start_time = datetime.now()

        mode = config.get("dataset_config", {}).get("preprocessing", {}).get("mode", "auto")
        duplicates = config.get("dataset_config", {}).get("preprocessing", {}).get("duplicates", False)
        missing_num = config.get("dataset_config", {}).get("preprocessing", {}).get("missing_num", False)
        missing_categ = config.get("dataset_config", {}).get("preprocessing", {}).get("missing_categ", False)
        outliers = config.get("dataset_config", {}).get("preprocessing", {}).get("outliers", False)
        encode_categ = config.get("dataset_config", {}).get("preprocessing", {}).get("encode_categ", [])
        extract_datetime = config.get("dataset_config", {}).get("preprocessing", {}).get("extract_datetime", False)
        outlier_param = config.get("dataset_config", {}).get("preprocessing", {}).get("outlier_param", 1.5)
        logfile = config.get("dataset_config", {}).get("preprocessing", {}).get("logfile", True)
        verbose = config.get("dataset_config", {}).get("preprocessing", {}).get("verbose", False)
        self.audit_logger = audit_logger
        self.config = config
        # Setup output directory
        output_folder = self.config.get("dataset_config", {}).get("preprocessing", {}).get("output_folder")
        self.output_folder = output_folder

        # Initialize logger
        self._initialize_logger(verbose, logfile)

        if not pathlib.Path.exists(pathlib.Path(output_folder)):
            os.mkdir(output_folder)

        output_data = input_data.copy()

        if mode == "auto":
            (
                duplicates,
                missing_num,
                missing_categ,
                outliers,
                encode_categ,
                extract_datetime,
            ) = ("auto", "auto", "auto", False, ["auto"], False)

        # Store parameters
        self.mode = mode
        self.duplicates = duplicates
        self.missing_num = missing_num
        self.missing_categ = missing_categ
        self.outliers = outliers
        self.encode_categ = encode_categ
        self.extract_datetime = extract_datetime
        self.outlier_param = outlier_param
        self.logfile = logfile
        self.verbose = verbose

        # Validate parameters
        self._validate_params(output_data, verbose, logfile)

        # Process data
        self.output = self._clean_data(output_data, input_data)

        # Save output
        output_file = output_folder + "/cleaned_data.csv"
        self.output.to_csv(output_file, index=False)
        logger.info(f"Output dataframe saved to: {output_file}")

        # audit_file = output_folder / "autoclean_audit.json"
        self.end_time = datetime.now()
        if not verbose:
            print(
                "AutoClean process completed in",
                (self.end_time - self.start_time).total_seconds(),
                "seconds",
            )
        if logfile:
            print("Logfile saved to:", os.path.join(os.getcwd(), "autoclean.log"))
            # print('Audit trail saved to:', audit_file)

    def _initialize_logger(self, verbose, logfile):
        # function for initializing the logging process
        logger.remove()
        if verbose == True:
            logger.add(
                sys.stderr, format="{time:DD-MM-YYYY HH:mm:ss.SS} - {level} - {message}"
            )
        if logfile == True:
            log_path = os.path.join(self.output_folder, "logfile.log")
            logger.add(
                log_path,
                mode="w",
                format="{time:DD-MM-YYYY HH:mm:ss.SS} - {level} - {message}",
            )
        return

    def _validate_params(self, df, verbose, logfile):
        # function for validating the input parameters of the autolean process
        logger.info("Started validation of input parameters...")

        if type(df) != pd.core.frame.DataFrame:
            raise ValueError('Invalid value for "df" parameter.')
        if self.mode not in ["manual", "auto"]:
            raise ValueError('Invalid value for "mode" parameter. Possible values are "manual" and "auto".')
        if self.duplicates not in [False, "auto"]:
            raise ValueError('Invalid value for "duplicates" parameter. Possible values are "auto" and False.')
        if self.missing_num not in [
            False,
            "auto",
            "knn",
            "mean",
            "median",
            "most_frequent",
            "delete",
        ]:
            raise ValueError('Invalid value for "missing_num" parameter. Possible values are "auto", "knn", "mean", "median", "most_frequent" and "delete".')
        if self.missing_categ not in [False, "auto", "knn", "most_frequent", "delete"]:
            raise ValueError('Invalid value for "missing_categ" parameter. Possible values are "auto", "knn", "most_frequent" and "delete".')
        if self.outliers not in [False, "auto", "winz", "delete"]:
            raise ValueError('Invalid value for "outliers" parameter. Possible values are "auto", "winz" and "delete".')
        if isinstance(self.encode_categ, list):
            if len(self.encode_categ) > 2 and self.encode_categ[0] not in [
                "auto",
                "onehot",
                "label",
            ]:
                raise ValueError('Invalid value for "encode_categ" parameter. Possible values are "auto", "onehot" and "label".')
            if len(self.encode_categ) == 2:
                if not isinstance(self.encode_categ[1], list):
                    raise ValueError('Invalid value for "encode_categ" parameter. Possible values are "auto", "onehot" and "label".')
        else:
            if not self.encode_categ in ["auto", False]:
                raise ValueError('Invalid value for "encode_categ" parameter. Possible values are "auto", "onehot" and "label".')
        if not isinstance(self.outlier_param, int) and not isinstance(
            self.outlier_param, float
        ):
            raise ValueError('Invalid value for "outlier_param" parameter. Possible values are integers and floats.')
        if self.extract_datetime not in [False, "auto", "D", "M", "Y", "h", "m", "s"]:
            raise ValueError('Invalid value for "extract_datetime" parameter. Possible values are "auto", "D", "M", "Y", "h", "m" and "s".')
        if not isinstance(verbose, bool):
            raise ValueError('Invalid value for "verbose" parameter. Possible values are True and False.')
        if not isinstance(logfile, bool):
            raise ValueError('Invalid value for "logfile" parameter. Possible values are True and False.')

        logger.info("Completed validation of input parameters")
        return

    def _clean_data(self, df, input_data):
        # function for starting the autoclean process
        df = df.reset_index(drop=True)

        # Duplicate handling
        if self.duplicates:
            start_time = self.audit_logger.start_operation(
                "duplicate_handling",
                "Remove duplicate rows from the dataset",
                {"method": self.duplicates},
                df,
            )
            df_before = df.copy()
            df = Duplicates.handle(self, df)
            changes = self.audit_logger.log_dataframe_changes(
                "duplicate_handling", df_before, df
            )
            self.audit_logger.complete_operation(
                "duplicate_handling",
                "Remove duplicate rows from the dataset",
                {"method": self.duplicates},
                start_time,
                df_before,
                df,
                changes,
            )

        # Missing value handling
        if self.missing_num or self.missing_categ:
            start_time = self.audit_logger.start_operation(
                "missing_value_handling",
                "Handle missing values in the dataset",
                {
                    "numerical_method": self.missing_num,
                    "categorical_method": self.missing_categ,
                },
                df,
            )
            df_before = df.copy()
            df = MissingValues.handle(self, df)
            changes = self.audit_logger.log_dataframe_changes(
                "missing_value_handling", df_before, df
            )
            self.audit_logger.complete_operation(
                "missing_value_handling",
                "Handle missing values in the dataset",
                {
                    "numerical_method": self.missing_num,
                    "categorical_method": self.missing_categ,
                },
                start_time,
                df_before,
                df,
                changes,
            )

        # Outlier handling
        if self.outliers:
            start_time = self.audit_logger.start_operation(
                "outlier_handling",
                "Handle outliers in numerical features",
                {"method": self.outliers, "outlier_param": self.outlier_param},
                df,
            )
            df_before = df.copy()
            df = Outliers.handle(self, df)
            changes = self.audit_logger.log_dataframe_changes(
                "outlier_handling", df_before, df
            )
            self.audit_logger.complete_operation(
                "outlier_handling",
                "Handle outliers in numerical features",
                {"method": self.outliers, "outlier_param": self.outlier_param},
                start_time,
                df_before,
                df,
                changes,
            )
            
        # Field assignments
        start_time = self.audit_logger.start_operation(
            "field_assignments", "Assign field types", {}, df
        )
        df_before = df.copy()
        df = FieldAssignment.handle(self, df)
        changes = self.audit_logger.log_dataframe_changes(
            "field_assignments", df_before, df
        )
        self.audit_logger.complete_operation(
            "field_assignments",
            "Assign field types",
            {},
            start_time,
            df_before,
            df,
            changes,
        )

        # DateTime conversion
        if self.extract_datetime:
            start_time = self.audit_logger.start_operation(
                "datetime_conversion",
                "Convert and extract datetime features",
                {"granularity": self.extract_datetime},
                df,
            )
            df_before = df.copy()
            df = Adjust.convert_datetime(self, df)
            changes = self.audit_logger.log_dataframe_changes(
                "datetime_conversion", df_before, df
            )
            self.audit_logger.complete_operation(
                "datetime_conversion",
                "Convert and extract datetime features",
                {"granularity": self.extract_datetime},
                start_time,
                df_before,
                df,
                changes,
            )

        # Categorical encoding
        if self.encode_categ:
            start_time = self.audit_logger.start_operation(
                "categorical_encoding",
                "Encode categorical features",
                {"method": self.encode_categ},
                df,
            )
            df_before = df.copy()
            df = EncodeCateg.handle(self, df)
            changes = self.audit_logger.log_dataframe_changes(
                "categorical_encoding", df_before, df
            )
            self.audit_logger.complete_operation(
                "categorical_encoding",
                "Encode categorical features",
                {"method": self.encode_categ},
                start_time,
                df_before,
                df,
                changes,
            )
            
       

        # Value rounding
        start_time = self.audit_logger.start_operation(
            "value_rounding", "Round numerical values to appropriate precision", {}, df
        )
        df_before = df.copy()
        df = Adjust.round_values(self, df, input_data)
        changes = self.audit_logger.log_dataframe_changes(
            "value_rounding", df_before, df
        )
        self.audit_logger.complete_operation(
            "value_rounding",
            "Round numerical values to appropriate precision",
            {},
            start_time,
            df_before,
            df,
            changes,
        )
        
        df.to_csv(self.output_folder + "/before_normalization.csv", index=False)

        # Normalization
        if (
            self.config.get("dataset_config", {})
            .get("preprocessing", {})
            .get("normalization", {})
            .get("enabled", False)
            == True
        ):
            start_time = self.audit_logger.start_operation(
                "normalization",
                "Normalize numerical features",
                self.config["dataset_config"]["preprocessing"][
                    "normalization"
                ],
                df,
            )
            df_before = df.copy()
            normalizer = DataNormalizer(
                method=self.config["dataset_config"]["preprocessing"][
                    "normalization"
                ].get("method", "standard"),
                exclude_features=self.config["dataset_config"][
                    "preprocessing"
                ]["normalization"].get("exclude_features", []),
            )
            df = normalizer.fit_transform(df)
            changes = self.audit_logger.log_dataframe_changes(
                "normalization", df_before, df
            )
            changes.update({"feature_stats": normalizer.feature_stats})
            self.audit_logger.complete_operation(
                "normalization",
                "Normalize numerical features",
                self.config["dataset_config"]["preprocessing"][
                    "normalization"
                ],
                start_time,
                df_before,
                df,
                changes,
            )

        # # Dimensionality reduction
        # if self.config.get('dataset_config', {}).get('dataset', {}).get('preprocessing', {}).get('dim_reduction', {}).get('enabled', False)==True:
        #     start_time = self.audit_logger.start_operation(
        #         "dimensionality_reduction",
        #         "Reduce data dimensionality",
        #         self.config['dataset_config']['preprocessing']['dim_reduction'],
        #         df
        #     )
        #     df_before = df.copy()
        #     reducer = DimensionalityReducer(
        #         method=self.config['dataset_config']['preprocessing']['dim_reduction'].get('method', 'pca'),
        #         n_components=self.config['dataset_config']['preprocessing']['dim_reduction'].get('n_components'),
        #         target_explained_variance=self.config['dataset_config']['preprocessing']['dim_reduction'].get('target_explained_variance', 0.95)
        #     )
        #     reduced_data, reduction_metadata = reducer.fit_transform(df)
        #     reduced_cols = [f'component_{i+1}' for i in range(reduced_data.shape[1])]
        #     df = pd.DataFrame(reduced_data, columns=reduced_cols, index=df.index)

        #     changes = self.audit_logger.log_dataframe_changes("dimensionality_reduction", df_before, df)
        #     changes.update(reduction_metadata)
        #     self.audit_logger.complete_operation(
        #         "dimensionality_reduction",
        #         "Reduce data dimensionality",
        #         self.config['dataset_config']['preprocessing']['dim_reduction'],
        #         start_time,
        #         df_before,
        #         df,
        #         changes
        #     )

        return df
