import os
import pathlib
import argparse


def valid_path_type(path_check: str) -> pathlib.Path:
  """Custom argparse type for real path"""
  try:
    if os.path.isdir(path_check) is False:
      raise ValueError
    return pathlib.Path(path_check)
  except ValueError:
      raise argparse.ArgumentTypeError(f"This path ({path_check}) not valid! ")