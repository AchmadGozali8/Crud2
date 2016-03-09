import datetime
from flask import Flask,render_template,redirect,request
from db import db
from models import Barang,Expaire

app = Flask(__name__)
app.config.from_object("config")
db.init_app(app)

@app.route("/data")
def alldata():
	barang = Barang.query.all()
	
	return render_template("alldata.html",**locals())

@app.route("/data/<int:id>")
def byid(id):
	barang = Barang.query.get(id)
	
	return render_template("byid.html",**locals())

@app.route("/data/add", methods=["POST","GET"])
def add():
	if request.method == "POST":
		nama_barang = request.form.get("nama_barang",None)
		harga = request.form.get("harga",None)
		tahun_expaire = request.form.get("tahun_expaire",None)

		data = Barang(nama_barang,harga,tahun_expaire)
		data.update_harga= datetime.datetime.now()
	
		db.session.add(data)
		db.session.commit()
		return redirect("/data")
	return render_template("add.html",**locals())

@app.route("/data/update/<int:id>",methods=['POST','GET'])
def update(id):
	if request.method=='POST':
		harga_baru = request.form.get("harga",None)
		barang = Barang.query.get(id)
		barang.harga = harga_baru

		db.session.add(barang)
		db.session.commit()
		return redirect("/data") 

	barang = Barang.query.get(id)
	return render_template("update.html",**locals())

@app.route("/data/delete/<int:id>",methods=['POST','GET'])
def delete(id):
	barang = Barang.query.get(id)
	db.session.delete(barang)
	db.session.commit()
	return redirect("/data")
if __name__=="__main__":
	app.run()
