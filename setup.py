from setuptools import setup
import os

base_dir = os.path.dirname(__file__)

with open(os.path.join(base_dir, "README.md")) as f:
    long_description = f.read()

setup(
  name = 'FairAutoClean',         
  packages = ['AutoClean', 'ai_agent'],   
  version =  'v1.1.3',      
  license='MIT',        
  description = 'AutoClean - Python Package for Automated Preprocessing & Cleaning of Datasets', 
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Sedjro BONOU',                  
  author_email = 'habibhbn3@gmail.com', 
  # url = 'https://github.com/elisemercury/AutoClean', 
  # download_url = 'https://github.com/elisemercury/AutoClean/archive/refs/tags/v1.1.3.tar.gz',
  keywords = ['automated', 'cleaning', 'preprocessing', "autoclean", "ethics", "data"],  
  install_requires=[          
          'scikit-learn',
          'numpy',
          'pandas',
          'loguru',
          'ydata_profiling'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',   
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',    
    'Programming Language :: Python :: 3.12'
  ],
)