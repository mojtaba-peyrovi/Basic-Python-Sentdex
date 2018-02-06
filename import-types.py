import statistics as s
list = [2,3,4,5,6,8,9,8,4]
x = s.variance(list)
#! or

from statistics import variance
list = [2,3,4,5,6,8,9,8,4]
y = variance(list)

#! or

from statistics import variance as v
list = [2,3,4,5,6,8,9,8,4]
z = v(list)

#! or
from statistics import variance, mean
list = [2,3,4,5,6,8,9,8,4]
t = variance(list)
m = mean(list)


#! or
from statistics import variance as v, mean as m
list = [2,3,4,5,6,8,9,8,4]
p = v(list)
q = m(list)
#! or
from statistics import *
list = [2,3,4,5,6,8,9,8,4]
a = variance(list)
b = mean(list)
