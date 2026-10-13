"""
Data Processing Pipeline - CLI Template

DS 3500 - MP1

Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""

import argparse
import logging
from pathlib import Path

# Initialize logger
logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    # Set logging level based on verbose flag
    level = logging.DEBUG if verbose else logging.INFO

    # Set up logger, print time, level & message
    # Print hours:minutes:seconds
    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S')


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Analyze files.')

    # Add input argument
    parser.add_argument('-i', '--input', required=True, help='Path to the input file')

    # Add output argument
    parser.add_argument('-o', '--output', required=True, help='Path to the output file')

    # Add format argument
    parser.add_argument('--format', choices=['csv', 'json'], default='csv',
                        help='Output format: csv or json; default is csv')

    # Add verbose argument
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')

    return parser.parse_args()


def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    return Path(filepath).is_file()


def main():
    """Main pipeline function."""
    # Parse arguments
    args = parse_arguments()
    # Set up logging
    setup_logging()
    # Try to validate the input
    try:
        validate_input(args)
    # If error
    except:
        # Return error
        return 1


if __name__ == "__main__":
    main()
