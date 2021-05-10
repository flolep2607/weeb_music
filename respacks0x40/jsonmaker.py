import os
import zipfile
from lxml import etree
parser = etree.XMLParser(recover=True)
import json

arr = os.listdir()
os.system("clear")
DICTS=[]
for FILENAME in arr:
	if not FILENAME.endswith(".zip"):continue
	SIZE=os.path.getsize(FILENAME)
	unzipped_file = zipfile.ZipFile(FILENAME, "r")
	SONGS=[]
	IMAGES=[]
	images_number=0
	songs_number=0
	title=""
	description=""
	for file in unzipped_file.filelist:
		if file.filename.endswith(".xml"):
			#print(file.filename)
			parsed=etree.fromstring(unzipped_file.read(file.filename),parser)
			if parsed.cssselect("name"):
				title=parsed.cssselect("name")[0].text
			if parsed.cssselect("title") and title=="":
				title=parsed.cssselect("title")[0].text
			if parsed.find("description"):
				description=parsed.find("description").text
		for extension in ["png","jpg"]:
			if file.filename.endswith("."+extension):
				images_number+=1
				IMAGES.append(file.filename.replace(".png","").replace(".jpg",""))
		for extension in ["ogg","mp3"]:
			if file.filename.endswith("."+extension):
				songs_number+=1
				SONGS.append(file.filename.replace(".ogg","").replace(".mp3",""))
	if title=="":title=FILENAME.replace("zip","")
	DICTS.append({
        "url": "https://music.weeb.flolep.fr/respacks0x40/%s"%FILENAME,
        "link": "https://music.weeb.flolep.fr",
        "name": title,
        "author": "Flo",
        "images": IMAGES,
        "songs": SONGS,
        "imagecount": images_number,
        "songcount": songs_number,
        "size": SIZE,
        "description": description
    })

with open("output.json","w") as FILE:
	json.dump(DICTS,FILE)