import argparse
import simply_ai


def _args():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", help="Configuration file (ex: simply-ai-config.(yaml/json))")
    parser.add_argument("data_file", nargs='?', help="Data file, will override data_file attribute in `config_file` (ex: test-data.csv)")
    return parser.parse_args()


if __name__ == '__main__':
    args = _args()
    simply_ai.run_box_from_config_file(config_file=args.config_file, data_file=args.data_file)
