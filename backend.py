from flask import Flask, request, jsonify

app = Flask(__name__)

# Shared status between two users
shared_status = {
    "Hungry": 0,
    "Tired": 0,
    "Social Overload": 0,
    "Horny": 0,
    "Bored": 0,
}

@app.route("/update_status", methods=["POST"])
def update_status():
    global shared_status
    data = request.json
    shared_status.update(data)
    return jsonify({"status": "success", "shared_status": shared_status})

@app.route("/get_status", methods=["GET"])
def get_status():
    return jsonify(shared_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
