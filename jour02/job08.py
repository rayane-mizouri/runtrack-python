def produits(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire,fraise et cassis")
    elif type == "legumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legumes" and saison == "ete":
        print("artichaut,aubergine et navet")

produits("fruits","hiver")
produits("fruits","ete")
produits("legumes","hiver")
produits("legumes","ete")