import pytest
from app import app
from flask import request
import json

#def test_first():
#	assert to_test() == "good test"


#needs restructuring
db_address_answer = [{u'addresstype': 1, u'countrycode': 143, u'seqno': 283, u'municipality': None,
 u'postalcity': u'Nacka', u'address': u'Alpstigen 3', u'postalcode': u'131 54', u'userseqno': 14882},
{u'addresstype': 1, u'countrycode': 143, u'seqno': 285, u'municipality': None, u'postalcity': u'Malm\xf6',
  u'address': u'Fastighetsgatan 6', u'postalcode': u'30238', u'userseqno': 14905},
{u'addresstype': 1, u'countrycode': 143, u'seqno': 286, u'municipality': None, u'postalcity': u'New York', 
 u'address': u'Oxford Street', u'postalcode': u'201 01', u'userseqno': 14904},
{u'addresstype': 1, u'countrycode': 143, u'seqno': 287, u'municipality': None, u'postalcity': u'G\xf6teborg',
 u'address': u'Brogatan 1', u'postalcode': u'500 00', u'userseqno': 14909},
{u'addresstype': 1, u'countrycode': 143, u'seqno': 288, u'municipality': None, 
u'postalcity': u'G\xf6teborg', u'address': u'Kungsgatan 3', u'postalcode': u'600 00', u'userseqno': 14908},
{u'addresstype': 1, u'countrycode': 143, u'seqno': 284, u'municipality': None, u'postalcity': u'Bor\xe5s',
 u'address': u'All\xe9gatan 63', u'postalcode': u'503 37', u'userseqno': 14907},
{u'addresstype': 1, u'countrycode': 143, u'seqno': 289, u'municipality': None, u'postalcity': u'H\xf6kerum',
 u'address': u'Vings Torp', u'postalcode': u'523 98', u'userseqno': 14906},
{u'addresstype': 1, u'countrycode': None, u'seqno': 281, u'municipality': None, u'postalcity': None,
 u'address': u'Kungsgatan 3', u'postalcode': None, u'userseqno': 66},
{u'addresstype': 1, u'countrycode': 143, u'seqno': 294, u'municipality': None, u'postalcity': u'Stockholm',
 u'address': u'Storgatan 1', u'postalcode': u'123 45', u'userseqno': 14967}, 
{u'addresstype': 1, u'countrycode': 143, u'seqno': 279, u'municipality': None, u'postalcity': u'Nacka',
 u'address': u'Ekbacken 3', u'postalcode': u'121 23', u'userseqno': 14881}, 
{u'addresstype': 1, u'countrycode': 143, u'seqno': 293, u'municipality': None, u'postalcity': u'Nacka',
 u'address': u'Klyvarev\xe4gen 36', u'postalcode': u'131 42 ', u'userseqno': 174}, 
{u'addresstype': 1, u'countrycode': 129, u'seqno': 297, u'municipality': None, u'postalcity': u'Kiev',
 u'address': u'Vul. Shcherbakova 61-B, kv.77', u'postalcode': u'04128', u'userseqno': 15027}, 
{u'addresstype': 1, u'countrycode': 180, u'seqno': 299, u'municipality': None, u'postalcity': u'123456',
 u'address': u'Canada lane, 25', u'postalcode': u'12541', u'userseqno': 15089},
{u'addresstype': 1, u'countrycode': 147, u'seqno': 292, u'municipality': None, u'postalcity': u'Kiev',
  u'address': u'Mira str,26b', u'postalcode': u'02230', u'userseqno': 205},
{u'addresstype': 1, u'countrycode': 143, u'seqno': 2, u'municipality': u'G\xf6teborg',
 u'postalcity': u'Torslanda ', u'address': u'Meridianv\xe4gen 6, test', u'postalcode': u'4233899',
  u'userseqno': 0}]



def test_doc():
	with app.test_client() as c:
		rv = c.get('/?tequila=42')
		assert request.args['tequila'] == '42'


# def test_get_address():
# 	response = app.test_client().get("/address")
#	assert request.args[""]==db_address_answer

def test_get_address():
	with app.test_client() as c:
		response = c.get('/address')
		assert json.loads(response.data) == db_address_answer

def test_get_id():
	with app.test_client() as c:
		response = c.get('/67')
		assert json.loads(response.data) == db_address_answer

def test_get_address_id():
	with app.test_client() as c:
		response = c.get('/address/67')
		assert json.loads(response.data) == db_address_answer

def test_delete_address_without_id():
	with app.test_client() as c:
		response = c.delete("/address")
		print "in delete", response
		assert response.status_code == 500

def test_delete_address_id():
	with app.test_client() as c:
		response = c.delete("/address/14882")
		print "in delete", response.data
		assert response.data == '"Item was deleted"\n'

def test_delete_id():
	with app.test_client() as c:
		response = c.delete("/14882")
		print "in delete", response.data
		assert response.data == '"Item was deleted"\n'

def test_post_address_id():
	with app.test_client() as c:
		response = c.post("/address/14882", {},{"id":14882})
		print "in post", json.loads(response.data)
		real_data = {u'addresstype': 1, u'countrycode': 143, u'seqno': 283, u'municipality': None,
		u'postalcity': u'Nacka', u'address': u'Alpstigen 3', u'postalcode': u'131 54', u'userseqno': 14882}

		assert json.loads(response.data) == real_data

def test_posts_id():
	with app.test_client() as c:
		response = c.post("/14882", {},{"id":14882})
		print "in post", json.loads(response.data)
		real_data = {u'addresstype': 1, u'countrycode': 143, u'seqno': 283, u'municipality': None,
		u'postalcity': u'Nacka', u'address': u'Alpstigen 3', u'postalcode': u'131 54', u'userseqno': 14882}
		assert json.loads(response.data) == real_data

def test_put_address_id():
	put_data = {u'addresstype': 1, u'countrycode': 153, u'municipality': None,
		u'postalcity': None, u'address': u'Alpstigen 35', u'postalcode': u'178 54', u'userseqno': 14856}
	print "in put"
	with app.test_client() as c:
		response = c.put("/address/14856", data = json.dumps(put_data))
		assert json.loads(response.data) =="some problems" #because of that trigger insert errors

def test_put_address():
	put_data = {u'addresstype': 1, u'countrycode': 153, u'municipality': None,
		u'postalcity': None, u'address': u'Alpstigen 35', u'postalcode': u'178 54', u'userseqno': 14856}
	print "in put"
	with app.test_client() as c:
		response = c.put("/address", data = json.dumps(put_data))
		assert json.loads(response.data) =="some problems" #because of that trigger insert errors