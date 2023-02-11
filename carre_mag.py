class CarreMagique:
    def __init__(self, carre_magique: list[int]):
        self.carre_magique = carre_magique
        self._affichage_carre()
        self._check_carre_magique()

    def _affichage_carre(self):
        print("Votre carre magique:")
        for i in range(0, len(self.carre_magique), len(self.carre_magique)//3):
            for j in range(i, i+3):
                print(self.carre_magique[j], end=" ")
            print()

    def _check_horizontale(self):
        somme = 0
        stock_somme = sum([self.carre_magique[i]
                          for i in range(len(self.carre_magique)//3)])
        for i in range(3, len(self.carre_magique), len(self.carre_magique) // 3):
            for j in range(i, i+3):
                somme += self.carre_magique[j]
            if somme != stock_somme:
                return -1
            stock_somme = somme
            somme = 0
        return stock_somme

    def _check_verticale(self):
        somme = 0
        stock_somme = sum([self.carre_magique[i]
                          for i in range(0, len(self.carre_magique), len(self.carre_magique)//3)])
        for i in range(1, len(self.carre_magique)//3):
            for j in range(i, len(self.carre_magique), len(self.carre_magique)//3):
                somme += self.carre_magique[j]
            if somme != stock_somme:
                return -1
            stock_somme = somme
            somme = 0
        return stock_somme

    def _check_diagonale(self):
        cpt = 0
        sommeN = 0
        sommeI = 0
        for i in range(0, len(self.carre_magique), (len(self.carre_magique)//3)):
            sommeN += self.carre_magique[i+cpt]
            cpt += 1
        for i in range(len(self.carre_magique), 0, -(len(self.carre_magique)//3)):
            sommeI += self.carre_magique[i-cpt]
            cpt -= 1
        if sommeN == sommeI:
            return sommeN
        else:
            return -1

    def _check_carre_magique(self):
        Horizontale_somme = self._check_horizontale()
        Verticale_somme = self._check_verticale()
        Diagonale_somme = self._check_diagonale()
        if Horizontale_somme == Verticale_somme == Diagonale_somme:
            print("C'est un carre magique avec une constante magique de = {}\n".format(
                  Horizontale_somme))
        else:
            print("Ce n'est pas un carre magique\n")
