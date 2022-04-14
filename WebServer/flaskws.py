import time
from flask import Flask, render_template, request
import roslibpy
import os.path
import os

HTMLFILE = 'test.html'

app = Flask(__name__)

client = roslibpy.Ros(host='localhost', port=9090)

fanDict = {}

def toROS():
	print(fanDict)
	talker = roslibpy.Topic(client, 'fans', 'std_msgs/String')
	for key in fanDict:
		value = fanDict[key]
		print("%s:%s" % (value[0],value[1]))
		talker.publish(roslibpy.Message({'data':"%s:%s" % (value[0],value[1])}))
	talker.unadvertise


def RunFans(form):
	# Takes in a fan id (i.e. fan1) and a fan speed (0-100)
	# Looks up id in config file for i2c addr, and sends i2c addr and speed
	# updates dict with the new speed values

	if 'ALLFANS' in form:
		speed = form.get('ALLFANS')
		if (speed == ''):
			speed = 0
		form.pop('ALLFANS')
		for key in fanDict:
			fanDict[key][1] = speed
	else:
		for key in form:
			if form[key] != '':
				fanDict[key][1] = form[key]


def RunActuators(form):
	print(form)
	
	

def loadFile(fileName):

	if os.path.exists(fileName):
		with open(fileName) as file:
			for line in file:
				print(line)
				line = line.split(",")
				print(line)

				fanDict[line[0]] = [line[1],line[2]]
	else:
		#TODO send error to GUI, 
		print("FILE NO EXIST")
			


def saveFile(fileName):
	if os.path.exists(fileName):
		# TODO send error to GUI, file exist....
		print("FILE EXIST")
	else:
		with open(fileName, 'w') as file:
			for key in fanDict:
				value = fanDict[key]
				file.writelines("%s,%s,%s" % (key, value[0], value[1]))
			file.close()

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
			saveFile(request.form['filename'])
		if request.form.get('loadfile') == 'LOAD CONFIG':
			form.pop('loadfile')
			loadFile(request.form['filename'])
		if request.form.get('toros'):
			toROS()
	elif request.method == 'GET':
		return render_template(HTMLFILE,data=fanDict)
	return render_template(HTMLFILE,data=fanDict)
 

def main():
	print(os.path)
	loadFile("zerofan.txt")
	client.run()
	app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
	main()
