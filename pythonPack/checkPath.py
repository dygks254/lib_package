import os
import pathlib
import argparse


def validPathType(pathCheck: str) -> pathlib.Path:
    """Custom argparse type for real path"""
    try:
        if os.path.isdir(pathCheck) is False:
            raise ValueError
        return pathlib.Path(pathCheck)
    except ValueError:
        raise argparse.ArgumentTypeError(f"This directory ({pathCheck}) not valid! ")


def validFileType(fileCheck: str) -> pathlib.Path:
    """Custom argparse type for real file"""
    try:
        if os.path.isfile(fileCheck) is False:
            raise ValueError
        return pathlib.Path(fileCheck)
    except ValueError:
        raise argparse.ArgumentTypeError(f"This file ({fileCheck}) not valid! ")
