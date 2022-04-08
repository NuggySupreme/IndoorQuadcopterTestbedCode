import time
from defer import return_value
from flask import Flask, render_template, request
import roslibpy

HTMLFILE = 'test.html'

app = Flask(__name__)

client = roslibpy.Ros(host='localhost', port=9090)

def toROS(topic, msg):
	talker = roslibpy.Topic(client, topic, 'std_msgs/String')
	talker.publish(roslibpy.Message({'data':msg}))
	talker.unadvertise

def RunFans(form):
	# Takes in a fan id (i.e. fan1) and a fan speed (0-100)
	# Looks up id in config file for i2c addr, and sends i2c addr and speed
	# Sends as an string 'i2c:speed'
	print(form)

	if 'ALLFANS' in form:
		speed = form.get('ALLFANS')
		form.pop('ALLFANS')
		for i in range(1,17):
			toROS('fans', "fan%d:%s" % (i,speed))

	for key in form:
		i2c = key	# TODO look up i2c addr in file
		toROS('fans', ("%s:%s" % (i2c, form.get(key))))

def RunActuators(form):

	toROS('actuators', form.get('DIRECTION'))
	toROS('actuators', form.get('ANGLE'))
	

def loadFile(form):
	print("loadFile")
	print(form)


def saveFile(form):
	print("saveFile")
	print(form)

@app.route("/", methods=['GET','POST'])
def index():
	if request.method == 'POST':
		form = dict(request.form) # takes inmutalbe dict to a mutalbe one so we can pop unwanted items out the form
		if form.get('updatefan') == 'RUN FANS':
			form.pop('updatefan')
			RunFans(form)
		if request.form.get('updateactuator') == 'RUN ANGLE':
			form.pop('updateactuator')
			RunActuators(form)
		if request.form.get('savefile') == 'SAVE CONFIG':
			form.pop('savefile')
			saveFile(request.form)
		if request.form.get('loadfile') == 'LOAD CONFIG':
			form.pop('loadfile')
			loadFile(request.form)
	elif request.method == 'GET':
		return render_template(HTMLFILE, form=request.form)
	return render_template(HTMLFILE)
 

def main():
	
	client.run()
	app.run(host='0.0.0.0', port=8080)
	

if __name__ == "__main__":
	main()
