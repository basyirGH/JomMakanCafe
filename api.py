#Author: MOHAMAD BASYIR BIN ZAINUDDIN 
#This is the main server execution file

import flask
from flask import request, jsonify, render_template
from datetime import datetime, date


app = flask.Flask(__name__)
app.config["DEBUG"] = True

tableinfo = [  {
    "drink": "",
    "food": "", 
    "status": "Available", 
    "table": "A", 
    "time": ""
  }, 
  {
    "drink": "",
    "food": "", 
    "status": "Available", 
    "table": "B", 
    "time": ""
  }, 
  {
    "drink": "",
    "food": "", 
    "status": "Available", 
    "table": "C", 
    "time": ""
  }, 
  {
    "drink": "",
    "food": "", 
    "status": "Available", 
    "table": "D", 
    "time": ""
  }, 
  {
    "drink": "",
    "food": "", 
    "status": "Available", 
    "table": "E", 
    "time": ""
  }, 
  {
    "drink": "",
    "food": "", 
    "status": "Available", 
    "table": "F", 
    "time": ""
  }
]

food=[
	{"name":"Cheesy-O-Burger Meal"},
	{"name":"Hotouch Burger Meal"},
	{"name":"Lucky Plate Meal"},
	{"name":"Chick-A-Licious with Black pepper Sauce"},
	{"name":"Chick-A-Licious with Mushroom Sauce"},
	{"name":"Double Chicken Delight:"},
	{"name":"Fish N Chips Meals"},
	{"name":"JomMakan Nasi Kandar"},
	{"name":"JomMakan Nasi Ayam"},
	{"name":"BuburAyam Meal"},
	{"name":"BuburPedasMeal"},
	{"name":"Nasi Kari Kapitan"},
	{"name":"Fish Fillet Burger Meal"},
	{"name":"Tower Burger Meal"}
]

drink=[
	{"name":"Coca-Cola"},
	{"name":"FantaStrawberry"},
	{"name":"FantaGrape"},
	{"name":"Minute Maid Fresh Orange"},
	{"name":"Heaven and Earth Iced Lemon"},
	{"name":"NescafeTarik"},
	{"name":"TeaTarik"},
	{"name":"Milo"},
	{"name":"NescafeIce"},
	{"name":"TeaIce"},
	{"name":"Milo Ice"}
]

@app.route('/', methods=['GET'])
def home():
	return "JomMakan Cafe"

@app.route('/api/v1/resources/jommakan/tables/all', methods=['GET'])
def api_alltables():
	return jsonify(tableinfo)

@app.route('/api/v1/resources/jommakan/tables/all/page', methods=['GET'])
def api_alltablespage():
	return render_template("cafedashboard3.html")
	
	
@app.route('/api/v1/resources/jommakan', methods=['GET'])
def api_table():
	if 'name' in request.args:
		name = str(request.args['name'])
	else:
		return "Error: No table name provided. Please specify which table. (A/B/C etc)"

	results = []

	for table in tableinfo:
		if table['table'] == name:
			results.append(table)


	return jsonify(results)

@app.route('/api/v1/resources/jommakan/menu/food', methods=['GET'])
def api_menufood():
	return jsonify(food)

@app.route('/api/v1/resources/jommakan/makeorder/page', methods=['GET'])
def api_menufoodpage():
	return render_template("makeorder.html")

@app.route('/api/v1/resources/jommakan/menu/drink', methods=['GET'])
def api_menudrink():
	return jsonify(drink)

@app.route('/post_makeorder_form', methods=['POST'])
def process_makeorder_form():
	order = request.form 
	now = datetime.now()
	currenttime = now.strftime("%H:%M")
	today = date.today()
	d = today.strftime("%d/%m/%Y")

	for table in tableinfo:
		for key in table:
			if (order['ordertable'] == table[key]):
				
				table.update(
					drink = order['orderdrink'],
					food = order['orderfood'],
					table = order['ordertable'],
					status = 'Ordered',
					time = d + '/' + currenttime
					)
				
				return flask.redirect('/orderconfirmed/page?table='+order['ordertable'])
			else:
				continue 
	
@app.route('/api/v1/resources/jommakan/changestatus/tables/page', methods=['GET'])
def api_changestatus():
	return render_template("changestatus.html")

@app.route('/post_changestatus', methods=['POST'])
def process_changestatus():
	tablestatus = request.form

	for table in tableinfo:
		for key in table:
			if (tablestatus['chosentable'] == table[key]):
				
				table.update(
					status = tablestatus['chosenstatus']
					)
				
				return flask.redirect('/api/v1/resources/jommakan/changestatus/tables/page')
			else:
				continue
@app.route('/orderconfirmed/page', methods=['GET'])
def orderconfirmed():
	return render_template("orderconfirmed.html")

app.run(host='192.168.100.60', debug=True)

