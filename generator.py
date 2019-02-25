# 数据生成器
import random
eazy1000 = 1000
eazy10000 = 10000
hard = 100000

def gen(maxn):
    fo = open('%d.txt' % maxn, 'w')
    random.seed(1)
    for i in range(1, maxn):
        action = random.sample(['Add', 'Sub', 'Query'], 1)[0]

        a = random.randint(1, 1000000)
        b = random.randint(1, 1000000)
        if action == 'Query' and a > b:
            a, b = b, a
        fo.write("%s %d %d\n" % (action, a, b))
    fo.close()


gen(eazy1000)
gen(eazy10000)
gen(hard)

