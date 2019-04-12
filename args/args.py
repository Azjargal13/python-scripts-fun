'''
Command line option parser
Receive data gathering interval, count that is row of data in a cycle
Output directory where data will be saved

If options are not given, default values will be set.
'''

import argparse, os

def arguments():
    # show arguments
    parser = argparse.ArgumentParser(description="Retrieve data from analog ang digital sensors")
    parser.add_argument('-i', '--interval', type=int, dest='interval', default='10', help='specify interval of data acquisition in millseconds (ms)')
    parser.add_argument('-c', '--count', dest='count',type=int, default='500', help='specify maximum counts of row of data in a cycle')
    parser.add_argument('-o', '--outdir', dest='outdir',type=str, default='.', help='specify directory data are saved')
    args = parser.parse_args()

    # receive and validate input argument
    a = Arguments(args.interval, args.count, args.outdir)
    a.validateArgs()
    a.readArgs()
    #Arguments(args).readArgs()
    #validateArgs(args.interval, args.count, args.outdir)
    #readArgs(args.interval, args.count, args.outdir)
# make class for arguments



class Arguments:
    def __init__(self, ival, cnt, out):
        self.ival=ival
        self.cnt=cnt
        self.out=out
    def readArgs (self):
        print(self.ival, self.cnt, self.out)
    def validateArgs(self):
        if self.ival < 5 or self.ival > 60000 :
            raise ValueError("unexpected interval value. Input from 5 to 60000")
        elif self.cnt<1 :
            raise ValueError("unexpected count value. Input 1 or more")
        elif self.dirExist() is False:
            raise ValueError("unexpected directory path. Input existing directory")
    def dirExist(self):
        if os.path.isdir(self.out):
            return True
        else:
            return False

# def readArgs (interval, count, outdir):
#     print(interval,count,outdir)
# def validateArgs(ival, cnt, out):
#     if ival < 5 or ival > 60000 :
#         raise ValueError("unexpected interval value. Input from 5 to 60000")
#     elif cnt <1 :
#         raise ValueError("unexpected count value. Input 1 or more")
#     elif dirExist(out) is False:
#         raise ValueError("unexpected directory path. Input existing directory")

# def dirExist(dirPath):
    # if os.path.isdir(dirPath):
    #     return True
    # else:
    #     return False

# class Arguments:
#     def __init__(self):
#         return None

#     # @property 
#     # def readArgs (self, interval, count, outdir):
#     #     print(interval,count,outdir)

#     # @property
#     def validateArgs(self, arguments):
#         interval = self.arguments.interval
#         count = self.arguments.count
#         outdir = self.arguments.outdir
#         print(interval, count, outdir)
    
#     def arguments():
#         parser = argparse.ArgumentParser(description="Retrieve data from analog ang digital sensors")
#         parser.add_argument('-i', '--interval', dest='interval', default='10', help='specify interval of data acquisition in millseconds (ms)')
#         parser.add_argument('-c', '--count', dest='count', default='500', help='specify maximum counts of row of data in a cycle')
#         parser.add_argument('-o', '--outdir', dest='outdir', default='.', help='specify directory data are saved')
#         args = parser.parse_args()
#         validateArgs(args)

#   Arguments.readArgs()
#     print(args.interval, args.count)
#     readArgs(args.interval, args.count, args.outdir)