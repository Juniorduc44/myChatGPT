#myChatGPT version_0.1.2
import openai
import os
from dotenv import load_dotenv
load_dotenv()

def askGPT(text):
  openai.api_key = os.getenv('OPENAI_API_KEY')
  response = openai.Completion.create(
    model= "gpt-3.5-turbo",
     messages= 'role: user, content: Say this is a test!',
     temperature= 0.7
    )
  return print(response.choices[0].text)
  return print(response.choices[1].text)
  return print(response.choices[2].text)

def main():
  
  while True:
    print('GPT: Ask me a question\n')
    myQn = input()
    askGPT(myQn)
    print('\n')
main()
