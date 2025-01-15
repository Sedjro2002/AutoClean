from setuptools import setup, find_packages
import os

base_dir = os.path.dirname(__file__)

with open(os.path.join(base_dir, "README.md")) as f:
    long_description = f.read()

setup(
    name='FairAutoCleaner',         
    packages=find_packages(),   
    version='v1.0',      
    license='MIT',        
    description='FairAutoCleaner - Python Package for Automated Fair Data Preprocessing & Cleaning', 
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sedjro BONOU',                  
    author_email='habibhbn3@gmail.com', 
    keywords=['automated', 'cleaning', 'preprocessing', "autoclean", "ethics", "data", "fairness", "bias"],  
    install_requires=[          
        'scikit-learn',
        'numpy',
        'pandas',
        'loguru',
        'ydata_profiling',
        'openai',
        'python-dotenv',
        'pydantic',
        'tensorflow',
        'setuptools'
    ],
    entry_points={
        'console_scripts': [
            'fairautocleaner=AutoClean.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',   
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',    
        'Programming Language :: Python :: 3.12'
    ],
    python_requires='>=3.8',
)