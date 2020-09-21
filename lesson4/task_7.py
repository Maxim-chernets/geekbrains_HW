from functools import reduce


def bam(foo, bar):
    return foo*bar


def fuct(n):
        list = [el for el in range(1, n+1)]
        fuct = reduce(bam, list)
        yield fuct


for el in fuct(6):
    print(el)

# ------------------------ вар 2
# watch task_7_alt.py
