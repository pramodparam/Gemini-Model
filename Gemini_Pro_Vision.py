import os
import google.generativeai as genai
import PIL.Image

os.environ['GOOGLE_API_KEY'] = "YOUR_GOOGLE_API_KEY"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])


#Generate Story from an Image

image = PIL.Image.open('random.jpg')
vision_model = genai.GenerativeModel('gemini-pro-vision')
response = vision_model.generate_content(["Write a 100 words story from the Picture",image])


# print(response.text)

'''
Result:

Once upon a time, there was a lion who was very thirsty. He went to a well to get a drink, but when he looked down, he saw that the water was very low. He could not reach it.

Just then, a rabbit came hopping by. The lion asked the rabbit to help him get a drink. The rabbit agreed and hopped down into the well. He drank some water and then hopped back out.

The lion was very grateful to the rabbit. He asked the rabbit how he could repay him. The rabbit said that he would like the lion to help him get out of the well. The lion agreed and helped the rabbit get out of the well.     

The lion and the rabbit became good friends. They played together every day. The lion learned that even the smallest creatures can be helpful. The rabbit learned that even the biggest creatures can be kind.


'''

#Generate a JSON Response

image = PIL.Image.open('items.webp')

response = vision_model.generate_content(["generate a json of ingredients \
with their count present on the table",image])

print(response.text)

'''
Result :

json
{
  "ingredients": [
    {
      "name": "avocado",
      "count": 1
    },
    {
      "name": "tomato",
      "count": 9
    },
    {
      "name": "egg",
      "count": 2
    },
    {
      "name": "mushroom",
      "count": 3
    },
    {
      "name": "jalapeno",
      "count": 1
    },
    {
      "name": "spinach",
      "count": 1
    },
    {
      "name": "cilantro",
      "count": 1
    },
    {
      "name": "green onion",
      "count": 1
    }
  ]
}
'''