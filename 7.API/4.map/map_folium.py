from flask import Flask, render_template, request
import folium

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def map_view():
    latitude, longitude = 37.5198, 126.9406  # Default to 63 Building
    if request.method == 'POST':
        latitude = float(request.form.get('latitude', latitude))
        longitude = float(request.form.get('longitude', longitude))

    # Create folium map
    folium_map = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([latitude, longitude], popup='Location').add_to(folium_map)

    # Render map to HTML
    map_html = folium_map._repr_html_()
    return render_template('map.html', latitude=latitude, longitude=longitude, map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)
