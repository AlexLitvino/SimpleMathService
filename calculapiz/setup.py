from setuptools import setup

__version__ = '0.0.2'

setup(
    name="calculapiz",
    description="Service to perform math calculation on remote server via REST API",
    version=__version__,
    url="https://github.com/AlexLitvino/calculapiz",
    author="Oleksii Lytvynov",
    author_email="litvinov.aleks@gmail.com",
    license="Apache License 2.0",
    install_requires=[
        "Flask==3.0.2",
    ],
    python_requires=">=3.9",
    packages=["app"]
)
