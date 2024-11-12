import ollama


localModel = 'phi3:mini'
conversation = []

while True:
    prompt = input('USER: \n')
    conversation.append({'role': 'user', 'content': prompt})
    output = ollama.chat(model=localModel, messages=conversation)
    response = output['message']['content']
    print(response)
    conversation.append({'role': 'assistant', 'content': response})

