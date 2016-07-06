from app import app
from flask import render_template, request, redirect, g
from flask_restful import Resource, Api, reqparse
import psycopg2.extras
import json

api = Api(app)

def connect_db():
	conn = psycopg2.connect("""
							dbname='reachmee'
							user='postgres' 
							host='127.0.0.1'
							port='5432' 
							password='uknowW2009'""")
	return conn

parser = reqparse.RequestParser()
parser.add_argument('id', type = int)

@app.before_request
def before_request():
    g.db = connect_db()
    g.cursor = g.db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/<file_name>')
def static_html(file_name):
	return app.send_static_file(file_name)

@app.route('/images/<img_number>')
def send_image(img_number):
	file_name = "images/"+str(img_number)+".png" 
	return app.send_static_file(file_name)

class Address(Resource):
	def get(self):
		#cursor = g.db.cursor()
		g.cursor.execute("SELECT * FROM rm0.address WHERE NOT address = ''")
		address_list = g.cursor.fetchall()
		print "address_list", address_list
		return address_list

	def put(self, addressId = None):
		new_address = json.loads(request.data)
		print "new_address", new_address
		if new_address:
			
			try:
				g.cursor.execute("""INSERT INTO rm0.address (userseqno, addresstype, address, postalcode
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

	def delete(self, addressId):
		address_to_delete = addressId
		#g.cursor.execute("DELETE FROM rm0.address WHERE userseqno=%s" %(address_to_delete))
		print "will be deleted: " + str(address_to_delete)
		return "Item was deleted"

	def post(self):
		args = parser.parse_args()
		address_id = args["id"]
		print "address_id", address_id
		try:

			g.cursor.execute("SELECT * FROM rm0.address WHERE userseqno=%s", (address_id,))
			address = g.cursor.fetchall()[0]
			return address
		except Exception as e:
			print e
			return "Item was returned"

api.add_resource(Address, '/address', '/<int:addressId>', '/address/<int:addressId>')



