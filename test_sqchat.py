import sqlchat

messages = []

while True:
    user = input('you: ')

    sqlchat_cmpl = sqlchat.Completion.create(
        prompt   = user,
        messages = messages
    )

    print('gpt:', sqlchat_cmpl.completion.choices[0].text)
    
    messages.extend([
        {'role': 'user', 'content': user }, 
        {'role': 'assistant', 'content': sqlchat_cmpl.completion.choices[0].text}
    ])

    # for response in sqlchat.StreamCompletion.create(
    #     prompt   = 'write python code to reverse a string',
    #     messages = []):

    #     print(response.completion.choices[0].text)