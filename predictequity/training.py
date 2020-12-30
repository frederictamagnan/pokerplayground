import torch
from predictequity.EquityDataset import EquityDataset
import torch.nn as nn
from predictequity.SimpleCNNNet import SimpleCNNNet,SimpleNet,Simple3DNet
import torch.optim as optim
import numpy as np
full_dataset = EquityDataset()

train_size = int(0.9 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])


trainloader = torch.utils.data.DataLoader(train_dataset,batch_size=64)
testloader = torch.utils.data.DataLoader(test_dataset,batch_size=len(test_dataset))
net=SimpleCNNNet()

model_parameters = filter(lambda p: p.requires_grad, net.parameters())
params = sum([np.prod(p.size()) for p in model_parameters])

print("number of parameters",params)
criterion = nn.BCELoss()
# criterion=nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=0.001)

for epoch in range(25):  # loop over the dataset multiple times

    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        # get the inputs; data is a list of [inputs, labels]
        X,y = data

        # zero the parameter gradients
        optimizer.zero_grad()
        # forward + backward + optimize
        outputs = net(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        # print statistics
        running_loss += loss.item()
        if i % 10 == 9:    # print every 20 mini-batches
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 20))
            running_loss = 0.0
            correct = 0
            total = 0

            for data in testloader:
                X, y = data
                outputs = net(X)
                # outputs=outputs.reshape(-1,6,3)
                _, predicted = torch.max(outputs, 1)
                # y=y.reshape(-1,6,3)
                _, y_max = torch.max(y, 1)
                total += y.size(0)
                correct += (predicted == y_max).sum().item()
                # correct += (predicted == y).sum().item()
            print('Accuracy of the network on the 10000 test images: %d %%' % (
                100 * correct / total))
PATH = './model/poker_cnnnet2.pth'
torch.save(net.state_dict(), PATH)
print('Finished Training')