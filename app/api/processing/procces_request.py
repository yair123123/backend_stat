

def execute_function_by_name(function_name, filter):
    if function_name in globals() and callable(globals()[function_name]):
        func = globals()[function_name]
        if filter:
            return func(filter)
        return func()
