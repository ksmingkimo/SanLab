from PIL import Image
from pip._vendor.distlib.compat import raw_input

a1 = ("a1 Go to the start of the Labyrinth", "You're at the start of the labyrinth") #Start
a2 = ("a2 Go Left", "You've chosen to go left, unfortunatly it leads to nothing.") #Fail route
a3 = ("a3 Go Right", "You've chosen to go right.") #Right route
a4 = ("a4 Go Left", "You've chosen to go left") #Fail route
a5 = ("a5 Go Right", "You've chosen to go right") #Right route
a6 = ("a6 Go Right", "You've chosen to go right") #Fail route; end
a7 = ("a7 Go Left", "You've chosen to go left") #Fail route
a8 = ("a8 Go Left", "You've chosen to go left") #Fail route; end
a9 = ("a9 Go Right", "You've chosen to go right") #Fail route; end
a10 = ("a10 Go Forwards", "You've chosen to go forwards") #Right route
a11 = ("a11 Go left", "You've chosen to go left; Congratulations, you won! You may restart") #Right route; end; victory
fail = ("fail End game", "You lost!") #End game
b1 = ("b1 Go Left", "You've chosen to go left")
b2 = ("b2 Go Right", "You've chosen to go right")
b3 = ("b3 Go Left", "You've chosen to go left")

transitions = {
    a1: (a2, a3),
    a2: (fail, a1),
    a3: (b1,),
    b1: (a4, a5,),
    a4: (b2,),
    b2: (a7, a6,),
    a5: (b3,),
    b3: (a9, a10,),
    a6: (fail, a1),
    a7: (a8,),
    a8: (fail, a1),
    a9: (fail, a1),
    a10: (a11,),
    a11: (a1,)
}

location = a1

while True:
    print( location[1])
    print ("Here you can: ")

    for (i, t) in enumerate(transitions[location]):
        print(i + 1, t[0])

    choice = int(raw_input("Choose one "))
    location = transitions[location][choice - 1]

    if location == a2:
        img = Image.open('photo\\picture.jpg')
        img.show()