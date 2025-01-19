from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="FairAutoCleaner",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Automated data cleaning and preprocessing package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/AutoClean",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "scikit-learn>=0.24.0",
        "loguru>=0.5.0",
        "openai>=0.27.0",
        "python-dotenv>=0.19.0",
        "pydantic>=1.8.0",
        "ydata-profiling>=4.0.0",
        "aif360>=0.4.0",
        "pydantic_ai"	
    ],
    include_package_data=True,
)
