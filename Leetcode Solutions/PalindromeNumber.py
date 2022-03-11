class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        w = str(x)
        split = list(w)
        if len(split)%2 == 0:
            first = []
            second = []
            for i in range(len(split)//2):
                first.append(split[i])
                second.append(split[len(split)-1-i])
        else:
            middle_number = ((len(split)+1)/2)-1
            split.pop(int(middle_number))
            first = []
            second = []
            for i in range(len(split)//2):
                first.append(split[i])
                second.append(split[len(split)-1-i])
        if first == second:
            return True
        else:
            return False
        

