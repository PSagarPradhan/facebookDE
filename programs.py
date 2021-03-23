class Monotonic:
    def isMonotonic1(self, A: List[int]) -> bool:
        sign = 1 if A[-1] >= A[0] else -1
        for i in range(len(A) - 1):
            if (A[i + 1] - A[i]) * sign < 0:
                return False
        return True

    def isMonotonic2(self, A: List[int]) -> bool:   ##fast but uses in built python function reverse
        if len(A) < 3:
            return True
        
        def check(B):
            i = 1
            while i < len(B):
                if B[i] < B[i-1]:
                    return False
                i += 1
            return True
        
        return check(A) or check(list(reversed(A)))


    def isMonotonic3(self, A):   ### slow
        isIncreasing=True
        isDecreasing=True
        for i in range(len(A)-1):
            if(A[i]>A[i+1]):
                isIncreasing=False
            elif(A[i]<A[i+1]):
                isDecreasing=False
        return isIncreasing or isDecreasing


    def isMonotonic4(self, A: List[int]) -> bool:    #fast solution
        
        #set s as first element
        s = A[0]
		# determine if going up or down
        if A[0] - A[-1] < 0:                       #going up 
            for i in A: 
                if i > s: 
                    s = i
                if i < s: 
                    return False
            return True
        else:                                      #going down
            for i in A: 
                if i < s: s = i
                if i > s: return False
            return True


