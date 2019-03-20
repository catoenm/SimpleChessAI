
import os

output = open("./datasets/AllGames.pgn", "w+")

for filename in os.listdir("./datasets"):
   if ".pgn" in filename:
       print(filename)
       f = open("./datasets/" + filename)
       output.write(f.read())

output.close()