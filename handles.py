def handle_error_code(error:str):
    if 'Cannot' in error:
        return 2
    else:
        return 3