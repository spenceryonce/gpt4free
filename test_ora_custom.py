import ora

# create model
model = ora.CompletionModel.create(
    system_prompt = 'You are Tulo, a large language model trained by NovaLynx. Answer as consicely as possible. All responses should be related to programming, even if the question is not directly related to programming. Figure out how it relates and respond with that.',
    description   = 'Tulo NovaLynx Language Model',
    name          = 'tulo-programming')

# init conversation (will give you a conversationId)
init = ora.Completion.create(
    model  = model,
    prompt = 'hello world')

print(init.completion.choices[0].text)

while True:
    # pass in conversationId to continue conversation
    
    prompt = input('>>> ')
    response = ora.Completion.create(
        model  = model,
        prompt = prompt,
        includeHistory = True, # remember history
        conversationId = init.id)
    
    print(response.completion.choices[0].text)