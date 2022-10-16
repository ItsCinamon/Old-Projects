
from random import choice


# Input Genre
print("What genre would you like?  (RomCom, Action, Dark, Slice of Life)")
genre_input = input()


# Pick the genre and print the animes on the genre

romcom = ["Fruit Basket","Lovely Complex", "Love is War", "Blue Spring Ride"]
action = ["Demon Slayer", "Kakegurui", "Beyond the Boundery"]
dark = ["Another"]
slice_of_life = []

if genre_input == ("RomCom"):
    print("This is the list of RomCom animes: ", romcom)
    genre = romcom

if genre_input == ("Action"):
    print("This is the list of Action animes: ", action)
    genre = action

if genre_input == ("Dark"):
    print("This is the list of Dark animes: ", dark)
    genre = dark

if genre_input == ("Slice of Life"):
    print("This is the list of Slice of Life animes: ", slice_of_life)
    genre = slice_of_life

    


# Randomize the genre
print("Do you want to randomize the list and get an anime? (Y/N)")
randomize_it = input()

if randomize_it == ("Y"):
    print("This is your recommended Anime: ", (choice(genre)))

if randomize_it == ("N"):
    print("Ok bye!")

input()
