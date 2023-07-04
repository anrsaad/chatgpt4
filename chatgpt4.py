# be sure to download the code from : https://github.com/anrsaad

import openai

# Set up OpenAI API credentials
openai.api_key = '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'  # Replace with your OpenAI API key

def search(query):
    # Define your search prompt
    prompt = f"Search: {query}\nResponse:"

    # Generate response using ChatGPT-4
    response = openai.Completion.create(
        engine='text-davinci-003',  # Replace with the appropriate ChatGPT-4 engine
        prompt=prompt,
        max_tokens=50,  # Set the desired response length
        n=1,  # Set the number of responses to generate
        stop=None,  # Set a stop sequence if needed
    )

    reply = response.choices[0].text.strip()
    return reply

# Example usage
while True:
    user_query = input("Enter your search query: ")
    search_result = search(user_query)
    print(search_result)
    if user_query == "kick me out" :
        break
