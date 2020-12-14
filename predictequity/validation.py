
import torch
from predictequity.EquityDataset import EquityDataset
import torch.nn as nn
from predictequity.SimpleCNNNet import SimpleCNNNet,SimpleNet
import torch.optim as optim

PATH = './model/poker_net.pth'

full_dataset = EquityDataset()

train_size = int(0.8 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])

trainloader = torch.utils.data.DataLoader(train_dataset,batch_size=256)
testloader = torch.utils.data.DataLoader(test_dataset,batch_size=len(test_dataset))
net=SimpleNet()
correct = 0
total = 0
net.load_state_dict(torch.load(PATH))
with torch.no_grad():
    for data in testloader:
        x_c,x_b, y = data
        outputs = net(x_c,x_b)
        _, predicted = torch.max(outputs.data, 1)
        _,y_max=torch.max(y.data,1)
        total += y.size(0)
        correct += (predicted == y_max).sum().item()

print('Accuracy of the network on the 10000 test images: %d %%' % (
    100 * correct / total))