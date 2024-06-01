import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
'''jljjfdkd
f,ldlkmdmd,,dlkjmdjm
dnnmdkkd'''

# List available voices
for voice in voices:
    print(f"Voice ID: {voice.id}, Name: {voice.name}")

# Find the voice with the name "Zira"
zira_voice = next((voice for voice in voices if "Zira" in voice.name), None)

    # if zira_voice:
    #     engine.setProperty('voice', zira_voice.id)
    #     print("Zira voice selected.")
    # else:
    #     print("Zira voice not found.")

answer = input("What do you want me to say? ")
engine.say(answer)
engine.runAndWait()
