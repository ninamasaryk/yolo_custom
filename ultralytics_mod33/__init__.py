# Ultralytics YOLO 🚀, AGPL-3.0 license

__version__ = "8.3.59"

import os

# Set ENV variables (place before imports)
if not os.environ.get("OMP_NUM_THREADS"):
    os.environ["OMP_NUM_THREADS"] = "1"  # default for reduced CPU utilization during training

from ultralytics_mod33.models import NAS, RTDETR, SAM, YOLO, FastSAM, YOLOWorld
from ultralytics_mod33.utils import ASSETS, SETTINGS
from ultralytics_mod33.utils.checks import check_yolo as checks
from ultralytics_mod33.utils.downloads import download

settings = SETTINGS
__all__ = (
    "__version__",
    "ASSETS",
    "YOLO",
    "YOLOWorld",
    "NAS",
    "SAM",
    "FastSAM",
    "RTDETR",
    "checks",
    "download",
    "settings",
)
