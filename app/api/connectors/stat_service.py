import requests

path_stat="http://127.0.0.1:5000/api/stat"
def get_most_deadly(top):
    response = requests.get(url=f"{path_stat}/most_deadly/{top}")
    return response.json()


def average_casualties(top):
    response = requests.get(url=f"{path_stat}/average_casualties_by_area/{top}")
    return response.json()


def get_top_5_most_num_spread():
    response = requests.get(url=f"{path_stat}/top_5_most_num_spread")
    return response.json()


def get_most_group_active_by_region():
    response = requests.get(url=f"{path_stat}/most_group_active_by_region")
    return response.json()


def get_history_events_by_year(year):
    response = requests.get(url=f"{path_stat}/history_events_by_year/{year}")
    return response.json()
