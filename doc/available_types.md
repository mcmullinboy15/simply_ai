# Available Types

### BoxTypes
+ PytorchNNBuilderBox
    + model layer types [PytorchNNLayerTypes](#pytorch-nn-layer-types)
    + model:
    ```
      input_layer:   Tuple[ type, out ]
      hidden_layers: List[ Tuple[ type, in, out ] ]
      output_layer:  Tuple[ type, in ]
    ```
    
+ PytorchNNSimpleLinearBox
    + model:
    ```
    input_layer: <int:out>
    layers: 
        - <int:in> <int:out>
        - <int:in> <int:out>
        - ...
    output_layer: <int:in>
    ```

##### Upcoming BoxTypes
+ SkLearnLinearRegressionBox


### Pytorch NN Layer Types
+ [Linear](https://pytorch.org/docs/stable/generated/torch.nn.Linear.html#torch.nn.Linear)

### Pytorch NN Activation Functions
+ [relu](https://pytorch.org/docs/stable/generated/torch.nn.functional.relu.html#torch.nn.functional.relu)