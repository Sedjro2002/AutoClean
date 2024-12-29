# AutoClean 2022
# For detailed documentation and usage guide, please visit the official GitHub Repo.
# https://github.com/elisemercury/AutoClean

import os
import pathlib
import sys
from timeit import default_timer as timer
import pandas as pd
from loguru import logger
import ydata_profiling
from AutoClean.modules import *

class AutoClean:

    def __init__(self, input_data, mode='auto', duplicates=False, missing_num=False, missing_categ=False, encode_categ=False, extract_datetime=False, outliers=False, outlier_param=1.5, logfile=True, verbose=False):  
        '''
        input_data (dataframe)..........Pandas dataframe
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

        OUTPUT (dataframe)..............a cleaned Pandas dataframe, accessible through the 'output' instance
        '''
        start = timer()
        self._initialize_logger(verbose, logfile)
        
        output_folder = pathlib.Path(__file__).parent / "output"
        if not pathlib.Path.exists(output_folder):
            os.mkdir(output_folder)
            
        
        #TODO: check the size of the dataframe to know what type of profiler to use
        # logger.info('Profiling before data preprocessing started')
        # profile_before = ydata_profiling.ProfileReport(input_data, title="Before data preprocessing")
        # profile_before.to_file(output_folder / "before_preprocessing_profile.html")
        # profile_before.to_file(output_folder / "before_preprocessing_profile.json")
        # logger.info('Profiling before data preprocessing completed')
        
        output_data = input_data.copy()

        if mode == 'auto':
            duplicates, missing_num, missing_categ, outliers, encode_categ, extract_datetime = 'auto', 'auto', 'auto', 'winz', ['auto'], 's'

        self.mode = mode
        self.duplicates = duplicates
        self.missing_num = missing_num
        self.missing_categ = missing_categ
        self.outliers = outliers
        self.encode_categ = encode_categ
        self.extract_datetime = extract_datetime
        self.outlier_param = outlier_param
        
        # validate the input parameters
        self._validate_params(output_data, verbose, logfile)
        
        # initialize our class and start the autoclean process
        self.output = self._clean_data(output_data, input_data)  

        end = timer()
        logger.info('AutoClean process completed in {} seconds', round(end-start, 6))
        
        # logger.info('Profiling after data preprocessing started')
        # profile_after = ydata_profiling.ProfileReport(self.output, title="After data preprocessing")
        # profile_after.to_file(output_folder / "after_preprocessing_profile.html")
        # profile_after.to_file(output_folder / "after_preprocessing_profile.json")
        # logger.info('Profiling after data preprocessing completed')
        
        # logger.info('Doing the comparative analysis between before and after data preprocessing')
        # comparative = ydata_profiling.compare(reports=[profile_before, profile_after])
        # comparative.to_file(output_folder / "comparative_profile.html")
        # comparative.to_file(output_folder / "comparative_profile.json")
        # logger.info('Comparative analysis completed')
        
        
        # save the cleaned dataframe to a csv file
        output_data.to_csv(os.path.join(output_folder, 'autoclean_output.csv'), index=False)
        logger.info('Output dataframe saved to: autoclean_output.csv')

        if not verbose:
            print('AutoClean process completed in', round(end-start, 6), 'seconds')
        if logfile:
            print('Logfile saved to:', os.path.join(os.getcwd(), 'autoclean.log'))

    def _initialize_logger(self, verbose, logfile):
        # function for initializing the logging process
        logger.remove()
        if verbose == True:
            logger.add(sys.stderr, format='{time:DD-MM-YYYY HH:mm:ss.SS} - {level} - {message}')
        if logfile == True:    
            logger.add('autoclean.log', mode='w', format='{time:DD-MM-YYYY HH:mm:ss.SS} - {level} - {message}')
        return

    def _validate_params(self, df, verbose, logfile):
        # function for validating the input parameters of the autolean process
        logger.info('Started validation of input parameters...')
        
        if type(df) != pd.core.frame.DataFrame:
            raise ValueError('Invalid value for "df" parameter.')
        if self.mode not in ['manual', 'auto']:
            raise ValueError('Invalid value for "mode" parameter.')
        if self.duplicates not in [False, 'auto']:
            raise ValueError('Invalid value for "duplicates" parameter.')
        if self.missing_num not in [False, 'auto', 'knn', 'mean', 'median', 'most_frequent', 'delete']:
            raise ValueError('Invalid value for "missing_num" parameter.')
        if self.missing_categ not in [False, 'auto', 'knn', 'most_frequent', 'delete']:
            raise ValueError('Invalid value for "missing_categ" parameter.')
        if self.outliers not in [False, 'auto', 'winz', 'delete']:
            raise ValueError('Invalid value for "outliers" parameter.')
        if isinstance(self.encode_categ, list):
            if len(self.encode_categ) > 2 and self.encode_categ[0] not in ['auto', 'onehot', 'label']:
                raise ValueError('Invalid value for "encode_categ" parameter.')
            if len(self.encode_categ) == 2:
                if not isinstance(self.encode_categ[1], list):
                    raise ValueError('Invalid value for "encode_categ" parameter.')
        else:
            if not self.encode_categ in ['auto', False]:
                raise ValueError('Invalid value for "encode_categ" parameter.')
        if not isinstance(self.outlier_param, int) and not isinstance(self.outlier_param, float):
            raise ValueError('Invalid value for "outlier_param" parameter.')  
        if self.extract_datetime not in [False, 'auto', 'D','M','Y','h','m','s']:
            raise ValueError('Invalid value for "extract_datetime" parameter.')  
        if not isinstance(verbose, bool):
            raise ValueError('Invalid value for "verbose" parameter.')  
        if not isinstance(logfile, bool):
            raise ValueError('Invalid value for "logfile" parameter.')  

        logger.info('Completed validation of input parameters')
        return
            
    def _clean_data(self, df, input_data):
        # function for starting the autoclean process
        df = df.reset_index(drop=True)
        # df = FieldAssignment.handle(self, df)
        
        #TODO: Add normalisation
        df = Duplicates.handle(self, df)
        df = MissingValues.handle(self, df)
        df = Outliers.handle(self, df)    
        df = Adjust.convert_datetime(self, df) 
        df = EncodeCateg.handle(self, df)     
        df = Adjust.round_values(self, df, input_data)
        return df 
