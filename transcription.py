import speech_recognition as speech_recog

def speech():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        print("Nagrywanie dźwięków tła...")
        recog.adjust_for_ambient_noise(audio_file)
        print("Nagrywanie głosu...")
        audio = recog.listen(audio_file)
        print("Transkrypcja...")

        try:
            return recog.recognize_google(audio, language="pl-PL")
        except:
            print("Wystąpił błąd podczas transkrypcji")
