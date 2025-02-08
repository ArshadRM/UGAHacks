from flask import Flask, request, jsonify
from flask_cors import CORS # fix error from reqeusting by requesting CORS
from llm.llm import generate_questions  # Import the generate_questions method
from imggeneration.txttoimg import generate_image # Import the generate_image method

app = Flask(__name__)

#enable CORS for all routes
CORS(app)

#our API endpoint for generating questions
@app.route('/generate-questions', methods=['POST'])
def generate_questions_endpoint():
    try:
        # Get JSON data from the request body
        data = request.get_json()

        # Extract the 'topic' from the data
        topic = data.get('topic', '')

        # Ensure the topic is provided
        if not topic:
            return jsonify({"error": "Topic is required"}), 400

        # Call the generate_questions method with the topic
        question_data = generate_questions(topic)

        # Return the question data as is (Flask will handle converting it to JSON)
        return jsonify(question_data)
    
    except Exception as e:
        print(str(e))
        return jsonify({"error": str(e)}), 500
    
#our API endpoint for generating images from text
@app.route('/generate-image', methods=['POST'])
def generate_image_endpoint():
    try:
        # Get JSON data from the request body
        data = request.get_json()

        # Extract the 'topic' from the data
        topic = data.get('topic', '')

        # Ensure the topic is provided
        if not topic:
            return jsonify({"error": "Topic is required"}), 400

        # Call the generate_images method with the topic
        image_data = generate_image(topic)

        # Return the question data as is (Flask will handle converting it to JSON)
        return jsonify(image_data)
    
    except Exception as e:
        print(str(e))
        return jsonify({"error": str(e)}), 500

#our API endpoint for generating images from text
@app.route('/generate-upgrades', methods=['POST'])
def generate_upgrades_endpoint():
    try:
        # Get JSON data from the request body
        data = request.get_json()

        # Extract the 'topic' from the data
        topic = data.get('topic', '')

        # Ensure the topic is provided
        if not topic:
            return jsonify({"error": "Topic is required"}), 400

        # Call the generate_images method with the topic
        image_data = []

        for i in range(4):
            image_data.append(generate_image(topic))

        # Return the question data as is (Flask will handle converting it to JSON)
        return jsonify(image_data)
    
    except Exception as e:
        print(str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
