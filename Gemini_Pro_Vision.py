import os
import google.generativeai as genai
import PIL.Image

os.environ['GOOGLE_API_KEY'] = "YOUR_GOOGLE_API_KEY"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])


#Generate Story from an Image

image = PIL.Image.open('random.jpg')
vision_model = genai.GenerativeModel('gemini-pro-vision')
response = vision_model.generate_content(["Write a 100 words story from the Picture",image])


print(response.text)

'''
Output:
For image 'random.jpg'

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
Output :
For image 'items.webp'

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

#Describe an Image

image = PIL.Image.open('random2.jpg')

response = vision_model.generate_content(["Describe the image in a single sentence?",image])

print(response.text)

'''
Output:
For image 'random2.jpg'
 A female swimmer wearing a black cap and blue swimsuit is swimming the freestyle stroke in a blue pool.
'''

#Compare Two Images

image1=PIL.Image.open('random2.jpg')
image2=PIL.Image.open('random3.jpg')

response=vision_model.generate_content(["what are the differences between the two images?",image1,image2])

print(response.text)


'''
Output:

The first image is of a woman swimming in a pool. 
The second image is of a street with cars driving on it.  
The first image is in color, while the second image is in black and white. 
The first image is taken from a low angle, while the second image is taken from a high angle. 
The first image is focused on the woman, while the second image is focused on the cars. 
The first image is about a person enjoying themselves, while the second image is about the hustle and bustle of city life.

'''