import numpy as np
# from layers import *
class Net(object):
    def __init__(self,layers):
        self.layers = layers
    def forward(self,inputs):
        for layer in self.layers:
            inputs = layer.forward(inputs)
        return inputs
    def backwards(self,grad):
        all_grads = []
        for layer in self.layers:
            grad = layer.backward()
            all_grads.append(layer.grads)
        return all_grads[:,:,-1]
    def get_params_and_grads(self):
        for layer in self.layers:
            yield layer.params,layer.grads
    def get_params(self):
        return [layer.params for layer in self.layers]
    def set_parameters(self,params):
        for i,layer in enumerate(self.layers):
            for key in layer.params.keys():
                layer.params[key] = params[i][key]

