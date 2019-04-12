import sys
sys.path.extend(['args', 'retrieve'])

# importing related modules
import retreive, args, pushData

r = retreive.retrieve()
r.retrieve()
p = pushData.pushdata()
p.pushdata()

args.arguments()
