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
                "content": f"""
                {code}
                If the above code is an SQL code, than return the explanation
                of what each command is doing in the
                model: COMMAND NAME: WHAT IT DOES IN CODE.
                Else, just
                return as an answer:
                'This is not a SQL code.
                Please provide the SQL code you'd like me to analyze, and I'll
                be happy to help!' and just this, no other information.
                """
            },
        ],
        model="llama3-8b-8192",
    )
    return answer.choices[0].message.content
