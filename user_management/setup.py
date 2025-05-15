"""Python setup file for custom library publication"""
from setuptools import setup, find_packages
setup(
    name="symptom_analysis",  #library name
    version="1.0.2",
    packages=find_packages(include=["symptom_analysis", "symptom_analysis.*"]),
    install_requires=[],
    author="YashashwiniS",
    author_email="Yashashwini222@gmail.com",
    description="A custom Python library for symptom analysis",
    long_description=open("README.md").read() if "README.md" else "",
    long_description_content_type="text/markdown",
    url="https://github.com/Yashashwini0310/cpp_project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
