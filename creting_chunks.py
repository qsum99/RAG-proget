import whisper
import json
import os
modle=whisper.load_model("large-v2")
audios=os.listdir("video_mp3")
for audio in audios:
  number=audio.split(".")[0]
  title=audio.split(".")[1]
  print(number,title)
  result=modle.transcribe(audio=f"video_mp3/{audio}",task="translate",word_timestamps=False)
  chunks=[]
  for segments in result['segments']:
      chunks.append({"number": number, "title":title,'start':segments['start'],'end':segments['end'],'text':segments['text']})
  matadata={"chunks":chunks,"text":result['text']}
  with open(f"jsons/{audio}.josn","w") as f:
      json.dump(matadata,f)