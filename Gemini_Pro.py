import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "YOUR_GOOGLE_API_KEY"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

from IPython.display import Markdown


#Gemini Pro

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("List 5 planets each with an interesting fact")

print(response.text)

'''
Output:

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
Output:

1. 😭 Face with Tears of Joy
2. 😂 Face with Tears of Joy
3. ❤️ Red Heart
4. 😊 Smiling Face with Smiling Eyes
5. 👍 Thumbs Up
'''

#Chat-Model

chat_model = genai.GenerativeModel('gemini-pro')

chat = chat_model .start_chat(history=[])

response = chat.send_message("Give me a best one line quote with the person name")
print(response.text+'\n')

response = chat.send_message("Who is this person? And where was he/she born?\
 Explain in 2 sentences")
print(response.text)

'''
Output:

"Yesterday is history, tomorrow is a mystery, but today is a gift. That's why it's called the present." - Eleanor Roosevelt
Eleanor Roosevelt was the longest-serving First Lady of the United States, holding the post from 1933 to 1945 during her husband Franklin D. Roosevelt's four terms as President. She was born in New York City on October 11, 1884.
Roosevelt was a tireless advocate for human rights and social justice, and she served as a delegate to the United Nations for many years. She was also a prolific writer and lecturer, and her syndicated newspaper column, "My Day," was read by millions of Americans.
'''

response=model.generate_content('Write a 5 line poem on AI')
print(response.text)

'''
Output: 

Code's guiding hand,
AI's ethereal dance,
Unveiling mysteries,
Expanding realms of thought,
Shaping the future's trance.

'''
