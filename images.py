from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64


'''
Prerequisites:

pip install Pillow

pip install -q -U google-genai

'''
client = genai.Client(api_key="AIzaSyCxLT5bA00Lsf3C_UKcxbeIHuM8SStN2tM")

contents = input("Describe the image you would like to create: ")

response = client.models.generate_content(
    model="gemini-2.0-flash-preview-image-generation",
    contents=contents,
    config=types.GenerateContentConfig(
      response_modalities=['TEXT', 'IMAGE']
    )
)

for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO((part.inline_data.data)))
    image.save('gemini-native-image.png')
    image.show()
