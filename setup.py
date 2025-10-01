"""
Setup script for OthelloBot package
"""

from setuptools import setup, find_packages

with open("README_FIXED.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="othellobot",
    version="1.0.0",
    author="Othello AI Developer",
    description="AI players for the game of Othello (Reversi)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment :: Board Games",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.0.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
            "mypy>=0.910"
        ]
    },
    entry_points={
        "console_scripts": [
            "othello-tournament=Othello.tournament:main",
        ],
    },
)