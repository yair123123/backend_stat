import requests

from app.flow.create_map import create_heatmap

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
    # response = requests.get(url=f"{path_stat}/history_events_by_year/{year}").json()
    response = [(32.0853, 34.7818), (40.7306, -73.9352), (48.8566, 2.3522), (35.6895, 139.6917), (55.7558, 37.6176),
        (51.1657, 10.4515), (34.6937, 135.5023), (37.7749, -122.4194), (31.7683, 35.2137), (35.6762, 139.6503)]

    return create_heatmap(response)

STATISTICS_FUNCTIONS = {
    "get_most_deadly": get_most_deadly,
    "average_casualties": average_casualties,
    "get_top_5_most_num_spread": get_top_5_most_num_spread,
    "get_most_group_active_by_region": get_most_group_active_by_region,
    "get_history_events_by_year": get_history_events_by_year,
}
