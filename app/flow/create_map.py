import folium
from folium import plugins

corr = [(32.0853, 34.7818), (40.7306, -73.9352), (48.8566, 2.3522), (35.6895, 139.6917), (55.7558, 37.6176),
        (51.1657, 10.4515), (34.6937, 135.5023), (37.7749, -122.4194), (31.7683, 35.2137), (35.6762, 139.6503)]

def create_heatmap(corr):
        m = folium.Map(location=[0, 0], zoom_start=2)
        heat_map = plugins.HeatMap(corr)
        m.add_child(heat_map)

        return m.get_root().render()

create_heatmap(corr)