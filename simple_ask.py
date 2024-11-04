import openai
from config import TOKEN


def response_gpt(ask: str):
  client = openai.OpenAI(api_key=TOKEN)
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": ask}],
  )
  print(response)

  return f"gpt answer : {response.choices[0].message.content}"
