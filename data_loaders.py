# data_loaders.py
from pathlib import Path

import logging
import pandas as pd
import json
import yaml


# Do not call logging.basicConfig() here.
# Use the logging configuration from Part 1.
logger = logging.getLogger(__name__)


def load_csv(filepath):
    """Load a CSV file into a DataFrame.
    filepath is a Path object.
    """
    # Read CSV
    df = pd.read_csv(filepath)
    # Log that file was read
    logger.info(f'Loaded CSV file: {filepath} ({len(df)} rows)')
    # Return dataframe
    return df

def load_json(filepath):
    """Load a JSON file into a Python object (dict or list).
    filepath is a Path object.
    """
    # Read JSON
    with open(filepath) as file:
        # Load file
        data = json.load(file)
    # Log that file was read
    logger.info(f'Loaded JSON file: {filepath}')
    # Return data
    return data



def load_yaml(filepath):
    """Load a YAML file into a Python object.
    filepath is a Path object.
    """
    # Read YAML
    with open(filepath) as file:
        # Load file
        data = yaml.safe_load(file)

    # Log that file was read
    logging.info(f'Loaded YAML file: {filepath}')
    # Return data
    return data


def load_data(filepath):
    """Load a file based on its extension.
    filepath is a string, such as 'fixtures/sample.csv'
    """
    # Create path
    path = Path(filepath)
    # Get extension
    ext = path.suffix.lower()

    # If CSV
    if ext == '.csv':
        # Load CSV
        return load_csv(path)
    # If JSON
    elif ext== '.json':
        # Load JSON
        return load_json(path)
    # If YAML
    elif ext == '.yaml':
        # Load YAML
        return load_yaml(path)
    # If None
    else:
        # Define error message
        msg = f'Unsupported file format: {ext}'
        # Log error
        logging.error(msg)
        # Raise error
        raise ValueError(msg)