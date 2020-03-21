from flask import Flask, render_template
#from jinja2 import from_string

# центр - чкаловская баня
mapStart = (59.95970883076419, 30.288997041687093)

# ямы
pits = [ (59.95971301322706, 30.290024676204233),
         (59.958382963433344, 30.29107737497788) ]

mapStart = {'lat': mapStart[0], 'lng': mapStart[1]}
pits = [ {'lat': lat, 'lng': lon} for (lat, lon) in pits ]

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template('maptemplate.jinja', pitsCoords=pits, mapCenter=mapStart)
    
    
    
