#!/usr/bin/env python3.8
import shutil
from urllib.request import urlretrieve as retrieve, urlopen
from pathlib import Path
repo_root = Path(__file__).absolute().parent.parent.parent
target_location = Path(repo_root, "artifacts", "sqlite.y")
url="https://raw.githubusercontent.com/sqlite/sqlite/master/src/parse.y"
download_location, message = retrieve(url)
shutil.move(download_location, target_location)
