 fruits = DictionnaireOrdonne()
 fruits
 fruits["pomme"] = 52
 fruits["poire"] = 34
 fruits["prune"] = 128
 fruits["melon"] = 15
 fruits
 fruits.sort()
 print(fruits)
 legumes = DictionnaireOrdonne(carotte = 26, haricot = 48)
 print(legumes)
 len(legumes)
 legumes.reverse()
 fruits = fruits + legumes
 fruits
 del fruits['haricot']
 'haricot' in fruits
 legumes['haricot']
 for cle in legumes:
     print(cle)

 legumes.keys()
 legumes.values()
 for nom, qtt in legumes.items():
     print("{0} ({1})".format(nom, qtt))
