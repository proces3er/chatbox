
import openai
import os

openai.api_key= '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'
completion = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "please give realstic opinions."},
    {"role": "user", "content": " how do i buy my first home in australia."}
  ]
)

print(completion.choices[0].message.content)

# OPENAI_API_KEY= os.getenv('YidNDNtPDtRHNmQrQXLIT3BlbkFJKyPg6CDzhsFg7h9BpjO2')

# client = OpenAI(
#     api_key= 'YidNDNtPDtRHNmQrQXLIT3BlbkFJKyPg6CDzhsFg7h9BpjO2'
# )

# completion = openai.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)