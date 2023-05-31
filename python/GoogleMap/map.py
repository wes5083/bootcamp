import folium


# 创建地图对象
m = folium.Map(location=[40.712776, -74.005974], zoom_start=12)

# 定义搜索和手动定位的JavaScript代码
js_code = '''
<script>
    function searchLocation() {
        var address = document.getElementById('search-box').value;
        var geocoder = new google.maps.Geocoder();
        geocoder.geocode({'address': address}, function(results, status) {
            if (status === 'OK') {
                var lat = results[0].geometry.location.lat();
                var lng = results[0].geometry.location.lng();
                var marker = L.marker([lat, lng]).addTo(m);
                m.panTo([lat, lng]);
            } else {
                alert('Location not found');
            }
        });
    }

    function manualLocation() {
        m.on('click', function(e) {
            var lat = e.latlng.lat;
            var lng = e.latlng.lng;
            var marker = L.marker([lat, lng]).addTo(m);
            m.panTo([lat, lng]);
        });
    }
</script>
'''

# 添加搜索框和手动定位的功能
search_box = '''
<div>
    <input type="text" id="search-box" placeholder="Search location">
    <button onclick="searchLocation()">Search</button>
    <button onclick="manualLocation()">Manual Location</button>
</div>
'''

# 将JavaScript代码和搜索框添加到地图上
folium.Marker(
    location=[40.712776, -74.005974],
    popup=folium.Popup(search_box, max_width=250),
    icon=folium.Icon(icon='info-sign')
).add_to(m)

# 将地图保存为HTML文件
m.save('map.html')


