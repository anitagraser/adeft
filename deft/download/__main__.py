import os
import argparse

from deft.locations import MODELS_PATH
from deft.download import download_models

"""
Allows models to be downloaded from the command line with
python -m deft.download

Use python -m deft.download --update
to update existing models if models have changed on S3
"""

parser = argparse.ArgumentParser(description='Download models from S3')
parser.add_argument('--update', action='store_true',
                    help='Update existing models if they have changed on S3')
args = parser.parse_args()

if not os.path.exists(MODELS_PATH):
    os.makedirs(MODELS_PATH)

download_models(update=args.update)
