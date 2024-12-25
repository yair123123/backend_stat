import folium


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


def create_map_for_shared_attack_type_in_groups(data):
    map = folium.Map(location=[32.1, 34.8], zoom_start=6)
    locations = data['res']
    for location in locations:
        popup_content = f"<b>Count {location['count']}</b><br><b>Attack type: {location['type']}</b>"
        folium.Marker([location['location']['latitude'], location['location']["longitude"]],
                      popup=popup_content).add_to(map)
    return map._repr_html_()
