

from app import app
from flask import render_template, request, redirect
from flask_restful import Resource, Api
#from flask import send_from_directory
import psycopg2
import json

api = Api(app)
######################################################
conn = psycopg2.connect("""dbname='reachmee'
							 user='postgres' 
							 host='127.0.0.1'
							 port='5432' 
							 password='uknowW2009'""")
cursor = conn.cursor()



@app.route('/')
@app.route('/#')
@app.route('/index.html')
def root():
    return app.send_static_file('index.html')

@app.route('/<file_name>')
def static_html(file_name):
	return app.send_static_file(file_name)

@app.route('/home/julia/D_copy/ReachMee/trunk/phonecat/server/app/static/images/<img_number>')
def send_image(img_number):
	file_name = "images/"+str(img_number)+".png" 
	return app.send_static_file(file_name)


class Address(Resource):
	def get(self):
		cursor.execute("SELECT *   FROM rm0.address WHERE NOT address = ''")
		address_list = cursor.fetchall()
		list_to_client = []
		for i in address_list:
			list_to_client += [{"userseqno":i[0], "addresstype":i[1],
			"address":i[2], "postalcode":i[3], 
			"postalcity":i[4], "municipality":i[5]},]
		print list_to_client
		return list_to_client

	def put(self):
		new_address = json.loads(request.args.get("new_address", " "))
		print "new_address", new_address
		if new_address:
			
			try:
				cursor.execute("""INSERT INTO rm0.address (userseqno, addresstype, address, postalcode
					,postalcity, municipality) VALUES(%(userseqno)s, %(addresstype)s, %(address)s,
					 %(postalcode)s, %(postalcity)s, %(municipality)s)"""
					,new_address)
				cursor.commit()
				return "inserted"
			except Exception as e:
				print e
				return "some problems"

		else:
			raise Exception("empty value for PUT method")

	def delete(self):
		address_to_delete = request.args.get("id")
		#cursor.execite("DELETE FROM rm0.address WHERE userseqno=%s" %(address_to_delete))
		print "will be deleted: " + address_to_delete
		return "Item was deleted"

	def post(self):
		address_id = request.args.get("id")
		print "address_id", address_id
		try:
			cursor.execute("SELECT * FROM rm0.address WHERE userseqno=%s" %(address_id))
			address = cursor.fetchall()
			return address
		except Exception as e:
			print e
			return "Item was returned"

api.add_resource(Address, '/address', '/<addressId>')



