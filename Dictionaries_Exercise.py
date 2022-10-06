
infile = open("book of John text.txt","r")
book = infile.read()
book_list = book.split()

dictionary = {'Father': 0, 'God': 0, 'Christ': 0, 'Spirit': 0, 'spirit': 0, 'life': 0, 'man': 0}

father = book_list.count("Father")
god = book_list.count("God")
christ = book_list.count("Christ")
spirit = book_list.count("Spirit")
Spirit = book_list.count("spirit")
life = book_list.count("life")
man = book_list.count("man")

dictionary["Father"] = father
dictionary["God"] = god
dictionary["Christ"] = christ
dictionary["Spirit"] = spirit
dictionary["spirit"] = Spirit
dictionary["life"] = life
dictionary["man"] = man

for key, value in dictionary.items():
    print(key, ':' , value)



