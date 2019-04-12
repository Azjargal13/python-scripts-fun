'''
Command line option parser
'''

import argparse

parser = argparse.ArgumentParser(description="Retrieve data from analog ang digital sensors")

parser.add_argument('-i', '--interval', help='specify interval of data acquisition in millseconds (ms)')
parser.add_argument('-c', '--count', help='specify maximum counts of row of data in a cycle')
parser.add_argument('-o', '--outdir',help='specify directory data are saved')

# args = parser.parse_args()
args = parser.parse_args()