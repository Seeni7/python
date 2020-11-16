



try:

    scrabble =  open('sowpods.txt', 'r')
    words = scrabble.read()
    print(words)
except Exception as err:
    print("There is a problem to access the file")
    print(err)

    scrabble.close()
    


