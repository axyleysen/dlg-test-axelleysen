from flask import Flask, jsonify 
app = Flask(__name__)

# Defining route and function for api
@app.route('/total/<string:numbers_to_add>')
def sum_list(numbers_to_add):
	"""Return the sum of a list of numbers.

	Argument -- [String] Comma separated integers
	Response -- [Json]:
	{
		"total": int
	}

	"""

    # Converting api inputs into list
	list_to_add = [int(item) for item in numbers_to_add.split(",")]
	# Return response as json object
	return jsonify({"total": sum(list_to_add)})

# Initialising flask application
if __name__ == '__main__':
	app.run(debug=True)