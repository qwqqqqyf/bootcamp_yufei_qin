import argparse
import logging
from pathlib import Path

import pandas as pd

from src.features import add_modeling_features


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def build_features(input_path: Path, output_path: Path) -> Path:
    """Read raw prices, build leak-safe features, and write a deterministic CSV."""
    logger.info("Reading %s", input_path)
    data = pd.read_csv(input_path, parse_dates=["date"])
    result = add_modeling_features(data)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output_path, index=False)
    logger.info("Wrote %s rows to %s", len(result), output_path)
    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build project modeling features")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build_features(args.input, args.output)
