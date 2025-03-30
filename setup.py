from setuptools import setup, find_packages

setup(
    name="asos_analysis",  # Name of your library
    version="1.0.0",  # Initial version of your library
    description="A Python tool for sorting and analyzing ASOS weather data",  # Brief description
    author="Saurav",  # Your name
    author_email="your_email@example.com",  # Your contact email
    url="https://github.com/your_github_username/asos_analysis",  # URL to your GitHub repo or website
    packages=find_packages(),  # Automatically find all packages in your library folder
    install_requires=[
        "pandas>=1.3.0",
        "openpyxl>=3.0.9",
    ],  # Dependencies your library needs
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Minimum Python version
)
