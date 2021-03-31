# def wordOrder(arr):
#     diction = {}
#     counter = 0
#     for i in arr:
#         if i in diction.keys():
#             counter +=1
#             diction[i] = counter
#             #print('yaa')
#         else:
#             diction[i] = counter
#             #print('noo')
#     print(len(diction))
#     print(" ".join(str(value+1) for value in diction.values()))
# # n = input()
# # arr = []
# # for i in range(int(n)):
# #     arr.append(input())
# arr = ['bcdef',
# 'abcdefg',
# 'bcde',
# 'bcdef']
# wordOrder(arr)

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
#print(d)