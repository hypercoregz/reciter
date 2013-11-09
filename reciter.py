# coding=utf-8
import argparse

t = 0
d = {}
succ = False
ans = ''

# read the arguments and parse them into a dictionary
parser = argparse.ArgumentParser(description='Simple dictation tool.')
parser.add_argument('file', help='the dictionary you want to recite.', action='store', nargs=1, type=file)
parser.add_argument('-r', '--reverse', help='reversely recite.', action='store_true')
args=parser.parse_args()
for k in args.file[0].read().strip().split('\n'):
    j = k.split()
    d[j[0]] = j[1]
# print d

# main loop
while(not succ):
    succ = True
    print('\nTurn %s' % (t + 1))
    for k in d:
        if d[k] != True:
            ans = d[k]
            if raw_input('%s:' % k) == ans:
                d[k] = True
            else:
                print("^\n%s" % ans)
        for j in d:
            if d[j] != True:
                succ = False
                break
    if succ:
        print("Congratulations! You've completed reciting the file '%s' in %s turn(s)!" % (args.file[0].name, t))
        break
    t += 1
