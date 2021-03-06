from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
    "rangeEnd": "2020-09-06T00:00:00",
    "rangeStart": "2020-09-02T00:00:00",
    "graphs": [
        {
            "formula": "CPULoad5min*10"
        }
    ],
    "df": {
        "CPULoad5min": {
            "index": [
                "2020-09-02T00:01:49",
                "2020-09-02T00:06:37",
                "2020-09-02T00:11:36",
                "2020-09-02T00:16:54",
                "2020-09-02T00:21:35",
                "2020-09-02T00:26:32"
            ],
            "values": [
                123,
                112,
                78,
                111,
                111,
                95
            ]
        }
    }
    }
]


@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)
