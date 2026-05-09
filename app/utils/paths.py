# Used to determine absolute path to avoid passing hard coded file paths

from pathlib import Path

# Project root (job-market-analyzer/)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data folders
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"


def get_raw_data_path(filename: str) -> Path:
    return RAW_DATA_DIR / filename