from setuptools import setup, find_packages

setup(
    name="topo2d",
    version="0.1.0",
    author="Your Name",
    author_email="youremail@example.com",
    description="A 2D topology drawing tool for proteins based on PDB files.",
    long_description="Topo2d parses PDB files (using HELIX and SHEET records) and draws a 2D topology diagram using matplotlib.",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "topo2d = topo2d.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
)
