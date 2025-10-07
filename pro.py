
import random
import json



from nltk.chat.util import Chat, reflections
intents = json.loads(open('intents.json').read())






def get_response(intents_list,intents_json):
    tag= intents_list[0]['intent']
    list_of_intents =intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

print("|============= Welcome to College Equiry Chatbot System! =============|")
print("|============================== Feel Free ============================|")
print("|================================== To ===============================|")
print("|=============== Ask your any query about our college ================|")
while True:
    message = input("| You: ")
    if message == "bye" or message == "Goodbye":
        #ints = predict_class(message)
        res = get_response( intents)
        print("| Bot:", res)
        print("|===================== The Program End here! =====================|")
        exit()

    else:
       # ints = predict_class(message)
        res = get_response( intents)
        print("| Bot:", res)