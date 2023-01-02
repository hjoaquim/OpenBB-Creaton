# IMPORTATION STANDARD
import os
from pathlib import Path

# IMPORTATION THIRDPARTY
import dotenv

# IMPORTATION INTERNAL

REPOSITORY_DIRECTORY = Path(__file__).parent.parent

dotenv.load_dotenv(REPOSITORY_DIRECTORY / ".env")

PORTFOLIO_FILE = os.getenv("PORTFOLIO_FILE")
DASHBOARD_TITLE = os.getenv("DASHBOARD_TITLE")
