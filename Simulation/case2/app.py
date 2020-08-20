from flask import Flask, jsonify, render_template, request
import time
import numpy as np
app = Flask(__name__)
mem=[]
priority=[]

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    c = request.args.get('c', 0, type=int)
    d = request.args.get('d', 0, type=int)
    e = request.args.get('e', 0, type=int)
    f = request.args.get('f', 0, type=int)
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f) 
    # if(int(f)%4)==1 and f!=1:
    # 	mem = []

    if((int(f)%4)==1):
        print("----")
        print(f)
        print("----")
        i = f - 1
        mem.clear()
        l1 = a
        l2 = b
        l3 = c
        l4 = d
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
        return jsonify({"a" : lane+1 , "b" : maximum , "c" : rem , "d" : time,"e" : e,"f" : f,"g" : b})
    if((int(f)%4)==2) or ((int(f)%4)==3) or ((int(f)%4)==0):
        print("###")
        print(f)
        print("###")
        if (int(f)%4)==0:
            g = b
        else :
            g = 0    
        i = f - 1
        l1 = a
        l2 = b
        l3 = c
        l4 = d
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
        return jsonify({"a" : lane+1 , "b" : maximum , "c" : rem , "d" : time,"e" : e,"f" : f,"g" : g})        


    # return jsonify({"a" : lane , "b" : maximum , "c" : rem , "d" : time})
    # f = f + 1
    # return jsonify({"a" : a , "b" : b , "c" : c , "d" : d,"e" : e,"f" : f})

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=7555)
    
