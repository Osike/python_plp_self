import random 
def joke ():
   kicheko = [
      "Why do programmers prefer dark mode ?\n Because light attracts bugs!",
      "Mbona uliacah kazi ?\n sababu sina kazi",
      "atih zake zimeshika \n na hana grasp",
      "alipigwa ngumi\n kufinya mapua macho ikafura",
      "atih mimi skuli omena \n ame tapika fulu",
      
   ]
   #randomly selects a joke 
   kicheko = random.choice(kicheko)
   return kicheko
if __name__ == "__main__":
   print ("Here's a joke for you :\n")
   print(joke())
   
