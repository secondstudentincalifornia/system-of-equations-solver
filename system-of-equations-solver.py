"""
    Solve systems of equation using gaussian elimination method.
"""
from fractions import Fraction as fraction   

number_of_terms = int(input("Number of terms: "))
equations = [[fraction(1,1),fraction(1,1),fraction(-3,1),fraction(1,1),fraction(2,1)],[fraction(-5,1),fraction(3,1),fraction(-4,1),fraction(1,1), fraction(0,1)],[fraction(1,1),fraction(0,1),fraction(2,1),fraction(-1,1),fraction(1,1)],[fraction(1,1), fraction(2,1), fraction(0,1), fraction(0,1),fraction(12,1)]]
# for i in range(number_of_terms):
#     equations.append(list(map(fraction, input("Equation {} (please only input the numbers): ".format(i + 1)).split())))


# you want the matrix to be in the upper triangular form

def adding_to_eq(n, m, xn):
    add = -1*fraction(m[xn]/n[xn])
    for x in range(len(n)):
        n[x] *= add
        n[x] = n[x] + m[x]
    return(n)

for zeros_to_change in range(number_of_terms):
    for j in range(zeros_to_change):
        if equations[zeros_to_change][j] == 0:
            continue
        
        equations[zeros_to_change] = adding_to_eq(equations[zeros_to_change], equations[j], j)
        
#reverse substitution
answers = [0]*number_of_terms
try:
    for u in range(number_of_terms-1, -1, -1):
        constant = equations[u][-1]
        for w in range(number_of_terms):
            constant -= equations[u][w]*answers[w]
        answers[u] = constant/equations[u][u]
    print(answers)
except ZeroDivisionError:
    print("no solutons available")
    



# print(equations)