import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

remember_sequences = {0:0} # keep dict to remember first index we saw a digit in
recurrence, ret = 1, '0.' 
# recurrence is used to remember sequences we already encountered

while recurrence not in remember_sequences: # while we visit a new magnitude continue
    remember_sequences[recurrence] = len(ret) # keep our current length
    
    last_digit, recurrence = divmod(10*recurrence, n)
    ret += str(last_digit)    

if recurrence:
    ret = '%s(%s)' % (ret[:remember_sequences[recurrence]], ret[remember_sequences[recurrence]:]) # put last recurrence we saw in brackets like is asked of us

print(ret)
