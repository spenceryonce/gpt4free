import quora

models = {
    'sage'   : 'capybara',
    'gpt-4'  : 'beaver',
    'claude-v1.2'         : 'a2_2',
    'claude-instant-v1.0' : 'a2',
    'gpt-3.5-turbo'       : 'chinchilla'
}

# create account
# make sure to set enable_bot_creation to True
token = quora.Account.create(logging = True, enable_bot_creation=True)

model = quora.Model.create(
    token = token,
    model = 'gpt-3.5-turbo', # or claude-instant-v1.0
    system_prompt = 'you are ChatGPT a large language model ...' 
)

print(model.name)
# # streaming response
# for response in quora.StreamingCompletion.create(
#     custom_model = 'sage',
#     prompt       ='hello, who are you?',
#     token        = token):
    
#     print(response.completion.choices[0].text)