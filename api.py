import flask
from flask import request, jsonify
import newrelic.agent # Importing New Relic Agent

#comment it
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create a dictionary to keep the data 
members = [
    {
        'id': 0,
        'name': 'Erkin',
        'title': 'Dad',
    },
    {
        'id': 1,
        'name': 'Zerrin',
        'title': 'Mom',
    },
    {
        'id': 2,
        'name': 'Deniz',
        'title': 'Kido',
    },
]


@app.route('/', methods=['GET'])
def home():
    return "This is a test API"

@app.route('/api/v1/family/all', methods=['GET'])
def api_all():
    return jsonify(members)

@app.route('/api/v1/family', methods=['GET'])
def api_id():
    if 'id' in request.args: # request.args returns a dictionary
        id = int(request.args['id'])
        print(request.args)
        print(request.args['id'])
        newrelic.agent.add_custom_parameter('member_id', id) # Sending id as a New Relic attribute called member_id. 
    else:
        return "Error. Type correctly."
    
    results =[]

    for member in members:
        if member['id'] == id:
            results.append(member)

    return jsonify(results)


app.run()
