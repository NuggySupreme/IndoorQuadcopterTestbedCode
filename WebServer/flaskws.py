import time
from flask import Flask, render_template, request
import roslibpy
import os.path
import os

HTMLFILE = 'test.html'

app = Flask(__name__)

client = roslibpy.Ros(host='localhost', port=9090)

fanDict = {}
actArr = []
dataDict ={}

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
			dataDict[key][1] = speed

	else:
		for key in form:
			if form[key] != '':
				fanDict[key][1] = form[key]
				dataDict[key][1] = form[key]



def setActuators(form):
	print(form)
	dataDict['actuator'] = [form['DIRECTION'],form['ANGLE']]
	print(dataDict['actuator'])

def RunActuators():
	talker = roslibpy.Topic(client, 'actuators', 'std_msgs/String')
	print("%s:%s" % (dataDict['actuator'][0],dataDict['actuator'][1]))
	talker.publish(roslibpy.Message({'data':"%s:%s" % (dataDict['actuator'][0],dataDict['actuator'][1])}))
	talker.unadvertise

	with open('actuator.txt', 'w') as file:
		file.write("actuator,%s,%s" % (dataDict['actuator'][0],dataDict['actuator'][1]))

def loadActuatorFile():
	with open('actuator.txt') as file:
		actuatorArr = file.readline().split(",")

		actArr = actuatorArr
		print(actArr)
		dataDict[actuatorArr[0]] = [actuatorArr[1],actuatorArr[2]]

def loadFile(fileName):

	if os.path.exists(fileName):
		with open(fileName) as file:
			for line in file:
				print(line)
				line = line.split(",")
				print(line)

				fanDict[line[0]] = [line[1],line[2]]
				dataDict[line[0]] = [line[1],line[2]]
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
		print(actArr)
		if form.get('updatefan') == 'UPDATE FANS' or form.get('updatefan') == 'UPDATE ALL FANS':
			form.pop('updatefan')
			RunFans(form)
		if form.get('setfan') == 'SET FANS':
			form.pop('setfan')
			RunFans(form)
		if request.form.get('updateactuator') == 'UPDATE ANGLE':
			if 'DIRECTION' in form:
				form.pop('updateactuator')
				setActuators(form)
		if request.form.get('setactuator') == 'SET ANGLE':
			form.pop('setactuator')
			RunActuators()
		if request.form.get('savefile') == 'SAVE CONFIG':
			form.pop('savefile')
			saveFile(request.form['filename'])
		if request.form.get('loadfile') == 'LOAD CONFIG':
			form.pop('loadfile')
			loadFile(request.form['filename'])
		if request.form.get('toros'):
			toROS()
	elif request.method == 'GET':
		return render_template(HTMLFILE,data=dataDict,actarr=actArr)
	return render_template(HTMLFILE,data=dataDict,actarr=actArr)
 

def main():
	print(os.path)
	loadFile("zerofan.txt")
	loadActuatorFile()
	print(actArr)

	client.run()
	app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
	main()
