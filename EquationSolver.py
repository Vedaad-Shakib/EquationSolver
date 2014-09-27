from numpy import matrix
from numpy import concatenate

# must be in format <coefficient><letter>+<coefficient><letter>=<number>
def solve(*args):
    for i in args:
        rightEq = matrix([int(j) for j in i.split("=")[0].split("+")])
        leftEq = matrix([int (j) for j in i.split("=")[1]])
        if locals().has_key("rightSide"):
            rightSide = concatenate((rightSide, rightEq))
            leftSide = concatenate((leftSide, leftEq))
        else:
            rightSide = rightEq
            leftSide = leftEq
    return rightSide.I*leftSide
        

def cleanOperators(eq):
    pass

def cleanFormat(eq):
    pass
    
