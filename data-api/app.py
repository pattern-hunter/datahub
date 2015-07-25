from bottle import get, post, run, request, response
from pymongo import MongoClient
from bson.objectid import ObjectId

import json

client = MongoClient()
db = client.datahub

@get('/upload')
def login():
    return '''
        <form action="/api/data" method="post" id="data-form">
            <input value="Submit" type="submit" />
        </form>
    
       <textarea name="data" form="data-form" placeholder="Enter text here..."></textarea>
    '''

@post('/api/data')
def upload_data():
    data = request.forms.get('data')

    if data:
        try:
            data = json.loads(data)
            data_id = db.data.insert(data)
            
            response.headers['Location'] = '/api/data/' + str(data_id)
            
            return str(data_id)

        except ValueError:
            response.body = {
                "message" : "Did not provide valid JSON"
            }
    else:
        response.status = 400
        response.body = {
            "message" : "No data provided"
        }

@get('/api/data/<data_id>')
def get_data(data_id):
    data = db.data.find_one({ "_id" : ObjectId(data_id) })

    response.status = 404

    if data:
        response.status = 200
        response.headers['Content-Type'] = 'application/json'

        data['id'] = str(data['_id'])
        del data['_id']

    return data

run(host='0.0.0.0', port=8080, debug=True, reloader=True)
