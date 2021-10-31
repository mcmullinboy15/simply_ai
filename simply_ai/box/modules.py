import torch.nn as nn
import torch.nn.functional as F


class BaseModule(nn.Module):
    def __init__(self, shape_in, shape_out, config) -> None:
        super().__init__()
        self.shape_in = shape_in
        self.shape_out = shape_out
        self.config = config


class BuildModule(BaseModule):
    def __init__(self, shape_in, shape_out, config, layer_types, activation_types) -> None:
        super().__init__(shape_in, shape_out, config)
        self.layer_types = layer_types
        self.activation_types = activation_types

        """
            I want to make the classes change in the check so i just need to do config.input_layer(in, out)
            Also move most/all of this to the Box
        """
        self.inputLayer = layer_types[config["input_layer"][0]](shape_in, config["input_layer"][1])
        for idx, hidden_layer in enumerate(config["hidden_layers"]):
            layer = layer_types[hidden_layer[0]](hidden_layer[1], hidden_layer[2])
            self.__setattr__(f"{hidden_layer[0]}{idx}", layer)
        self.outputLayer = layer_types[config["output_layer"][0]](config["output_layer"][1], shape_out)
        print(self)

    def forward(self, x):
        x = self.activation_types[self.config["input_layer"][2]](self.inputLayer(x))
        for idx, hidden_layer in enumerate(self.config['hidden_layers']):
            x = self.activation_types[hidden_layer[3]](self.__getattr__(f"{hidden_layer[0]}{idx}")(x))
        x = self.activation_types[self.config["output_layer"][2]](self.outputLayer(x))
        return x


class LinearModule(BaseModule):
    def __init__(self, shape_in, shape_out, config) -> None:
        super().__init__(shape_in, shape_out, config)

        self.h1 = self.config['h1']
        self.h2 = self.config['h2']
        self.h3 = self.config['h3']

        self.l1 = nn.Linear(shape_in, self.h1)
        self.relu1 = nn.Linear(self.h1, self.h2)

        if self.h3 is not None:
            self.relu2 = nn.Linear(self.h2, self.h3)
            self.relu3 = nn.Linear(self.h3, self.h2)

        self.relu4 = nn.Linear(self.h2, self.h1)
        self.l2 = nn.Linear(self.h1, shape_out)

        print(self)

    def forward(self, x):

        x = F.relu(self.l1(x))
        x = F.relu(self.relu1(x))

        if self.h3 is not None:
            x = F.relu(self.relu2(x))
            x = F.relu(self.relu3(x))

        x = F.relu(self.relu4(x))
        x = self.l2(x)

        return x
