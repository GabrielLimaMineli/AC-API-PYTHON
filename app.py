from flask import Flask
import json
app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "name": "Luiz",
        "idade":32
    },
    {
        "id": 2,
        "name": "Glauber",
        "idade": 22
    },
    
]

tasksJSON = json.dumps(tasks)

@app.route('/teste', methods=['GET'])
def hello_world():
    return tasksJSON, 200

if __name__ == '__main__':
    app.run()
