import you
#works
# simple request with links and details
response = you.Completion.create(
    prompt       = "hello world",
    detailed     = True,
    includelinks = True,)

print(response)

chat = []

while True:
    prompt = input("You: ")
    
    response = you.Completion.create(
        prompt  = prompt,
        chat    = chat)
    
    print("Bot:", response["response"])
    
    chat.append({"question": prompt, "answer": response["response"]})