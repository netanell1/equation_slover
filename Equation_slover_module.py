from sympy import symbols, Eq, solve
from handles import handle_equation


def solve_equation_with_one_variable(equation:str)->list:
    # Define the variable
    x = symbols("x")

    # Parse the user input to extract coefficients and constants
    equation = handle_equation(equation, ['x'])
    print(equation)
    equation_parts = equation.split("=")
    left_side = equation_parts[0].strip()
    right_side = equation_parts[1].strip()

    # Create the equation
    equation = Eq(eval(left_side), eval(right_side))

    # Solve the equation
    solution = solve(equation, x)

    # Print the solution
    return solution


def solve_equations_with_two_variables(eq1:str, eq2:str):
    x=  symbols('x')
    y = symbols('y')
       # Parse the user input to extract coefficients and constants
    eq1 = handle_equation(eq1, ['x','y'])
    eq2 = handle_equation(eq2, ['x', 'y'])
    equation_parts_eq1 = eq1.split("=")
    left_side_eq1 = equation_parts_eq1[0].strip()
    right_side_eq1 = equation_parts_eq1[1].strip()
    equation1 = Eq(eval(left_side_eq1), eval(right_side_eq1))

    equation_parts_eq2 = eq2.split("=")
    left_side_eq2 = equation_parts_eq2[0].strip()
    right_side_eq2 = equation_parts_eq2[1].strip()
    equation2 = Eq(eval(left_side_eq2), eval(right_side_eq2))

    solution = solve((equation1, equation2), (x, y))
    if solution:
        if type(solution) is list:
            solution_values = [{"x":str(val[0]),"y": str(val[1])} for val in solution]
        # Substitute specific values for x and y to get numerical values
        else:
            solution_values =[{"x":str(solution[x].evalf()),"y":str(solution[y].evalf())}] 
        return solution_values
    else:
        return None
