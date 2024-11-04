import openai
from config import TOKEN


def refrigeratorSummarize(text: str):
  client = openai.OpenAI(api_key=TOKEN)
  prompt = f"""
  다음 User의 냉장고 사용 현황을 요약해 3줄 분량으로 정리해줘.
  """
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role": "system",
      "content": prompt
    }, {
      "role": "user",
      "content": text
    }
    ],
  )
  print(response)

  return f"gpt answer : {response.choices[0].message.content}"


if __name__ == "__main__":
  csv = """
사진, 품목이름, 입고일자, 수량
AppleImage.jpg, 사과, 2022-01-01, 5
BananaImage.jpg, 바나나, 2022-01-01, 3
CarrotImage.jpg, 당근, 2022-01-01, 2
"""
  data = refrigeratorSummarize(csv)
  print(data)

# 사용자의 냉장고에는 2022년 1월 1일에 사과 5개, 바나나 3개, 당근 2개가 있습니다. 냉장고에는 총 10개의 과일과 채소가 보관 중이며, 사과가 가장 많이 보관되어 있습니다. 과일과 채소가 각각 5가지 품목씩 보관 중이며, 다양한 식재료를 활용할 수 있을 것으로 보입니다.
