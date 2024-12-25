import inspect

from app.api.connectors.relation_service import RELATION_FUNCTIONS
from app.api.connectors.search_service import search_in_text
from app.api.connectors.stat_service import STATISTICS_FUNCTIONS

ALL_FUNCTIONS = {**STATISTICS_FUNCTIONS, **RELATION_FUNCTIONS,"search_in_text":search_in_text }

def execute_statistics_function(function_name, filter):
    if function_name not in ALL_FUNCTIONS:
        raise ValueError(f"Function '{function_name}' is not allowed.")

    func = ALL_FUNCTIONS[function_name]
    sig = inspect.signature(func)
    if len(sig.parameters) == 0:
        return func()
    else:
        return func(filter)
