class Solution(object):
    def romanToInt(self, s):
        l1 = ['I','V','X','L','C','D','M']
        l2 = ['1','5','10','50','100','500','1000'] 
        x = 0
        for i in s:
            x = x + int(l2[l1.index(i)])
        x -= s.count("IV")*2 + s.count("IX")*2 + s.count("XC")*20 + s.count("XL")*20 + s.count("CD")*200 + s.count("CM")*200
        return x
        