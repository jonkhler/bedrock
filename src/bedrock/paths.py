import os
from pathlib import Path


def bedrock_home() -> Path:
    return Path(os.environ.get("BEDROCK_HOME", Path.home() / ".bedrock"))
