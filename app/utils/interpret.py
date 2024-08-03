'''
    Code explainer using GROQ API
'''
import os

from groq import Groq
from dotenv import load_dotenv


def explain_code(code: str) -> str | None:
    '''
        Code explainer function
    '''
    load_dotenv()
    client = Groq(api_key=os.environ["GROQ_USER_API"])
    answer = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Retrun just yes or no if {code} is a sql code."
            }
        ],
        model="llama3-8b-8192",
    )
    return answer.choices[0].message.content
