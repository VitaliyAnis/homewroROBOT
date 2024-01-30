import random
lst = ['robot'] * 10
lst += ['himan'] * 10
random.shuffle(lst)
print('robot', 'human')
for i in lst:
    if i == 'robot':
        print(1 , 0)
    else:
        print(0, 1)