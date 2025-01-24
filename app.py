from flask import Flask, render_template, jsonify, make_response

app = Flask(__name__)

# Global state variable
current_state = "normal"


# Initialize state during app startup
def initialize_state():
    global current_state
    current_state = "normal"
    print("Initial state set to 'normal'.")


@app.route("/")
def home():
    return render_template("home.html")  # Serve the home.html template


@app.route("/get_state")
def get_state():
    # Disable caching to ensure fresh values
    response = make_response(jsonify({"state": current_state}))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    return response


@app.route("/start_attack")
def start_attack():
    global current_state
    current_state = "attack"  # Change state to 'attack'
    print(f"State changed to: {current_state}")  # Debugging log
    return jsonify({"success": True, "message": "Attack state activated."})


@app.route("/stop_attack")
def stop_attack():
    global current_state
    current_state = "normal"  # Reset state to 'normal'
    print(f"State changed to: {current_state}")  # Debugging log
    return jsonify({"success": True, "message": "Attack state stopped."})


@app.route("/set_state/<state>")
def set_state(state):
    global current_state
    if state in ["normal", "attack"]:
        current_state = state
        return jsonify({"success": True, "state": current_state})
    return jsonify({"success": False, "message": "Invalid state provided."}), 400


if __name__ == "__main__":
    # Call `initialize_state` once during app startup
    initialize_state()
    app.run(debug=True)