import ollama

localModel = 'phi3:mini'
output = ollama.generate(model=localModel, prompt='capitale de la France ?')
response = output['response'];

print(response)

