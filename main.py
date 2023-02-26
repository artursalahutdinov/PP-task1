from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Conversation, ConversationalPipeline
import os

tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")
nlp = ConversationalPipeline(model=model, tokenizer=tokenizer)

conversation = Conversation()

clear = lambda: os.system('cls')

clear()

print("Type some text to start conversation...")

while True:
    text = input()

    conversation.add_user_input(text)

    result = nlp([conversation], do_sample=False, max_length=1000)

    clear()

    for is_user, text in result.iter_texts():
        print(text)


    
