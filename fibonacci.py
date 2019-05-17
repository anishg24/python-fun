class Fibbonaci:
    def __init__(self, nums=10):
        self.nums = nums
    
    def generate(self, generateList=False):
        a, b = 0, 1
        resultList = []
        for i in range(0, self.nums):
            if generateList:
                resultList.append(a)
            else:
                print(a)
            a, b = b, a + b
        if generateList:
            return resultList

