class Solution(object):
    def repeatedNTimes(self, A):
        for i in A:
			if A.count(i)>1:
				return i
