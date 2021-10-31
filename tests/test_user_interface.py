import unittest
import yaml
import json
import simply_ai


def write_to_yaml(data, filename="tests/tmp-config.yaml"):
    with open(filename, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)


def write_to_json(data, filename="tests/tmp-config.json"):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)


class TestConfigVerification(unittest.TestCase):

    def test_build_config(self):
        yaml_file = "tests/tmp-config.yaml"
        json_file = "tests/tmp-config.json"

        config = {
            "data_file": "test-data.csv",
            "box": {
                "type": "PytorchNNBuilderBox",
                "epochs": 2000,
                "batch_size": 32,
                "input_cols": 0,
                "output_cols": [1, 2, 3],
                "model": {
                    "input_layer": {"type": "Linear", "out": 64},
                    "hidden_layers": [
                        # List[type, in, out]
                        ("Linear", 64, 128),
                        ("Linear", 128, 256),
                        ("Linear", 256, 256),
                        ("Linear", 256, 128),
                        ("Linear", 128, 64),
                        ("Linear", 64, 32)
                    ],
                    "output_layer": {"type": "Linear", "in": 32}
                }
            }
        }

        write_to_yaml(config)
        new_config = simply_ai.build_config(config_file=yaml_file, data_file="data.csv")
        print(config)
        print(new_config)
        assert new_config["data_file"] == "data.csv"

        simply_ai.build_config(config_file="tests/tmp-config.yaml", data_file="data.csv")
        simply_ai.build_config(config_file="tests/tmp-config.yaml", data_file="data.csv")

    def test_data_file(self):
        """
        data_file can be provided by command line which will override global data_file
        data_file can be Global and within each box
             but not sub data_file values in boxes
        """
        pass
