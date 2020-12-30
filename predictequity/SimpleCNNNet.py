import torch.nn as nn
import torch.nn.functional as F
import torch
from Logging import Logging

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()

        # self.fc1=nn.Linear()


        self.fc1 = nn.Linear(360, 3000)
        # self.log.debug(x.size())
        self.fc2=nn.Linear(3000,300)

        self.fc3=nn.Linear(300,200)
        self.fc4=nn.Linear(200,90)
        self.linear = nn.Sequential(*[nn.Linear(90,90) for i in range(10)])
        self.fc5 = nn.Linear(90, 6)
        self.softmax = nn.Softmax(dim=1)

        self.log = Logging()

    def forward(self, x):

        self.log.debug(x.size())
        x=x.view(-1,6*15*4)

        self.log.debug(x.size())
        x=self.fc1(x)
        self.log.debug(x.size())
        x=self.fc2(x)

        self.log.debug(x.size())
        x=self.fc3(x)
        self.log.debug(x.size())
        x=self.fc4(x)
        x = self.linear(x)
        self.log.debug(x.size())
        x=self.fc5(x)

        self.log.debug(x.size())
        x=self.softmax(x)
        return x
class Simple3DNet(nn.Module):
    def __init__(self):
        super(Simple3DNet, self).__init__()
        self.conv1 = nn.Conv3d(1,12,5)

        self.pool1 = nn.MaxPool3d(2,2)
        self.conv2 = nn.Conv3d(12, 24, 3)
        # self.pool2 = nn.MaxPool3d(2,2)


        self.fc1 = nn.Linear(1536, 100)
        self.fc2=nn.Linear(100,30)
        self.fc3 = nn.Linear(30, 6)
        self.softmax = nn.Softmax(dim=1)
        self.log=Logging()
    def forward(self, x):
        batch_size=x.size()[0]
        self.log.debug(x.size())
        x=self.conv1(x)
        self.log.debug(x.size())
        x = self.pool1(x)
        self.log.debug(x.size())

        x = self.conv2(x)
        self.log.debug(x.size())

        # x = self.pool2(x)
        self.log.debug(x.size())

        x = x.view(-1, 1536)
        self.log.debug(x.size())

        x = F.relu(self.fc1(x))
        self.log.debug(x.size())
        x = F.relu(self.fc2(x))
        self.log.debug(x.size())
        x = F.relu(self.fc3(x))
        self.log.debug(x.size())
        x=self.softmax(x)
        return x

class SimpleCNNNet(nn.Module):
    def __init__(self):
        super(SimpleCNNNet, self).__init__()
        self.conv1 = nn.Conv2d(6, 12,5)
        # self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(12, 24, 5)
        self.conv3=nn.Conv2d(24,48,5)
        # self.pool2 = nn.MaxPool2d(2, 2)
        # self.conv4=nn.Conv2d(48,96,5)


        self.fc1 = nn.Linear(48*5*5, 100)
        self.fc2=nn.Linear(100,30)
        self.fc3 = nn.Linear(30, 6)
        self.softmax = nn.Softmax(dim=1)
        self.log=Logging()
    def forward(self, x):
        batch_size=x.size()[0]
        self.log.debug(x.size())
        x=self.conv1(x)
        self.log.debug(x.size())
        # x = self.pool1(x)
        self.log.debug(x.size())
        x = self.conv2(x)
        self.log.debug(x.size())
        x = self.conv3(x)
        self.log.debug(x.size())
        # x = self.conv4(x)
        # self.log.debug(x.size())
        # x = self.pool1(x)
        self.log.debug(x.size())
        x = x.view(-1, 1200)
        self.log.debug(x.size())

        x = F.relu(self.fc1(x))
        self.log.debug(x.size())
        x = F.relu(self.fc2(x))
        self.log.debug(x.size())
        x = F.relu(self.fc3(x))
        self.log.debug(x.size())
        x=self.softmax(x)
        return x

# class SimpleCNNNet(nn.Module):
#     def __init__(self):
#         super(SimpleCNNNet, self).__init__()
#         self.conv1A_c = nn.Conv3d(1, 3, (12,5,4))
#         self.conv2A_c = nn.Conv3d(3,9, (1,5,1))
#         self.conv1A_b = nn.Conv3d(1, 3, (5, 5, 4))
#         self.conv2A_b = nn.Conv3d(3, 9, (1, 5, 1))
#
#
#         self.conv1B_c = nn.Conv3d(1, 3, (2, 2, 1))
#         self.conv2B_c = nn.Conv3d(3, 9, (2, 2, 1))
#         self.conv1B_b = nn.Conv3d(1, 3, (2, 2, 1))
#         self.conv2B_b = nn.Conv3d(3, 9, (1, 2, 1))
#
#
#         self.fc1 = nn.Linear(6678, 90)
#         self.fc2 = nn.Linear(90, 6)
#         self.softmax = nn.Softmax(dim=1)
#         self.log=Logging()
#     def forward(self, x_c,x_b):
#         batch_size=x_c.size()[0]
#         xA_c=self.conv1A_c(x_c)
#         self.log.debug(xA_c.size())
#         xA_c=self.conv2A_c(xA_c)
#         self.log.debug(xA_c.size())
#         xA_b = self.conv1A_b(x_b)
#         self.log.debug(xA_b.size())
#         xA_b = self.conv2A_b(xA_b)
#         self.log.debug(xA_b.size())
#
#         xB_c = self.conv1B_c(x_c)
#         self.log.debug(xB_c.size())
#         xB_c = self.conv2B_c(xB_c)
#         self.log.debug(xB_c.size())
#         xB_b = self.conv1B_b(x_b)
#         self.log.debug(xB_b.size())
#         xB_b = self.conv2B_b(xB_b)
#         self.log.debug(xB_b.size())
#
#         xA_c=xA_c.view(batch_size,-1)
#         xA_b = xA_b.view(batch_size, -1)
#         xB_c = xB_c.view(batch_size, -1)
#         xB_b = xB_b.view(batch_size, -1)
#
#         x=torch.cat((xA_c,xA_b,xB_c,xB_b),dim=1)
#         self.log.debug(x.size())
#         x = x.view(-1, 6678)
#         x = F.relu(self.fc1(x))
#         # x = F.relu(self.fc2(x))
#         x = F.relu(self.fc2(x))
#         # self.log.debug(x.size())
#         x=self.softmax(x)
#         return x
