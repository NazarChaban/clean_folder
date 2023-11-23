# Clean Folder Package

The `clean_folder` package is designed to organize and clean up directories by sorting files into categorized subdirectories and normalizing file names. This package is especially useful for users who have directories cluttered with various file types and wish to automate the process of tidying up.

## Features

- Sorts files into predefined categories: images, video, documents, audio, archives, and unknown.
- Normalizes file names by transliterating Cyrillic characters to Latin and replacing non-alphanumeric characters with underscores.
- Unpacks archive files into separate folders and removes the original archive files after unpacking.
- Detects and handles unknown file extensions, moving them into a separate 'unknown' folder.
- Cleans up empty directories after sorting.

## Prerequisites

To use the `clean_folder` package, you'll need Python installed on your system. This package has been tested with Python 3.8, but it should work with other Python 3 versions as well.

## Installation

You can install this package and use command `pip install -e .` or install from pypi `pip install clean-folder-PCR`

## Usage

1) To start cleaning and organizing a directory, navigate to the directory where the `clean.py` file is located and run the script with the path to the directory you want to clean as a command-line argument:
2) Or you can activate script as a termanil command `clean-folder` from any place of your pc

```bash
python clean.py <path_to_directory>
python clean-forder <path_to_directory>