import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from box import ConfigBox


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns

    Args:
     path_to_yaml (str): Path to the YAML file to be read.

    Raises:
      ValueError: if yaml file is empty
      e: empty file

    Returns:
     configBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories

    Args:
      path_to_directories (list): List of paths to be created
      ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of a file in bytes, KB

    Args:
      path(Path): path of the file

    Returns:
      str: size of the file in bytes, KB
    """

    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
