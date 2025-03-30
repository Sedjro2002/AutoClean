from ydata_profiling import ProfileReport
from pandas import DataFrame
import pandas as pd

def get_data(file_path: str) -> DataFrame:
    """
    This function takes a file path and returns a DataFrame.
    :param file_path: Path to the file
    :return: DataFrame
    """
    return pd.read_csv(file_path)

def profiling(df: DataFrame, title: str, description: str) -> ProfileReport:
    """
    This function takes a DataFrame and returns a ProfileReport object.
    :param df: DataFrame to be profiled
    :param title: Title of the report
    :param description: Description of the report
    :return: ProfileReport object
    """
    return ProfileReport(df, title=title, infer_dtypes=False)


def profiling_report(profile_report: ProfileReport) -> str:
    """
    This function takes a ProfileReport object and returns a string containing the HTML report.
    :param profile_report: ProfileReport object
    :return: HTML report as a string
    """
    return profile_report.to_html()


def profiling_report_to_file(profile_report: ProfileReport, file_path: str) -> None:
    """
    This function takes a ProfileReport object and saves the HTML report to a file.
    :param profile_report: ProfileReport object
    :param file_path: Path to the file where the HTML report will be saved
    :return: None
    """
    profile_report.to_file(file_path)
    

if __name__ == "__main__":
    # Example usage
    df = get_data("datasets/german_credit_data.csv")
    profile_report = profiling(df, "before", "Description")
    profiling_report_to_file(profile_report, "report.html")
    
    
    df = get_data("output/test_run/before_normalization.csv")
    profile_report = profiling(df, "after", "Description")
    profiling_report_to_file(profile_report, "clean_report.html")
    
    
    df = get_data("output/test_run/cleaned_data.csv")
    profile_report = profiling(df, "after", "Description")
    profiling_report_to_file(profile_report, "final_report.html")