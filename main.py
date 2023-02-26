from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Conversation, ConversationalPipeline
from flask import Flask
from flask import request, jsonify
from flask import send_from_directory

tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")
nlp = ConversationalPipeline(model=model, tokenizer=tokenizer)

app = Flask(__name__)

conversation = Conversation()

@app.route('/')
def index():
    return send_from_directory('public', "index.html")

@app.route('/message', methods = ['POST'])
def sendMessage():
    message = request.json['message']
    
    conversation.add_user_input(message)
    
    result = nlp([conversation], do_sample=False, max_length=1000)
    
    messages = []

    for is_user, text in result.iter_texts():
        messages.append({
            'is_user': is_user,
            'text': text
        })

    return jsonify({
        'uuid': result.uuid,
        'messages': messages
    })

@app.route('/reset', methods = ['GET'])
def reset():
    global conversation

    conversation = Conversation()
    
    return 'ok'

    
@app.route('/<path:path>')
def send_report(path):
    return send_from_directory('public', path)