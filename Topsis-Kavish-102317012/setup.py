from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="topsis-kavish-102317012",
    version="1.0.0",
    author="Kavish",
    author_email="kgupta9_be23@thapar.edu",
    description="A Python package for TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kavish1504/Topsis-Kavish-102317012",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.18.0',
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis_kavish_102317012.topsis:main',
        ],
    },
)
