import requests

print("Geometry Dash Song Location Finder - By: Sevenworks\n")
print("Examples: 509397 (--Spiders--) = RobTop, 1 (Chilled 1) = Newgrounds.\n\n")
songID = input("Song ID: ")

gdsong = requests.get(f'http://geometrydashcontent.b-cdn.net/songs/{songID}.mp3')

if gdsong.status_code < 400:
    print('The song does exist on RobTops Song Server')
else:
    print('Newgrounds or Nonexistant Song.')
