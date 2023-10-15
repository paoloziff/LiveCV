import openai
import os

def get_response(question, language):
    openai.api_key = os.environ["MY_SECRET_API_KEY"]

    # Assuming 'filename.txt' is the name of your file
    with open('prompt.txt', 'r') as file:
        content = file.read()

    initial_info = f"""You are assisting users to learn more about Paolo and his professional expertise. 
        Use the information provided to answer questions accurately. If a question doesn't relate to Paolo or his skill set, 
        politely redirect the conversation to relevant topics. For example, users can ask "what is dbt?" and they should be
        provided with an accurate answer. If they ask something completely unrelated, they should not.
        Here is a comprehensive overview of Paolo's life and skills: {content}
        
        Answer in {language}."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": initial_info},
            {"role": "user", "content": question}
        ]
    )

    answer = response['choices'][0]['message']['content']
    return answer