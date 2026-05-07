from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.errors import PyMongoError
import os

app = Flask(__name__)
CORS(app)

# MongoDB URI from environment variable only
#MONGO_URI = os.environ.get("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["flask_assignment"]
##collection = db["docker_submissions"]

#@app.route("/submit", methods=["POST"])
#def submit():
#    data = request.get_json()
 #   name    = data.get("name", "").strip()
  #  email   = data.get("email", "").strip()
   # message = data.get("message", "").strip()

    #if not name or not email or not message:
     #   return jsonify({"status": "error", "message": "All fields are required."}), 400

    #try:
     #   collection.insert_one({"name": name, "email": email, "message": message})
      #  return jsonify({"status": "success", "message": "Data submitted successfully!"}), 200
    #except PyMongoError as e:
     #   return jsonify({"status": "error", "message": f"Database error: {str(e)}"}), 500

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()

    if not name or not email or not message:
        return jsonify({
            "status": "error",
            "message": "All fields are required."
        }), 400

    return jsonify({
        "status": "success",
        "message": f"Data received from {name}"
    }), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Flask backend is running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
