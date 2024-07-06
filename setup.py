from setuptools import setup, find_packages

setup(
    name="coingecko_exporter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "httpx",
        "pandas",
        "sqlite3",
        "duckdb",
        "aiolimiter",
        "asyncio"
    ],
    author="Matt Maximo",
    author_email="matt@pioneerdigital.org",
    description="A package to fetch and export large amounts of CoinGecko cryptocurrency data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mattmaximo/coingecko_exporter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)