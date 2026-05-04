from flask import Flask,jsonify,render_template,request
app=Flask(__name__)
tasks=[]
ctr=[0]
@app.route("/")
def i(): return render_template("index.html")
@app.route("/api/health-data")
def h(): return jsonify({"source":"sample","data":[{"week":"W10","value":2841},{"week":"W09","value":3102},{"week":"W08","value":3380},{"week":"W07","value":3215},{"week":"W06","value":2990},{"week":"W05","value":3450}]})
@app.route("/api/disease-summary")
def d(): return jsonify([{"label":"Flu Cases Tracked","value":"1.2M","trend":"+4.2%","up":True},{"label":"States Reporting","value":"50","trend":"100%","up":True},{"label":"Hospitalizations","value":"84K","trend":"-2.1%","up":False},{"label":"Active Data Feeds","value":"12","trend":"Live","up":True}])
@app.route("/api/tasks",methods=["GET"])
def gt(): return jsonify(tasks)
@app.route("/api/tasks",methods=["POST"])
def ct():
 b=request.get_json();ctr[0]+=1;t={"id":ctr[0],"title":b["title"],"priority":b.get("priority","medium"),"done":False};tasks.append(t);return jsonify(t),201
@app.route("/api/tasks/<int:tid>",methods=["PUT","DELETE"])
def ut(tid):
 global tasks
 if request.method=="DELETE":
  tasks=[t for t in tasks if t["id"]!=tid];return jsonify({"ok":True})
 t=next(x for x in tasks if x["id"]==tid);t.update(request.get_json());return jsonify(t)
app.run(debug=False,port=5001)
