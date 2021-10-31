from typing import List, Dict

from simply_ai.utils import checking

from simply_ai.box.box import Box
from simply_ai.box.pytorch import PYTORCH_AVAILABLE_BOXES, PYTORCH_AVAILABLE_LAYERS, pytorch_check_model
from simply_ai.box.sklearn import SKLEARN_AVAILABLE_BOXES, sklearn_check_model

AVAILABLE_BOXES: Dict[str, Box] = {**PYTORCH_AVAILABLE_BOXES, **SKLEARN_AVAILABLE_BOXES}

rules = {
    "data_file": str,
    "type": AVAILABLE_BOXES,
    "epochs": int,
    "batch_size": int,
    "input_cols": (int, str, [int, str]),
    "output_cols": (int, str, [int, str]),
    "lr": float,
    "model": dict
}
# not_required_rules = {
#     "shuffle": False,
#     "normalize": False,
#     "optim": str,
#     "criterion": str,
# }


def check_box_config(config):
    checking.check_config(config, rules)
    pytorch_check_model(config["model"])
    sklearn_check_model(config["model"])


def build_boxes(config) -> List[Box]:
    boxes = []

    box_config = config.get("box")
    boxes_config = config.get("boxes")
    if box_config is not None:
        box_config["data_file"] = config["data_file"]
        check_box_config(box_config)
        boxes.append(AVAILABLE_BOXES[box_config["type"]](box_config))

    elif boxes_config is not None:
        for box_config in boxes_config:
            box_config["data_file"] = config["data_file"]
            check_box_config(box_config)
            boxes.append(AVAILABLE_BOXES[box_config["type"]](box_config))

    return boxes
