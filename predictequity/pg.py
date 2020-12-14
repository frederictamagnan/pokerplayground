from scipy.sparse import load_npz
import numpy as np
import torch
import torch.optim as optim
import torch.nn as nn
from predictequity.SimpleCNNNet import SimpleCNNNet



trainloader = torch.utils.data.DataLoader(x, batch_size=4,
                                          shuffle=True, num_workers=2)

net=SimpleCNNNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

