from pydub.generators import Sine

tone = Sine(440).to_audio_segment(duration=1000)
tone.export("tone.wav", format="wav")
print("Music generated!")
