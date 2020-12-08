from math import factorial

from Card import Card
from Hand import Hand
from tqdm import tqdm
from time import time
import numpy as np
# start=time()
# n=22000
# for i in tqdm(range(n)):
#     hh=Hand(Card.generate_hand(7))
#     hh.all
# end=time()
#
# print(str(end-start)+" sec elapsed")
a = Card(1, 1)
b = Card(2, 1)
c = Card(3, 1)
d = Card(4, 1)
e = Card(5, 1)
f = Card(6, 2)
g = Card(8, 3)
h = Card(9, 0)
i = Card(8, 0)

hh = [a, b, c, d, e, f, g, h, i]

hh = Hand(hh)
max=hh.straight_flush()
start=time()

print(hh.force)
end=time()
print(str(end-start)+" sec elapsed")