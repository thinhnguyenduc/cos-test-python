from pathlib import Path

PROJECT_ROOT = str(Path(__file__).parent.parent.parent)
PROJECT_NAME = PROJECT_ROOT.split("/")[-1]
LOG_DIR = PROJECT_ROOT + "/logs/"
LOG_FILE = LOG_DIR + "%s.log"
