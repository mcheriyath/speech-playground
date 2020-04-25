import speech_recognition as sr

#the following name is only used as an example
mic_name = "USB Device 0x46d:0x825: Audio (hw:2,0)"
#Sample rate is how often values are recorded
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data)
#here.
#it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048


#generate a list of all audio cards/microphones
mic_list = sr.Microphone.list_microphone_names()
print(mic_list)
#the following loop aims to set the device ID of the mic that
#we specifically want to use to avoid ambiguity.
for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i


print("Device ID: ", i)
r = sr.Recognizer()
with sr.Microphone(device_index = device_id, sample_rate = sample_rate,
                        chunk_size = chunk_size) as source:
    print("Please wait. Calibrating microphone...")
    # listen for 5 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=5)
    print("Say something!")
    audio = r.listen(source)

    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said '" + r.recognize_sphinx(audio,language='en-US') + "'")
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
