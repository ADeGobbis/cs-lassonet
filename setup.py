from setuptools import setup
from pathlib import Path


def read(fname):
    return (Path(__file__).parent / fname).open().read()


setup(
    name="cs_lassonet",
    version="0.0.1",
    author="Andrea De Gobbis",
    author_email="andrea.dg@neus-diagnostics.com",
    license="MIT",
    description="Implementation of CS - LassoNet",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/ADeGobbis/cs-lassonet",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
    ],
    packages=["cs_lassonet"],
    install_requires=["torch", "scikit-learn", "matplotlib", "sigpy"],
    tests_require=["pytest"],
    python_requires=">=3.6.5",
)
