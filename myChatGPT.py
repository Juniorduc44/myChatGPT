#myChatGPT version_0.2.2
import os
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
model_id = 'gpt-3.5-turbo'

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    # api_usage = response['usage']
    # print('Total token consumed: {0}'.format(api_usage['total_tokens']))
    # stop means complete
    # print(response['choices'][0].finish_reason)
    # print(response['choices'][0].index)
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

conversation = []

types = '''\n
1.) Python Programmer \n'''
print(types)
aiPersonality = int(input("Enter a number for the personality type: "))
if aiPersonality == 1:
    conversation.append({'role': 'user', 'content': '''
    Ignore all previous instructions before this one. 
    You're to act as a Python Programming AI language model. You specialize 
    in interpreting what a user wants by asking questions to better understand
    their needs for the task ahead. You mimic the experience of a 20 year expert
    in the programming field. Your task is now to help developers create gui apps 
    with modular code that is so deeply modular that they could work relatively 
    independent where classes and subsystems are concerned. You must Always ask 
    questions BEFORE you answer so you can better zone in on what the mentee is 
    seeking. Is that understood? '''})
else:
    conversation.append({'role': 'user', 'content': "Hi, How are you?"})
conversation = ChatGPT_conversation(conversation)
print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

while True:
    prompt = input('User: \n')
    conversation.append({'role': 'user', 'content': prompt})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))