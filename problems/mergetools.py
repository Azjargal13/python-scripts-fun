def mergeTool(string, k):
    n = len(string)
    r = n//k
    for i in range(r):
        subs = string[:k]
        string = string.replace(subs,'')
        d=removeSame(subs)
        print(''.join(str(key) for key in d.keys()))

def removeSame(substring):
    dict_={}
    for i in range(len(substring)):
        dict_[substring[i]] = substring[i]
    return dict_
mergeTool('AABCAAADA', 3)