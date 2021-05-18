def generateMadLib(language, aPersonYouKnow, adjective1, adjective2, animal, nonsenseWord, noun1, noun2, firstNumber, secondNumber, pluralNoun, typeOfBird):
    #create a variable that holds the MadLib and insert arguments 
    template = """Hi there, all you """ + adjective1 + """ little boys and girls! This is your
old TV buddy, """ + aPersonYouKnow + """, with another """ + str(firstNumber) + """-hour
program of fun and films and  """ + pluralNoun + """ for all of you. And we
have a lot of great cartoons and videos. We will start with a cartoon
about Mickey """ + animal + """ and Donald """ + typeOfBird + """. Then
we will have a commercial for a new toy called """ + nonsenseWord + """.
It will teach you how to build a """ + noun1 + """ and how to speak """ + language + """ before you even start school. Next, we'll have a
cartoon about Bullwinkle and Rocky, the Flying  """ + noun2 + """. And
after that, """ + str(secondNumber) + """ more """ + adjective2 + """ commercials. Wow!"""
    
    #given credit for Mad Lib
    url = "\nCredits: http://www.redkid.net/cgi-bin/madlibs/introkiddyshow.pl"

    #code that's shown
    print(template)
    print(url)
    
    #input start

language = input("Language: ")
aPersonYouKnow = input("A Person You Know: ")
adjective1 = input("First Adjective: ")
adjective2 = input("Second Adjective: ")
animal = input("Animal: ")
nonsenseWord = input("Nonsense Word: ")
noun1 = input("First Noun: ")
noun2 = input("Second Noun: ")
firstNumber = input("First Number: ")
secondNumber = input("Second Number: ")
pluralNoun = input("Plural Noun: ")
typeOfBird = input("Type of Bird: ")

    #what pops out for Mad Lib 
generateMadLib(language, aPersonYouKnow, adjective1, adjective2, animal, nonsenseWord, noun1, noun2, firstNumber, secondNumber, pluralNoun, typeOfBird)
