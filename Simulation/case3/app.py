from flask import Flask, jsonify, render_template, request
import time
import numpy as np
app = Flask(__name__)
mem = 0
priority=[]

@app.route('/_add_numbers')
def add_numbers():
	a = request.args.get('a', 0, type=int)
	b = request.args.get('b', 0, type=int)
	c = request.args.get('c', 0, type=int)
	d = request.args.get('d', 0, type=int)
	e = request.args.get('e', 0, type=int)
	f = request.args.get('f', 0, type=int)
	g = request.args.get('g', 0, type=int)
	h = request.args.get('h', 0, type=int)
	l1 = int(a)
	l2 = int(b)
	l3 = int(c)
	l4 = int(d)
	l5 = int(e)
	l6 = int(f)
	g = int(g)
	h = int(h)
	count1 = l1
	count4 = l4
	count2 = l2+l3
	count5 = l5+l6
	global mem
	twoway = max(count2, count5)
	oneway = max(count1, count4)

	if mem == 0:
	    if (oneway > twoway):
	        allow = oneway
	    else:
	        allow = twoway        
	elif(mem == 1):
	    allow = twoway
	else:
	    allow = oneway

	time = allow * 2.5
	if(time<10):
	    time = 10
	elif(time>60):
	    time = 60
	    
	if(allow == oneway):
	   
	    if(mem == 0):
	        mem = 1
	    else:
	        mem = 0
	    time = int(time)      
	    print("Full green allowed : l1, l4")
	    print("Right allowed : l3, l6")
	    print("timer length : ",time, " sec")
	    return jsonify({"a" : 1 ,"b": time, "g":g, "h" : h ,"c1" : a,"c2" : b,"c3" : c,"c4" : d,"c5" : e,"c6" : f})

	    
	else:
	    
	    if(mem == 0):
	        mem = 2
	    else:
	        mem = 0
	    time = int(time)    
	    print("Full green allowed : l5, l2")
	    print("Stright green allowed : l3, l6")
	    print("timer length : ",time, " sec")
	    return jsonify({"a" : 2 ,"b": time,"g":g, "h" : h,"c1" : a,"c2" : b,"c3" : c,"c4" : d,"c5" : e,"c6" : f})




@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=6018)
