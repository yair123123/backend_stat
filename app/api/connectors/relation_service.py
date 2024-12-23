import requests


path_relation="http://127.0.0.1:5000/api/relation"
def get_groups_with_common_goal_by_location(country):
    response = requests.get(url=f"{path_relation}/groups_with_common_goal_by_location/{country}")
    return response.json()


def get_both_groups_in_event_by_location(country):
    response = requests.get(url=f"{path_relation}/both_groups_in_event_by_location/{country}")
    return response.json()


def get_shared_goals_in_groups_by_year(year):
    response = requests.get(url=f"{path_relation}/shared_goals_in_groups_by_year/{year}")
    return response.json()


def get_shared_attack_type_in_groups_by_location(country):
    response = requests.get(url=f"{path_relation}/shared_attack_type_in_groups_by_location/{country}")
    return response.json()
