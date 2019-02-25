import program
import time
import sys

DIFFICULTY = 'eazy'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        DIFFICULTY = sys.argv[1]
    fo = open(DIFFICULTY + '.txt', "r+")
    ans = open("ans_"+DIFFICULTY+'.txt', "w")
    data = fo.readlines()
    t1 = time.time()
    for line in data:
        words = line.split(' ')
        action = words[0]
        if action == 'Add':
            program.add(int(words[1]), int(words[2]))
        elif action == 'Sub':
            program.sub(int(words[1]), int(words[2]))
        elif action == 'Query':
            ans.write(str(program.query(int(words[1]), int(words[2]))) + '\n')

    t2 = time.time()
    print("耗时%fs" % (t2 - t1))

    fo.close()
    ans.close()
