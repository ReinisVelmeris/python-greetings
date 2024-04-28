from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':
    # Default port is 7001 if no argument is provided
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 7001

    # Run the Flask app on the specified port
    app.run(host="0.0.0.0", debug=True, port=port)
