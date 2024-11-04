import openai
from config import TOKEN


def summarize(text: str):
  client = openai.OpenAI(api_key=TOKEN)
  prompt = f"""
  User의 콘텐츠를 한글로 3줄 요약해줘
  """
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role": "system",
      "content": prompt
    }, {"role": "user", "content": prompt + text}],
  )
  print(response)

  return f"gpt answer : {response.choices[0].message.content}"
