from flask import Flask, jsonify, render_template, request
import time
import numpy as np
app = Flask(__name__)
mem=[]
priority=[]

@app.route('/_add_numbers')
def add_numbers():
    a1 = request.args.get('a1', 0, type=int)
    a2 = request.args.get('a2', 0, type=int)
    a3 = request.args.get('a3', 0, type=int)
    b1 = request.args.get('b1', 0, type=int)
    b2 = request.args.get('b2', 0, type=int)
    b3 = request.args.get('b3', 0, type=int)
    c1 = request.args.get('c1', 0, type=int)
    c2 = request.args.get('c2', 0, type=int)
    c3 = request.args.get('c3', 0, type=int)
    d1 = request.args.get('d1', 0, type=int)
    d2 = request.args.get('d2', 0, type=int)
    d3 = request.args.get('d3', 0, type=int)
    e = request.args.get('e', 0, type=int)
    f = request.args.get('f', 0, type=int)
    ####################
    a1 = int(a1)
    b1 = int(b1)
    c1 = int(c1)
    d1 = int(d1)
    ###################
    a2 = int(a2)
    b2 = int(b2)
    c2 = int(c2)
    d2 = int(d2)
    ###################
    a3 = int(a3)
    b3 = int(b3)
    c3 = int(c3)
    d3 = int(d3)

    ###################
    e = int(e)
    f = int(f) 
    ##################


    if((int(f)%4)==1):
        print("----")
        print(f)
        print("----")
        i = f - 1
        mem.clear()
        l1 = a1 + (a2 * 2) + (a3 * 3)
        l2 = b1 + (b2 * 2) + (b3 * 3)
        l3 = c1 + (c2 * 2) + (c3 * 3)
        l4 = d1 + (d2 * 2) + (d3 * 3)
        q = [l1,l2,l3,l4]
        for x in range(0,4):
            priority.append(0)
        maximum = max(q)
        lane = q.index(maximum)
        mem.append(lane)
        time = maximum * 2.5

        if (time<10):
            time = 10
            rem = 0
        elif (time>60):
            time = 60
            rem = maximum - (60/2.5)
        else:
            rem = 0
        for j in range(0,4):
            priority[j] = priority[j] + 1
        priority[lane] = 0
        print (mem)
        

        print("Lane chosen : ",(lane+1))
        print("Count before signal : ",maximum)
        print("Count after signal : ",rem)
        print("Timer length : ",time)
        if(lane == 0):
        	return jsonify({"a" : lane+1 , "b" : a1+a2+a3 , "c" : rem , "d" : time,"e" : e,"f" : f})
        if(lane == 1):
        	return jsonify({"a" : lane+1 , "b" : b1+b2+b3 , "c" : rem , "d" : time,"e" : e,"f" : f})
        if(lane == 2):
        	return jsonify({"a" : lane+1 , "b" : c1+c2+c3 , "c" : rem , "d" : time,"e" : e,"f" : f})
        if(lane == 3):
        	return jsonify({"a" : lane+1 , "b" : d1+d2+d3 , "c" : rem , "d" : time,"e" : e,"f" : f})			

        # return jsonify({"a" : lane+1 , "b" : maximum , "c" : rem , "d" : time,"e" : e,"f" : f})
    if((int(f)%4)==2) or ((int(f)%4)==3) or ((int(f)%4)==0):
        print("###")
        print(f)
        print("###")
        i = f - 1
        l1 = a1 + (a2 * 2) + (a3 * 3)
        l2 = b1 + (b2 * 2) + (b3 * 3)
        l3 = c1 + (c2 * 2) + (c3 * 3)
        l4 = d1 + (d2 * 2) + (d3 * 3)
        print(*mem)
        q = [l1,l2,l3,l4]
        maximum = -1
        for j in range(0, 4):
            if j in mem:
                continue
            else:
                if q[j]>maximum:
                    maximum = q[j]
                    lane = j
        
        time = maximum * 2.5
        mem.append(lane)
        if (time<10):
            time = 10
            rem = 0
        elif (time>60):
            time = 60
            rem = maximum - (60/2.5)
        else:
            rem = 0
            
        for j in range(0,4):
            priority[j] = priority[j] + 1
        priority[lane] = 0
        
        if(i%4 == 3):
            priority[i] = 0

        print("Lane chosen : ",(lane+1))
        print("Count before signal : ",maximum)
        print("Count after signal : ",rem)
        print("Timer length : ",time)
        if(lane == 0):
        	return jsonify({"a" : lane+1 , "b" : a1+a2+a3 , "c" : rem , "d" : time,"e" : e,"f" : f})
        if(lane == 1):
        	return jsonify({"a" : lane+1 , "b" : b1+b2+b3 , "c" : rem , "d" : time,"e" : e,"f" : f})
        if(lane == 2):
        	return jsonify({"a" : lane+1 , "b" : c1+c2+c3 , "c" : rem , "d" : time,"e" : e,"f" : f})
        if(lane == 3):
        	return jsonify({"a" : lane+1 , "b" : d1+d2+d3 , "c" : rem , "d" : time,"e" : e,"f" : f})	
        # return jsonify({"a" : lane+1 , "b" : maximum , "c" : rem , "d" : time,"e" : e,"f" : f})        


    # return jsonify({"a" : lane , "b" : maximum , "c" : rem , "d" : time})
    # f = f + 1
    #return jsonify({"a1" : a1 , "b1" : b1 , "c1" : c1 , "d1" : d1,"a2" : a2 , "b2" : b2 , "c2" : c2 , "d2" : d2,"a3" : a3 , "b3" : b3 , "c3" : c3 , "d3" : d3,"e" : e,"f" : f})

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=2000)