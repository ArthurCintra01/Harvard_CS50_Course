#lista de dicionarios
people = [
    {"name":"Harry" , "house" : "Gryffindor"},
    {"name":"Cho" , "house" : "Ravenclaw"},
    {"name":"Draco" , "house" : "Slytherin"},
]

#usando uma funcao lambda (funcao de uma linha) como key para a funcao sort
people.sort(key=lambda person: person["name"])