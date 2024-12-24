import folium
from flask import render_template
from folium import plugins


def create_heatmap(corr):
        m = folium.Map(location=[0, 0], zoom_start=2)
        heat_map = plugins.HeatMap(corr)
        m.add_child(heat_map)

        return m._repr_html_()

def create_map(events):
        print(events)

def create_table(template_name,data):
        print(1)
        return render_template(template_name, data=data.get("res",[]))