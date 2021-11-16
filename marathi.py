import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'ma'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)


def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateBody():
    audio = AudioSegment.from_mp3('marathi.mp3')

    # 1-Krupaya laksha dya
    start = 12700
    finish = 13900
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_marathi.mp3", format="mp3")

    # 2-Train no and name

    # 3-Thodya velat platform kramank
    start = 12900
    finish = 23200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_marathi.mp3", format="mp3")

    # 4-platform no.

    # 5-var yet ahe
    start = 23800
    finish = 25000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_marathi.mp3", format="mp3")


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2-Train no and name
        textToSpeech(item['train_no'] + " " +
                     item['train_name'], '2_marathi.mp3')
        # 4-platform no.
        textToSpeech(item['platform'], '4_marathi.mp3')

        audios = [f"{i}_marathi.mp3" for i in range(1, 6)]

        announcement = mergeAudios(audios)
        announcement.export(
            f"mar_announce_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Body...")
    generateBody()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
