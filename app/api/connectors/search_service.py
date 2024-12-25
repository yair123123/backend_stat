import requests

path_search="http://127.0.0.1:5000/api/search"

def search_in_text(filter):
    query_select = filter.get('queriesSelect')
    text = filter.get('input-text')
    start_date = filter.get('start-input-date')
    end_date = filter.get('end-input-date')

    response = requests.get(url = f"{path_search}/{query_select}/{text}?start={start_date}&end={end_date}")