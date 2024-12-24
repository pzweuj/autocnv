from setuptools import setup, find_packages

setup(
    name="autocnv",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # 您可能需要添加项目的依赖包
        'pandas~=1.2.5',
        'pyfaidx',
        'pysam~=0.16.0.1',
        'gtfparse~=1.2.1',
    ],
    entry_points={
        'console_scripts': [
            'autocnv=autocnv.__main__:main',
        ],
    },
    author="pzweuj",
    author_email="pzweuj@live.com",
    description="CNV注释工具",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pzweuj/autocnv",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
