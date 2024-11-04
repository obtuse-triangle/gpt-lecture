import openai
from config import TOKEN
import urllib


def get_image(topic: str, mood: str):
  client = openai.OpenAI(api_key=TOKEN)
  prompt = f"{topic}에 맞는 그림을 {mood}한 느낌으로 생성해줘"
  response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1
  )
  print(response)
  image_url = response.data[0].url
  urllib.request.urlretrieve(image_url, f"{mood}한 {topic}.jpg")

  return image_url
