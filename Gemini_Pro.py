import os
import google.generativeai as genai
import PIL.Image

os.environ['GOOGLE_API_KEY'] = "YOUR_GOOGLE_API_KEY"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

from IPython.display import Markdown


#Gemini Pro

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("List 5 planets each with an interesting fact")

# print(response.text)

'''
Result:

**1. Mercury**
* While it's the smallest planet in our solar system, it has the second-largest iron core, giving it a higher density than any other planet.

**2. Venus**
* Known as Earth's "twin" due to its similar size and composition, Venus has a thick, carbon dioxide atmosphere that traps heat, making it the hottest planet in the solar system.

**3. Earth**
* The only known planet in the universe to support life, Earth has a unique combination of liquid water, a breathable atmosphere, and plate tectonics that have shaped its surface and environment.

**4. Mars**
* Often called the "Red Planet" due to its iron oxide-rich surface, Mars had a thicker atmosphere and liquid water in the past, suggesting the possibility of past or present life.

**5. Saturn**
* Known for its iconic ring system made of ice particles and dust, Saturn's rings span over 282,000 kilometers in diameter and are visible from Earth with even small telescopes.

'''
''' -----------------------------------------------2---------------------------------------------'''
response = model.generate_content("what are top 5 frequently used emojis?")
print(response.text)

'''
Result:

1. 😭 Face with Tears of Joy
2. 😂 Face with Tears of Joy
3. ❤️ Red Heart
4. 😊 Smiling Face with Smiling Eyes
5. 👍 Thumbs Up
'''

