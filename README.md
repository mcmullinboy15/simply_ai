# simply_ai

### Interface
+ Using a .yaml or .json file, simply_ai can be run from the terminal
    ```yaml
    data_file: here or in box
    box:
      type: PytorchNNBuilderBox
      epochs: <int>
      batch_size: <int>
      input_cols: <List[int or str]>
      output_cols: <List[int or str] or None(all but input_cols)> 
      model:
        input_layer: [<Layer>, <int:out>]
        hidden_layers:
          # [ layer, in, out, activation_func ]
          - [ Linear, 64,  128, relu ]
          - [ Linear, 128, 256, relu ]
          - [ Linear, 256, 256, relu ]
          - [ Linear, 256, 128, relu ]
          - [ Linear, 128, 64,  relu ]
          - [ Linear, 64,  32,  relu ]
        output_layer: [<Layer>, <int:in>]

    or
  
    boxes:
      - 
    ```
    ```
    $ simply_ai config_files/<file-name>.yaml
    ```
  
+ Or manipulate and run simply_ai Boxes directly from python
    + This allows you to create your own pytorch Modules
    
    ##### Train options:
      from simply_ai.box import PytorchBuilderBox
      import simply_ai
        
      box = PytorchBuilderBox()
      
      box.train()
      simply_ai.add_to_train_queue(box: Box)
      simply_ai.send_to_training_server(box: Box, url: Django endpoint)
      simply_ai.send_to_training_server(box: Box, domain: str, port: int)
      simply_ai.send_to_simply_ai_training_server(creds)
      
 
 ## Abilities
 + Train Models
 + Test Models
   + See Accuracy
 + Autopilot Finding Correlations 
  