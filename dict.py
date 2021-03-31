from collections import OrderedDict

d = OrderedDict()
d['one'] = 1
d['two'] = 2
d['three'] = 3

for key in d:
    print(key, d[key])
