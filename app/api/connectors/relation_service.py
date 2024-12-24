import pandas as pd
import requests

from app.api.processing.process_response import create_map_for_groups_with_common_goal, create_map_for_groups_unique, \
    create_map_for_shared_attack_type_in_groups
from app.flow.create_map import create_table

path_relation="http://127.0.0.1:5000/api/relation"
def get_groups_with_common_goal_by_location(country):
    response = requests.get(url=f"{path_relation}/groups_with_common_goal_by_location/{country}")
    res = response.json()
    return create_map_for_groups_with_common_goal(res)


def get_unique_groups_by_location(country):
    response = requests.get(url=f"{path_relation}/unique_groups_by_location/{country}")
    res = response.json()
    return  create_map_for_groups_unique(res)

def get_shared_goals_in_groups_by_year(year):
    response = requests.get(url=f"{path_relation}/shared_goals_in_groups_by_year/{year}")
    res = response.json()
    return pd.DataFrame(res['res']).to_html(index=False, escape=False)


def get_shared_attack_type_in_groups_by_location(country):
    response = requests.get(url=f"{path_relation}/shared_attack_type_in_groups_by_location/{country}")
    res = response.json()
    return create_map_for_shared_attack_type_in_groups(res)

RELATION_FUNCTIONS = {
    "get_groups_with_common_goal_by_location": get_groups_with_common_goal_by_location,
    "get_unique_groups_by_location": get_unique_groups_by_location,
    "get_shared_goals_in_groups_by_year": get_shared_goals_in_groups_by_year,
    "get_shared_attack_type_in_groups_by_location": get_shared_attack_type_in_groups_by_location,
}
