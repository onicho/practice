
from numpy import *
from scipy.stats.stats import pearsonr


array1 = []

with open("values1.txt", "r") as ins:
    for line in ins:
        array1.append(line.rstrip('\n').rstrip('\r'))


array2 = []

with open("values2.txt", "r") as ins:
    for line in ins:
        array2.append(line.rstrip('\n').rstrip('\r'))

array3 = []

with open("values3.txt", "r") as ins:
    for line in ins:
        array3.append(line.rstrip('\n').rstrip('\r'))

arrayMKT = []

with open("MKTvalues.txt", "r") as ins:
    for line in ins:
        arrayMKT.append(line.rstrip('\n').rstrip('\r'))

values3 = [float(i) for i in array3]
values1 = [float(i) for i in array1]
values2 = [float(i) for i in array2]
MKTvalues = [float(i) for i in arrayMKT]

# correlation1 = pearsonr(values1, values2)
# correlation = corrcoef([values1, values2, values3])
# print(correlation1, '\n', correlation, )

test_cov = cov(values1,MKTvalues,ddof=0)[0][1] # defo need this one!

print(test_cov)

test_var = var(MKTvalues)

print(test_var)

beta = test_cov/test_var

print("%.2f" % beta)