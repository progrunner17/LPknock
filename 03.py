str ="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list(map((lambda x:print(len([i for i in x if( i != ',' and i != '.')]))),str.split(" ")))
