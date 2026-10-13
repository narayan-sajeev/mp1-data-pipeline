"""
Data Processing Pipeline - CLI Template

DS 3500 - MP1

Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""

import argparse
import logging
import sys
from pathlib import Path

from data_loaders import load_data
from data_processor import process_data, create_cleaning_report

# Initialize logger
logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    # Set logging level based on verbose flag
    level = logging.DEBUG if verbose else logging.INFO

    # Set up logger, print time, level & message
    # Print hours:minutes:seconds
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
                        datefmt='%H:%M:%S')


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Analyze files.')

    # Add input argument
    parser.add_argument('-i', '--input', required=True, help='Path to the input file')

    # Add config argument
    parser.add_argument('--config', required=True, help='Path to YAML configuration file')

    # Add output argument
    parser.add_argument('-o', '--output', required=True, help='Path to the output file')

    # Add verbose argument
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')

    return parser.parse_args()


def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    # Define path
    path = Path(filepath)

    # Check if file
    if path.is_file():
        logger.info(f'Input file validated: {filepath}')
        return True

    # If not file
    logger.error(f'Input file not found: {filepath}')
    return False


def main():
    """Main pipeline function."""
    # Parse arguments
    args = parse_arguments()
    # Set up logging with proper verbosity
    setup_logging(args.verbose)
    # Output parsed arguments using logger
    logger.debug(f'Arguments parsed: input={args.input}, config={args.config}, output={args.output}')
    # Retrieve filepath
    path = args.input
    # See if error comes when validating path
    if not validate_input(path):
        # If so, exit with error 1
        sys.exit(1)
    # Retrieve config
    config_path = args.config
    # See if error comes when validating config
    if not validate_input(config_path):
        # If so, exit with error 1
        sys.exit(1)

    # Try to load data and config
    try:
        df = load_data(path)
        config = load_data(config_path)
    # If error
    except ValueError:
        # Exit program
        sys.exit(1)

    # Copy original data
    df_copy = df.copy()

    # Try to process data
    try:
        processed = process_data(df, config)
    # If error
    except ValueError:
        # Exit program
        sys.exit(1)

    # Print report
    print(create_cleaning_report(df_copy, processed))
    logger.info(f'Processing complete: {len(df_copy)} → {len(processed)} rows')

    # Save final df without index
    processed.to_csv(args.output, index=False)
    # Log message
    logger.info(f'Saved cleaned data to {args.output}')


if __name__ == "__main__":
    main()
