from setuptools import setup, find_packages

setup(
    name="autocnv",
    version="0.1.0",
    packages=find_packages(),
    package_data={
        'autocnv': ['data/*.gz', 'data/*.tbi', 'data/*.csv'],  # 根据实际数据库文件类型调整
    },
    install_requires=[
        # 依赖包自行安装
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
