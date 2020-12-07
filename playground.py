from math import factorial

from Card import Card
from Hand import Hand

a=Card(2,1)
b=Card(2,2)
c=Card(3,1)
d=Card(5,1)
e=Card(5,3)
h=[a,b,c,d,e]

h=Hand(h)
print("two pair",h.two_pairs())

# a_s=Card(1,1)
# b_s=Card(2,1)
# c_s=Card(3,2)
# d_s=Card(4,2)
# e_s=Card(5,3)
# h_s=[a_s,b_s,c_s,d_s,e_s]
#
#
# a_s=Card(1,1)
# b_s=Card(10,1)
# c_s=Card(11,1)
# d_s=Card(12,1)
# e_s=Card(13,1)
# h_f=[a_s,b_s,c_s,d_s,e_s]
#
# h_f=Hand(h_f)
#
# h_s=Hand(h_s)
# print(h_s)
# print(h.straight())
# print(h_s.highest_pair(),"highest pair")
#
# print(h_f.flush(),"flush")