from flask import Flask, render_template_string
#from jinja2 import from_string

app = Flask(__name__)

tmpl = '''    
<html>
	<head>
		<script src="https://js.api.here.com/v3/3.1/mapsjs-core.js"
		type="text/javascript" charset="utf-8"></script>
		<script src="https://js.api.here.com/v3/3.1/mapsjs-service.js"
		type="text/javascript" charset="utf-8"></script>
		<script src="https://js.api.here.com/v3/3.1/mapsjs-mapevents.js"
		type="text/javascript" charset="utf-8"></script>
		<script src="https://js.api.here.com/v3/3.1/mapsjs-ui.js"
		type="text/javascript" charset="utf-8"></script>
        <link rel="stylesheet" type="text/css"
		href="https://js.api.here.com/v3/3.1/mapsjs-ui.css" />
	</head>
	<body>
		<div style="width: 800px; height: 600px" id="mapContainer"></div>
		<script>
			// Initialize the platform object:
			var platform = new H.service.Platform({
				'apikey': 'FE9w9Y4LozwKnt6m_3ceYXZyUV4aphNJo9Snh-sUkr4'
			});
			
			// Obtain the default map types from the platform object
			var maptypes = platform.createDefaultLayers();
			
			// Instantiate (and display) a map object:
			var map = new H.Map(
			document.getElementById('mapContainer'),
			maptypes.vector.normal.map,
			{
				zoom: 12,
				center: { lng: 13.4, lat: 52.51 }
			});
			
			var berlinMarker = new H.map.Marker({
				lat:52.5192,
				lng:13.4061
			});
			map.addObject(berlinMarker);
			var ui = H.ui.UI.createDefault(map, maptypes, 'ru-RU');
			// Create an info bubble object at a specific geographic location:
			var bubble = new H.ui.InfoBubble({ lng: 13.5, lat: 52.61 }, {
                content: '<b>Hello World!</b>'
			});
			
			// Add info bubble to the UI:
			ui.addBubble(bubble);
			// Initialize the map:
			// var map = new H.Map(...);
			
			// Enable the event system on the map instance:
			var mapEvents = new H.mapevents.MapEvents(map);
			
			// Add event listeners:
			map.addEventListener('tap', function(evt) {
				// Log 'tap' and 'mouse' events:
				console.log(evt.type, evt.currentPointer.type);
			});
			map.addEventListener('dbltap', function(evt) {
				console.log(evt.type, evt.currentPointer.type, evt.currentPointer.id);
				//console.log(evt.target);
				//var latt = map.screenToGeo(evt.currentPointer.viewportX, evt.currentPointer.viewportY);
				//var lon = map.screenToGeo(evt.currentPointer.viewportX, evt.currentPointer.viewportY);
				//console.log(latt, lon);
				behavior.disable();
			var bubble = new H.ui.InfoBubble(map.screenToGeo(evt.currentPointer.viewportX, evt.currentPointer.viewportY), {
                content: '<b>You clicked here!</b>'
			});
			ui.addBubble(bubble);
			behavior.enable();
				
			});
			
			// Instantiate the default behavior, providing the mapEvents object:
			var behavior = new H.mapevents.Behavior(mapEvents);
			
			
			
		</script>
	</body>
</html>	
'''

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template_string(tmpl)
    
    
