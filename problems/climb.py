# climbing the leaderboard
from collections import OrderedDict, Counter
# import math
# import os
# import random
# import re
# import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    ab = OrderedDict()
    
    for i in scores:
        ab[i]=i
    print(Counter(ab))
    #OrderedDict()
    
    # count = 1
    # for i in range(len(sorted(scores, reverse=True))):
    #     if i<=len(scores)-2:
    #         if scores[i]==scores[i+1]:
    #             count +=1
    #             ab[scores[i]]=count
    #     ab[scores[i]]=count
    print(ab)

all_ = [100,90,90,80,75,60]
alice = [50,65,77,90,102]

climbingLeaderboard(all_, alice)