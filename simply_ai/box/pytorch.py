from simply_ai.box.box import Box
from simply_ai.box.modules import BuildModule

from torch.nn import Linear
from torch.nn.functional import relu


# Pytorch
class PytorchBox(Box):
    pass


# Pytorch NN
class PytorchNNBox(PytorchBox):
    pass


class PytorchNNBuilderBox(PytorchNNBox):
    def train(self):
        model = BuildModule(len(self.input_cols), len(self.output_cols), config=self.model, layer_types=PYTORCH_AVAILABLE_LAYERS, activation_types=PYTORCH_AVAILABLE_ACTIVATION_FUNCTIONS)
        print("data:", len(self.data), len(self.data[0]))
        print("train_y:", len(self.train_y), len(self.train_y[0]), "train_x:", len(self.train_x), len(self.train_x[0]))
        print("val_y:", len(self.val_y), len(self.val_y[0]), "val_x:", len(self.val_x), len(self.val_x[0]))
        print("test_y:", len(self.test_y), len(self.test_y[0]), "test_x:", len(self.test_x), len(self.test_x[0]))


class PytorchNNSimpleLinearBox(PytorchNNBox):
    pass


# Pytorch TorchVision
class TorchVisionBox(PytorchBox):
    pass


PYTORCH_AVAILABLE_BOXES = {
    "PytorchNNBuilderBox": PytorchNNBuilderBox,
    "PytorchLinearBox": PytorchNNSimpleLinearBox
}
PYTORCH_AVAILABLE_LAYERS = {
    "Linear": Linear
}
PYTORCH_AVAILABLE_ACTIVATION_FUNCTIONS = {
    "relu": relu
}


def pytorch_check_model(config):
    from simply_ai.utils import checking
    rules = {
        "input_layer": ([PYTORCH_AVAILABLE_LAYERS, int, PYTORCH_AVAILABLE_ACTIVATION_FUNCTIONS],),
        "hidden_layers": [[PYTORCH_AVAILABLE_LAYERS, int, int, PYTORCH_AVAILABLE_ACTIVATION_FUNCTIONS]],
        "output_layer": ([PYTORCH_AVAILABLE_LAYERS, int, PYTORCH_AVAILABLE_ACTIVATION_FUNCTIONS],)
    }
    checking.check_config(config, rules)

