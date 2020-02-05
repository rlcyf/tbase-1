import torch
import torch.nn as nn

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


# full connect layer
def fc(in_features, out_features, *args):
    layer = nn.Linear(in_features, out_features)
    nn.init.xavier_normal_(layer.weight)
    # 默认为随机初始化
    nn.init.constant_(layer.bias, 0)
    return layer


def lstm(input_size, hidden_size, num_layers, dropout):
    rnn = nn.LSTM(input_size=input_size, hidden_size=hidden_size,
                  num_layers=num_layers, dropout=dropout)
    return rnn


def init(module, weight_init, bias_init, gain=1):
    weight_init(module.weight.data, gain=gain)
    bias_init(module.bias.data)
    return module


def to_device(device, *args):
    return [x.to(device) for x in args]
