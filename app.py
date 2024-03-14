
import random
import requests
from flask import Flask,request,jsonify
app=Flask(__name__)
def mm(nam):
	ayt = random.randint(1, nam)
	return ayt
@app.route('/')
def abdo():
	number = random.randint(1, 114)
	url =f'https://unpkg.com/quran-json@1.0.1/json/surahs/{number}.pretty.json'
	res=requests.get(url).json()
	ayt=res['total_verses']
	ay=mm(ayt)-1
	ay_1=ay+1
	try:
		try:
			
			aya_oll=res['verses'][ay]['text']
			aya=res['verses'][ay_1]['text']
			data={'data':{1:aya_oll,2:aya}}
			return jsonify(data)
		except:
			data={'data':'error'}
			return jsonify(data)
	except:pass

if __name__ =='__main__':
	app.run(host='0.0.0.0',port=8080)


