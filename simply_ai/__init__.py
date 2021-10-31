from typing import Dict, List
import pandas as pd
import json
import yaml

from simply_ai.box import build_boxes


def build_config(config_file: str, data_file: str = None):
    # Get config
    config = None
    if config_file.endswith('.json'):
        config = json.loads(config_file)
    elif config_file.endswith('.yaml'):
        config = yaml.full_load(open(file=config_file))

    if config is None:
        raise ValueError("config_file must be (.yaml or .json)")

    # Get Data
    if data_file is not None:
        config["data_file"] = data_file

    if not config["data_file"].endswith('.csv'):
        raise ValueError("Datafile must be .csv")

    if config.get("data_file") is None:
        raise ValueError("data_file is not provided or in config")

    return config


def run_box_from_config_file(config_file: str, data_file: str = None):
    """
    :param config_file
    :param data_file
    """
    config = build_config(config_file=config_file, data_file=data_file)
    boxes = build_boxes(config=config)
    for box in boxes:
        box.train()
