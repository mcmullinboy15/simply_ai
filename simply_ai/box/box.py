from typing import Dict, Tuple
import pandas as pd
import numpy as np


class _SetupBox:
    global_data = {}

    def __init__(self, config: Dict):
        super(_SetupBox, self).__init__()

        self.config = config
        self.data_key = config["data_file"]
        self.epochs = config["epochs"]
        self.batch_size = config["batch_size"]
        self.input_cols = config["input_cols"]
        self.input_cols = [self.input_cols] if type(self.input_cols) != list else self.input_cols
        self.output_cols = config["output_cols"]
        self.output_cols = [self.output_cols] if type(self.output_cols) != list else self.output_cols
        self.model = config["model"]
        self.lr = config["lr"]
        self.optim = config["optim"]
        self.criterion = config["criterion"]


class _DataBox(_SetupBox):
    def __init__(self, config: Dict):
        super(_DataBox, self).__init__(config=config)
        self.shuffle = self.config.get("shuffle", False)
        self.normalize = self.config.get("normalize", False)

        _use_numpy_only = True

        if self.data_key not in self.global_data:
            _pandas_dataframe = pd.read_csv(self.data_key)

            if _use_numpy_only:
                if type(self.input_cols[0]) != int:
                    self.input_cols = [_pandas_dataframe.columns.index(c) for c in self.input_cols]
                self.global_data[self.data_key] = _pandas_dataframe.to_numpy()

        # Shuffle Data
        self.data = self.global_data.get(self.data_key)
        if self.shuffle:
            np.random.shuffle(self.data)

        # Normalize Data
        # if self.normalize:

        (self.train_y, self.train_x), \
            (self.val_y, self.val_x), \
            (self.test_y, self.test_x) = self._split_data()

    def _separate_y_x(self, data: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        return data[:, self.output_cols], data[:, self.input_cols]  # returns out, in

    def _split_data(self, train_size=0.80, val_size=0.1) -> Tuple[
        Tuple[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]:
        """
        TODO: should I make these variables configurable
        :arg train_size 80% or the data is for Training
        :arg val_size 10% or it is for Validation
        The rest is for Testing
        """
        train, validate, test = np.split(self.data,
                                         [int(train_size * len(self.data)),
                                          int((train_size + val_size) * len(self.data))])
        return self._separate_y_x(train), self._separate_y_x(validate), self._separate_y_x(test)


class Box(_DataBox):
    def train(self):
        raise NotImplementedError("Box.train")
