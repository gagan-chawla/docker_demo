import json
from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_HOST'] = 'database'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'demo'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
api = Api(app)
cors = CORS(app)

# API
class User(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("Select * FROM user")
        results = cur.fetchall()
        return results

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()
        results = {}
        with open('logs/users.txt',  'a') as file:
            file.write(json.dumps(args))
            file.write('\n')
        username = args['username']
        password = args['password']
        cur = mysql.connection.cursor()
        cur.execute(f"INSERT INTO user (username, password) VALUES ('{username}', '{password}')")
        mysql.connection.commit()
        
        # cur.execute("Select * FROM user")
        # results = cur.fetchall()
        return results, 200
        # return "Done", 200


# Route
api.add_resource(User, '/')

# Running server
if __name__ == '__main__':
     app.run(host="0.0.0.0", port='5000', debug=True)
