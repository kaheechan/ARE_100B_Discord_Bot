from sympy import *

def derivative(function, variable):
    return diff(function, variable)

def solution(function, variable):
    return solve(function, variable)

def systems(function_1, function_2, variable):
    function_1 = simplify(function_1)
    function_2 = simplify(function_2)
    result = simplify(function_1 - function_2)
    return solve(result, variable)



