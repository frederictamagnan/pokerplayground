import torch.nn as nn
import torch.nn.functional as F
import torch
from Logging import Logging
class SimpleCNNNet(nn.Module):
    def __init__(self):
        super(SimpleCNNNet, self).__init__()
        self.conv1A_c = nn.Conv3d(1, 3, (12,5,4))
        self.conv2A_c = nn.Conv3d(3,9, (1,5,1))
        self.conv1A_b = nn.Conv3d(1, 3, (5, 5, 4))
        self.conv2A_b = nn.Conv3d(3, 9, (1, 5, 1))


        self.conv1B_c = nn.Conv3d(1, 3, (2, 2, 1))
        self.conv2B_c = nn.Conv3d(3, 9, (2, 2, 1))
        self.conv1B_b = nn.Conv3d(1, 3, (2, 2, 1))
        self.conv2B_b = nn.Conv3d(3, 9, (1, 2, 1))


        self.fc1 = nn.Linear(6678, 90)
        self.fc2 = nn.Linear(90, 3)
        self.softmax = nn.Softmax(dim=1)
        self.log=Logging()
    def forward(self, x_c,x_b):
        batch_size=x_c.size()[0]
        xA_c=self.conv1A_c(x_c)
        self.log.debug(xA_c.size())
        xA_c=self.conv2A_c(xA_c)
        self.log.debug(xA_c.size())
        xA_b = self.conv1A_b(x_b)
        self.log.debug(xA_b.size())
        xA_b = self.conv2A_b(xA_b)
        self.log.debug(xA_b.size())

        xB_c = self.conv1B_c(x_c)
        self.log.debug(xB_c.size())
        xB_c = self.conv2B_c(xB_c)
        self.log.debug(xB_c.size())
        xB_b = self.conv1B_b(x_b)
        self.log.debug(xB_b.size())
        xB_b = self.conv2B_b(xB_b)
        self.log.debug(xB_b.size())

        xA_c=xA_c.view(batch_size,-1)
        xA_b = xA_b.view(batch_size, -1)
        xB_c = xB_c.view(batch_size, -1)
        xB_b = xB_b.view(batch_size, -1)

        x=torch.cat((xA_c,xA_b,xB_c,xB_b),dim=1)
        self.log.debug(x.size())
        x = x.view(-1, 6678)
        x = F.relu(self.fc1(x))
        # x = F.relu(self.fc2(x))
        x = F.relu(self.fc2(x))
        # self.log.debug(x.size())
        x=self.softmax(x)
        return x

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()

        # self.fc1=nn.Linear()


        self.fc1 = nn.Linear(1020, 1020)
        # self.log.debug(x.size())
        self.fc2=nn.Linear(1020,1020)
        self.fc3=nn.Linear(1020,200)
        self.fc4=nn.Linear(200,90)
        self.fc5 = nn.Linear(90, 3)
        self.softmax = nn.Softmax(dim=1)

        self.log = Logging()

    def forward(self, x_c,x_b):
        x=torch.cat((x_c,x_b),dim=2)
        self.log.debug(x.size())
        x=x.view(-1,17*15*4)

        self.log.debug(x.size())
        x=self.fc1(x)
        self.log.debug(x.size())
        x=self.fc2(x)
        self.log.debug(x.size())
        x=self.fc3(x)
        self.log.debug(x.size())
        x=self.fc4(x)
        self.log.debug(x.size())
        x=self.fc5(x)
        self.log.debug(x.size())
        x=self.softmax(x)
        return x