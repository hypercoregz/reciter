# coding=utf-8
import argparse
import random

t = 0
d = []
succ = False
ans = ''

# read the arguments and parse them into a 2D list
parser = argparse.ArgumentParser(description='Simple dictation tool.')
parser.add_argument('file', help='the dictionary you want to recite', action='store', nargs=1, type=file)
parser.add_argument('-r', '--reverse', help='reversely recite(ignored when using with "-R")', action='store_true')
parser.add_argument('-R', '--random', help='randomly recite', action='store_true')
args=parser.parse_args()
for k in args.file[0].read().strip().split('\n'):
     d.append(k.split())

# reverse or randomly the 2D list(if needed)
if args.reverse and not args.random:
    d.reverse()
elif args.random:
    random.shuffle(d)

print(args)
# main loop
while(not succ):
    succ = True
    print('\nTurn %s' % (t + 1))
    for k in d:
        if k[1] != True:
            ans = k[1]
            if raw_input('%s:' % k[0]) == ans:
                k[1] = True
            else:
                print("^\n%s" % ans)
        for j in d:
            if j[1] != True:
                succ = False
                break
    if succ:
        print("Congratulations! You've completed reciting the file '%s' in %s turn(s)!" % (args.file[0].name, t))
        break
    t += 1
