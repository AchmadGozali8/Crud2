from db import db

class Barang(db.Model):
	__tablename__="barang"

	id = db.Column(db.Integer,primary_key=True)
	nama_barang = db.Column(db.String(80))
	harga = db.Column(db.String(80))
	tahun_expaire = db.Column(db.Integer,db.ForeignKey("expaire.id"))
	expaire = db.relationship("Expaire",
		  backref = db.backref("expaire",lazy = "dynamic"))
	update_harga=db.Column(db.DateTime)
	
	def __init__(self,nama_barang,harga,tahun_expaire):
		self.nama_barang = nama_barang
		self.harga = harga
		self.tahun_expaire = tahun_expaire
		
	def __repr__(self):
		return "<barang{}>".format(self.barang)

class Expaire(db.Model):
	__tablename__ = "expaire"

	id = db.Column(db.Integer,primary_key=True)
	tahun_expaire = db.Column(db.String(80))
	
	def __init__(self,tahun_expaire):
		self.tahun_expaire = tahun_expaire
	def __repr__ (self):
		return "<Expaire {}>".format(self.Expaire)

