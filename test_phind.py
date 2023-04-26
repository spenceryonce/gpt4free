import phind
#works
# set cf_clearance cookie
phind.cf_clearance = 'heguhSRBB9d0sjLvGbQECS8b80m2BQ31xEmk9ChshKI-1682268995-0-160'
phind.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'

prompt = 'Generate github readme documentation for the code'

#open code txt file
with open('code.txt', 'r') as file:
    code = file.read()

while True:
    prompt = input("You: ")
    print("Bot: ", end='', flush=True)
    for result in phind.StreamingCompletion.create(
        model  = 'gpt-3.5',
        prompt = prompt,
        results     = phind.Search.create(prompt, actualSearch = True), # create search (set actualSearch to False to disable internet)
        creative    = False,
        detailed    = False,
        codeContext = ''):  # up to 3000 chars of code

        print(result.completion.choices[0].text, end='', flush=True)