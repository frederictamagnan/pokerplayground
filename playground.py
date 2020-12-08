from math import factorial

from Card import Card
from Hand import Hand
from tqdm import tqdm
from time import time
start=time()
n=22000
for i in tqdm(range(n)):
    hh=Hand(Card.generate_hand(7))
    hh.all
end=time()

print(str(end-start)+" sec elapsed")
