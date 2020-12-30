# a=1.26
# b=14.5
# c=5.9
# d=a+b+c
# print((d-a)/d)
#
# print(1/a+1/b+1/c)
#
# a=1.64
# b=4.3
# c=6
# d=a+b+c
# print((d-a)/d)
# print(1/a)
# print(1/a+1/b+1/c)

def calc_marge_match_foot(cote1,cote2,cote3):

    marge=(1/cote1+1/cote2+1/cote3-1)*100
    return marge

a=1.85
b=4
c=4.1

print(calc_marge_match_foot(a,b,c))

def calc_marge_match_tennis(cote1,cote2):

    marge=(1/cote1+1/cote2-1)*100
    return marge

a=1.09
b=4

print(calc_marge_match_tennis(a,b))