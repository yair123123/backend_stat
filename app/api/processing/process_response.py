from typing import Dict, List

import folium
from flask import render_template
from folium import plugins


def dict_to_html(data, level=0):
    html = ""
    for key, value in data.items():
        if isinstance(value, dict):
            html += f"{'&nbsp;' * (level * 4)}<b>{key}:</b><br>{dict_to_html(value, level + 1)}"
        elif isinstance(value, list):
            html += f"{'&nbsp;' * (level * 4)}<b>{key}:</b> {', '.join(map(str, value))}<br>"
        else:
            html += f"{'&nbsp;' * (level * 4)}<b>{key}:</b> {value}<br>"
    return html
def create_map(events:List[Dict[str,Dict[str,float]]]):
    map = folium.Map(location=[32.1, 34.8], zoom_start=6)
    for event in events:
        folium.Marker([event["location"]["latitude"], event["location"]["longitude"]],
                      popup=dict_to_html(event)).add_to(map)
    return map._repr_html_()
def create_map_for_casualties_by_area(data):
    map = folium.Map(location=[32.1, 34.8], zoom_start=6)

    locations = data['res']

    for location in locations:
        if location['average_casualties'] > 0.5:
            color = "red"
        elif location['average_casualties'] < 0.3:
            color = "green"
        else:
            color = "blue"
        icon = folium.Icon(color=color)

        folium.Marker([location["latitude"], location["longitude"]],
                      popup=f"<b>{location['_id']['region']}</b><br>{location['average_casualties']}",
                      icon=icon).add_to(map)

    return map._repr_html_()


def create_map_for_most_groups_active_by_region(data):
    map = folium.Map(location=[32.1, 34.8], zoom_start=6)
    locations = data['res']

    for location in locations:
        popup_content = "<b>Region:</b> " + location['_id'] + "<br><b>Groups:</b><br>"

        for group in location['top_groups']:
            popup_content += f"<b>{group['group']}</b>: {group['total_casualties']} casualties<br>"

        folium.Marker([location["latitude"], location["longitude"]],
                      popup=popup_content).add_to(map)
    return map._repr_html_()


def create_map_for_groups_with_common_goal(data):
    map = folium.Map(location=[32.1, 34.8], zoom_start=6)
    locations = data['res']

    for location in locations:
        popup_content = "<br><b>Groups:</b><br>"

        for group in location['groups']:
            popup_content += f"<b>{group}</b>"

        folium.Marker([location["location"]['latitude'], location["location"]["longitude"]],
                      popup=popup_content).add_to(map)
    return map._repr_html_()


def create_map_for_groups_unique(data):
    map = folium.Map(location=[32.1, 34.8], zoom_start=6)
    locations = data['res']
    for location in locations:
        popup_content = f"<b>Count {location['count']}</b><br><b>Groups:</b><br>"
        for group in location['groups']:
            popup_content += f"<b>{group}</b>"
        folium.Marker([location["location"]['latitude'], location["location"]["longitude"]],
                      popup=popup_content).add_to(map)
    return map._repr_html_()


def create_map_for_shared_goals_in_groups(data):
    map = folium.Map(location=[32.1, 34.8], zoom_start=6)
    locations = data['res']
    for location in locations:
        popup_content = f"<b>Count {location['groups_count']}</b><br><b>Target type: {location['target_type']}</b><br><br><b>Groups:</b><br>"
        for group in location['groups']:
            popup_content += f"<b>{group}</b>"
        folium.Marker([location["location"]['location']['latitude'], location["location"]['location']["longitude"]],
                      popup=popup_content).add_to(map)
    return map._repr_html_()


from folium import Map, Marker, Popup, Icon
from folium.plugins import MarkerCluster


def create_map_for_shared_attack_type_in_groups(data):
    map = Map(location=[32.1, 34.8], zoom_start=6, tiles='CartoDB positron')
    marker_cluster = MarkerCluster().add_to(map)

    locations = data['res']
    for location in locations:
        color = 'green' if location['count'] < 10 else 'orange' if location['count'] < 20 else 'red'

        popup_content = f"""
        <div style="font-family: Arial; font-size: 14px; line-height: 1.5;">
            <b>Attack Type:</b> {location['type']}<br>
            <b>Count:</b> {location['count']}<br>
            <b>Location:</b> ({location['location']['latitude']}, {location['location']['longitude']})
        </div>
        """
        popup = Popup(popup_content, max_width=250)

        Marker(
            location=[location['location']['latitude'], location['location']['longitude']],
            popup=popup,
            icon=Icon(color=color, icon='info-sign')
        ).add_to(marker_cluster)

    return map._repr_html_()


def create_heatmap(corr):
    m = folium.Map(location=[0, 0], zoom_start=2)
    heat_map = plugins.HeatMap(corr)
    m.add_child(heat_map)

    return m._repr_html_()

def create_table(template_name,data):
        return render_template(template_name, data=data.get("res",[]))