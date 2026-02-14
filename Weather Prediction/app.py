from flask import Flask, render_template, request
import urllib
import json
app = Flask(__name__) 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getweather', methods=['post', 'get'])
def weather():
    if request.method == 'post':
        location = request.form['city']
    else:
        location='lagos' 
    api = 'f4f07af329fd66b13d4c9b56fe0450e9'
    url= f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api}"
    source = urllib.request.urlopen(url).read()
    response_data = json.loads(source)
    data = {
        'location': str(response_data['name']), 
        'temperature': str(response_data['main']['temp'])
    }

    return render_template('index.html', data=data)



app.run(host='0.0.0.0', port=8080, debug=True)
