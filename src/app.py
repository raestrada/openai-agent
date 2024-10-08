from flask import Flask, request, jsonify, render_template
from chat import get_thread, create_message

app = Flask(__name__)

thread_id = None

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/start_chat', methods=['POST'])
def start_chat():
    global thread_id
    thread = get_thread()
    thread_id = thread.id
    return jsonify({'success': True, 'thread_id': thread_id})

@app.route('/send_message', methods=['POST'])
def send_message():
    global thread_id
    content = request.json.get('content', '')
    
    if thread_id is None:
        return jsonify({'error': 'No thread started'}), 400

    response = create_message(thread_id, content)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8888)
    print("openai-agent ready")
