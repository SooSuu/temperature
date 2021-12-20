from flask import Flask, render_template, request, Response
from camera_pi import Camera
import sqlite3

app = Flask(__name__)

def getData():
	conn=sqlite3.connect('../sensorsData.db')
	curs=conn.cursor()
	for row in curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		temp = row[1]
		hum = row[2]
	conn.close()
	temp = int(temp)
	hum = int(hum)
	return time, temp, hum
	
	
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')	


@app.route("/") 
def index():	
	time, temp, hum = getData()
	templateData = {
		'time': time,
		'temp': temp,
		'hum': hum
	}
	return render_template('index.html', **templateData)
	
	
@app.route("/alarm")
def alarm():
	return render_template('alarm.html')


@app.route("/alarm2", methods=['GET','POST'])
def alarm2():
	if request.method == 'POST':
		result = request.form
		MAX = int(result['MAX'])
		MIN = int(result['MIN'])
		time, temp, hum = getData()
		templateData = {
			'time': time,
			'temp': temp,
			'hum': hum,
			'MAX': MAX,
			'MIN': MIN
			}
	return render_template('alarm2.html', **templateData)


@app.route("/graph")
def graph():
    return render_template("graph.html")


@app.route("/camera")
def camera():
    return render_template("camera.html")


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/info")
def info():
    return render_template("info.html")
    

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
