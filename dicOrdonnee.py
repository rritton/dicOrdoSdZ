class DictionnaireOrdonne:
    """Notre dictionnaire ordonn�. L'ordre des donn�es est maintenu
    et il peut donc, contrairement aux dictionnaires usuels, �tre tri�
    ou voir l'ordre de ses donn�es invers�es"""
    
    def __init__(self, base={}, **donnees):
        """Constructeur de notre objet. Il peut ne prendre aucun param�tre
        (dans ce cas, le dictionnaire sera vide) ou construire un
        dictionnaire remplis gr�ce :
        -   au dictionnaire 'base' pass� en premier param�tre ;
        -   aux valeurs que l'on retrouve dans 'donnees'."""
        
        self._cles = [] # Liste contenant nos cl�s
        self._valeurs = [] # Liste contenant les valeurs correspondant � nos cl�s
        
        # On v�rifie que 'base' est un dictionnaire exploitable
        if type(base) not in (dict, DictionnaireOrdonne):
            raise TypeError( \
                "le type attendu est un dictionnaire (usuel ou ordonne)")
        
        # On r�cup�re les donn�es de 'base'
        for cle in base:
            self[cle] = base[cle]
        
        # On r�cup�re les donn�es de 'donnees'
        for cle in donnees:
            self[cle] = donnees[cle]
    
    def __repr__(self):
        """Repr�sentation de notre objet. C'est cette cha�ne qui sera affich�e
        quand on saisit directement le dictionnaire dans l'interpr�teur, ou en
        utilisant la fonction 'repr'"""
        
        chaine = "{"
        premier_passage = True
        for cle, valeur in self.items():
            if not premier_passage:
                chaine += ", " # On ajoute la virgule comme s�parateur
            else:
                premier_passage = False
            chaine += repr(cle) + ": " + repr(valeur)
        chaine += "}"
        return chaine
    
    def __str__(self):
        """Fonction appel�e quand on souhaite afficher le dictionnaire gr�ce
        � la fonction 'print' ou le convertir en cha�ne gr�ce au constructeur
        'str'. On redirige sur __repr__"""
        
        return repr(self)