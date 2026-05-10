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
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_map = Counter(t)
        t_map = Counter(s)
        print(s_map == t_map)
        return s_map == t_map
''' 