from itertools import groupby
def compress_string(string):
    a = []
    for i in groupby(string):
        #a.append(string[int(i)])
    print(a)
    # for i in range(len(string)):
    #     a = groupby(string, string[i])
    #     d.append(a)
    # print(d)

inp = 124512115533
compress_string(str(inp))