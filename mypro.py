from flask import *
import psycopg2
import os
import csv
app=Flask(__name__)
app.secret_key="a"
myconn=psycopg2.connect(
	user="postgres",
	password="sri",
	database="aditya"
	)
@app.route("/")
@app.route("/home")
def home():
	return render_template("homepr.html")
@app.route("/details")
def details():
	return render_template("details.html")
@app.route("/incharge",methods=['GET','POST'])
def incharge():
	if request.method=="POST":
		uname=request.form['uname']
		pwd=request.form['pwd']
		cur=myconn.cursor()
		cur.execute("""select * from logins where uname=%s and pwd=%s""",(uname,pwd))
		data=cur.fetchall()
		if (data):
			session['loggedin']=True
			flash("login succesful")
			return render_template("selectcol.html")
		else:
			flask("incorrect username or password")
	return render_template("incharge.html")
@app.route("/selectcol")
def selectcol():
	return render_template("selectcol.html")
@app.route("/aec",methods=['GET','POST'])
def aec():
	cur=myconn.cursor()
	cur.execute("""select * from aec1""")
	data=cur.fetchall()
	return render_template("aec.html",data=data)
@app.route("/acet",methods=['GET','POST'])
def acet():
	cur=myconn.cursor()
	cur.execute("""select * from acet2""")
	data=cur.fetchall()
	return render_template("acet.html",data=data)
@app.route("/acoe",methods=['GET','POST'])
def acoe():
	cur=myconn.cursor()
	cur.execute("""select * from acoe3""")
	data=cur.fetchall()
	return render_template("acoe.html",data=data)
@app.route("/AEC",methods=['GET','POST'])
def AEC():
	if not session.get('loggedin'):
		return render_template('incharge.html')
	cur=myconn.cursor()
	cur.execute("""select * from aec1""")
	data=cur.fetchall()
	return render_template("aec_in.html",data=data)
@app.route("/ACET",methods=['GET','POST'])
def ACET():
	if not session.get('loggedin'):
		return render_template('incharge.html')
	cur=myconn.cursor()
	cur.execute("""select * from acet2""")
	data=cur.fetchall()
	return render_template("acet_in.html",data=data)
@app.route("/ACOE",methods=['GET','POST'])
def ACOE():
	if not session.get('loggedin'):
		return render_template('incharge.html')
	cur=myconn.cursor()
	cur.execute("""select * from acoe3""")
	data=cur.fetchall()
	return render_template("acoe_in.html",data=data)
@app.route("/delete1",methods=['GET','POST'])
def delete1():
	if not session.get('loggedin'):
		return render_template("incharge.html")
	if request.method=='POST':
		id=request.form['delete1']
		cur=myconn.cursor()
		cur.execute("""delete from aec1 where labno=%s""",(id))
		myconn.commit()
		cu=myconn.cursor()
		cu.execute("""select * from aec1""")
		d1=cu.fetchall()
		return render_template("aec_in.html",data=d1)
@app.route("/delete2",methods=['GET','POST'])
def delete2():
	if not session.get('loggedin'):
		return render_template("incharge.html")
	if request.method=='POST':
		id=request.form['delete2']
		cur=myconn.cursor()
		cur.execute("""delete from acet2 where labno=%s""",(id))
		myconn.commit()
		cu=myconn.cursor()
		cu.execute("""select * from acet2""")
		d1=cu.fetchall()
		return render_template("acet_in.html",data=d1)
@app.route("/delete3",methods=['GET','POST'])
def delete3():
	if not session.get('loggedin'):
		return render_template("incharge.html")
	if request.method=='POST':
		id=request.form['delete3']
		cur=myconn.cursor()
		cur.execute("""delete from acoe3 where labno=%s""",(id))
		myconn.commit()
		cu=myconn.cursor()
		cu.execute("""select * from acoe3""")
		d1=cu.fetchall()
		return render_template("acoe_in.html",data=d1)
@app.route("/edit1",methods=['GET','POST'])
def edit1():
	if not session.get('loggedin'):
		return render_template("incharge.html")
	if request.method=='POST':
		id=request.form['edit1']
		cur=myconn.cursor()
		cur.execute("""select * from aec1 where labno=%s""",(id))
		d1=cur.fetchall()
		return render_template("edit1.html",data=d1)
@app.route("/edit2",methods=['GET','POST'])
def edit2():
	if not session.get('loggedin'):
		return render_template("incharge.html")
	if request.method=='POST':
		id=request.form['edit2']
		cur=myconn.cursor()
		cur.execute("""select * from acet2 where labno=%s""",(id))
		d1=cur.fetchall()
		return render_template("edit2.html",data=d1)
@app.route("/edit3",methods=['GET','POST'])
def edit3():
	if not session.get('loggedin'):
		return render_template("incharge.html")
	if request.method=='POST':
		id=request.form['edit3']
		cur=myconn.cursor()
		cur.execute("""select * from acoe3 where labno=%s""",(id))
		d1=cur.fetchall()
		return render_template("edit3.html",data=d1)
@app.route("/update1",methods=['GET','POST'])
def update1():
    if not session.get('loggedin'):
        return render_template("incharge.html")
    if request.method=="POST":
        #id=request.form['id']
        labno=int(request.form['labno'])
        labname=request.form['labname']
        floorno=int(request.form['floorno'])
        incharge=request.form['incharge']
        technicians=request.form['technicians']
        softwares=request.form['softwares']
        totalsystems=int(request.form['totalsystems'])
        underprob=int(request.form['underprob'])
        mycur=myconn.cursor()
        mycur.execute("""update aec1 set labno=%s,labname=%s,
            floorno=%s,incharge=%s,technicians=%s,softwares=%s,totalsystems=%s,
                underprob=%s where labno=%s""",(labno,labname,floorno,incharge,
                technicians,softwares,totalsystems,underprob,labno))
        myconn.commit()
        cu=myconn.cursor()
        cu.execute("""select * from aec1""")
        data=cu.fetchall()
        
        return render_template("aec_in.html",data=data)
@app.route("/update2",methods=['GET','POST'])
def update2():
    if not session.get('loggedin'):
        return render_template("incharge.html")
    if request.method=="POST":
        #id=request.form['id']
        labno=int(request.form['labno'])
        labname=request.form['labname']
        floorno=int(request.form['floorno'])
        incharge=request.form['incharge']
        technicians=request.form['technicians']
        softwares=request.form['softwares']
        totalsystems=int(request.form['totalsystems'])
        underprob=int(request.form['underprob'])
        mycur=myconn.cursor()
        mycur.execute("""update acet2 set labno=%s,labname=%s,
            floorno=%s,incharge=%s,technicians=%s,softwares=%s,totalsystems=%s,
                underprob=%s where labno=%s""",(labno,labname,floorno,incharge,
                technicians,softwares,totalsystems,underprob,labno))
        myconn.commit()
        cu=myconn.cursor()
        cu.execute("""select * from acet2""")
        data=cu.fetchall()
        
        return render_template("acet_in.html",data=data)
@app.route("/update3",methods=['GET','POST'])
def update3():
    if not session.get('loggedin'):
        return render_template("incharge.html")
    if request.method=="POST":
        #id=request.form['id']
        labno=int(request.form['labno'])
        labname=request.form['labname']
        floorno=int(request.form['floorno'])
        incharge=request.form['incharge']
        technicians=request.form['technicians']
        softwares=request.form['softwares']
        totalsystems=int(request.form['totalsystems'])
        underprob=int(request.form['underprob'])
        mycur=myconn.cursor()
        mycur.execute("""update acoe3 set labno=%s,labname=%s,
            floorno=%s,incharge=%s,technicians=%s,softwares=%s,totalsystems=%s,
                underprob=%s where labno=%s""",(labno,labname,floorno,incharge,
                technicians,softwares,totalsystems,underprob,labno))
        myconn.commit()
        cu=myconn.cursor()
        cu.execute("""select * from acoe3""")
        data=cu.fetchall()
        
        return render_template("acoe_in.html",data=data)

@app.route("/logout")
def logout():
	session['loggedin']=False
	return render_template("homepr.html")
if __name__=="__main__":
	app.run(debug=True)








































































