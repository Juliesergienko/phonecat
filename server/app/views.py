

from app import app
from flask import render_template, request, redirect
from flask_restful import Resource, Api
#from flask import send_from_directory
import psycopg2
import json

api = Api(app)
##########################################################3
conn = psycopg2.connect("dbname='reachmee' user='postgres' host='127.0.0.1' port='5432' password='uknowW2009'")
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
	print file_name 
	return app.send_static_file(file_name)


class Address(Resource):
	def get(self):
		cursor.execute("SELECT *   FROM rm0.address WHERE NOT address = ''")
		address_list = cursor.fetchall()
		list_to_client = []
		for i in address_list:
			img_url = "/home/julia/D_copy/ReachMee/trunk/phonecat/server/app/static/images/" + str(i[0])
			i += (img_url,)
			list_to_client.append(i)
		print "here"
		print list_to_client
		return list_to_client

	def put(self):
		new_address = json.loads(request.args.get('new_address', ''))
		print "new_address", new_address
		print type(new_address)
		if new_address:
			print "in if"
			print "here"
			
			try:
				#################################################################################3
				cursor.execute("""INSERT INTO rm0.address (userseqno, addresstype, address, postalcode
					,postalcity, municipality) VALUES('%s', '%s', '%s', '%s', '%s', '%s')"""
					%(new_address["userseqno"], new_address["addresstype"], new_address["address"],
					new_address["postalcode"], new_address["postalcity"], new_address["municipality"], 
					))#new_address["countrycode"]
				cursor.commit()
				print "here_0"
				root()
			except:
				print "there"
				return root()

		else:
			print "in else"
			raise Exception("empty value for PUT method")

	def delete(self):
		address_to_delete = request.args.get("id")
		#cursor.execite("DELETE FROM rm0.address WHERE userseqno=%s" %(address_to_delete))
		print "will be deleted: " + address_to_delete
		return root()

	def post(self):
		address_id = request.args.get("id")
		print "address_id", address_id
		try:
			cursor.execute("SELECT * FROM rm0.address WHERE userseqno=%s" %(address_id))
			address = cursor.fetchall()
			return json.dumps(address)
		except:
			return root()

api.add_resource(Address, '/address')

# @app.route('/address', methods = ['DELETE'])
# def delete_address():
	
# @app.route('/address', methods=['GET'])
# def address():


# @app.route('/address', methods = ['PUT'])
# def add_address():
	#print "request", request
	

# @app.route('/address', methods = ['POST'])
# def get_certain_address():
	

