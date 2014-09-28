import re
from numpy import matrix
from numpy import concatenate

# uses inverse matrix method
# must be in format <number>+<number>=<number>; coefficients are assumed
def solve(eqs):
    for i in eqs:
        rightEq = matrix([int(j) for j in i.split("=")[0].split("+")])
        leftEq = matrix([int(i.split("=")[1])])
        if locals().has_key("rightSide"):
            rightSide = concatenate((rightSide, rightEq))
            leftSide = concatenate((leftSide, leftEq))
        else:
            rightSide = rightEq
            leftSide = leftEq
    return (rightSide.I*leftSide).T.tolist()[0] # transpose for 1 row matrix
        

def cleanOperators(eqs):
    return eqs

# checks and adds a coefficient of 1 to number without coefficient
def checkCoefficient(i):
    if i.count("-") == 0:
        return i if i[0].isdigit() else "1"+i
    else:
        return i if i[1].isdigit() else "-1"+i[1:]
    
# separates variable names and cleaned equations - reorders variables if not in correct order
# note: these few lines of code took around 45 minutes to produce :P
def removeVariables(eqs):
    # puts all variables and coefficients in array variables, adding 1 if no coefficient exists
    variables = [[checkCoefficient(i) for i in re.findall("-?[0-9]*[a-zA-Z]+", eq)] for eq in eqs]

    # gets the right side of the equation
    rightCoefficients = [[i.split("=")[1]] for i in eqs]
    
    # sorts variables alphabetically
    cleanedVariables = [sorted(i, key=lambda string: string[re.search("[a-z]", string).start():]) for i in variables]

    # gets names of variables and coefficients of variables
    leftCoefficients = [[re.sub("[a-zA-Z]", "", i) for i in j] for j in cleanedVariables]
    variableNames = [re.sub("-?[0-9]", "", i) for i in cleanedVariables[0]]

    # join right and left side for an equation that fits into the solve method above
    equations = ["+".join(left)+"="+right[0] for left, right in zip(leftCoefficients, rightCoefficients)]

    return variableNames, equations
    
         
    

def main():
    equations = []
    equation = " "
    while equation != "":
        equation = str(raw_input("Input equation " + str(len(equations)+1) + ": "))
        equations.append(equation) if equation != "" else None

    equations = cleanOperators(equations)
    variables, equations = removeVariables(equations)
    answers = solve(equations)

    print "\n".join([str(variable)+": "+str(value) for variable, value in zip(variables, answers)])

    


main()
    
