def handle_error_code(error:str):
    if 'Cannot' in error:
        return 2
    else:
        return 3
    

def handle_equation(equation:str, charts:list[str]):
    new_equation = ""
    # print(equation, charts)
    for index, s in enumerate(equation):
        if s in charts and index>0 and equation[index-1].isdigit():
            new_equation+=f"*{s}"
        else:
            new_equation+=s
    return new_equation
