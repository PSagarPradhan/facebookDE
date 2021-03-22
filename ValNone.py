def ReplaceNone(A):
    repl = None
    for i in range(len(A)):
        if A[i]:
            repl = A[i]
        else:
            A[i] = repl
    return A


a = ReplaceNone([None,1,2,3,None,None, 5,6,None])
print(a)