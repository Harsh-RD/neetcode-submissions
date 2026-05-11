class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count={}
        for i in s:
            count[i]=count.get(i,0)+1
        for j in t:
            count[j]=count.get(j,0)-1
        for value in count.values():
            if value!=0:
                return False
        return True
'''
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        print(Counter(s) == Counter(t))
        return s_map == t_map


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if s.count(c)!=t.count(c):
                return False
        return True
''' 