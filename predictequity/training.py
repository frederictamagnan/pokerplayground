import torch
from predictequity.EquityDataset import EquityDataset
import torch.nn as nn
from predictequity.SimpleCNNNet import SimpleCNNNet,SimpleNet
import torch.optim as optim
full_dataset = EquityDataset()

train_size = int(0.5 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])


trainloader = torch.utils.data.DataLoader(train_dataset,batch_size=256)
testloader = torch.utils.data.DataLoader(test_dataset,batch_size=len(test_dataset))
net=SimpleNet()

criterion = nn.BCELoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

for epoch in range(30):  # loop over the dataset multiple times

    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        # get the inputs; data is a list of [inputs, labels]
        x_c,x_b,y = data

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(x_c,x_b)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        # print statistics
        running_loss += loss.item()
        if i % 15 == 14:    # print every 20 mini-batches
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 20))
            running_loss = 0.0
            correct = 0
            total = 0

            for data in testloader:
                x_c,x_b, y = data
                outputs = net(x_c,x_b)
                _, predicted = torch.max(outputs.data, 1)
                _, y_max = torch.max(y.data, 1)
                total += y.size(0)
                correct += (predicted == y_max).sum().item()

            print('Accuracy of the network on the 10000 test images: %d %%' % (
                100 * correct / total))
PATH = './model/poker_net.pth'
torch.save(net.state_dict(), PATH)
print('Finished Training')