
class JogoDaVelha():
    def __init__(self):
        self.tab = {str(i):" " for i in range(9)}
        self.ids = ["X","O"]
        self.isid = 0
        
    def tabuleiro(self):
        j=0
        print("")
        for i in range(3):
            print(" %s | %s | %s " % (self.tab[str(j+0)],self.tab[str(j+1)],self.tab[str(j+2)]))
            if i<2:
                print("___________")
            j+=3
        print("")
    
    def jogada(self,pos,id):
        if self.tab[str(pos)]!=" ":
            print("Posição já ocupada!")
            return False
        else:
            self.tab[str(pos)]=id
            return True
    
    def checkGame(self):
        if(self.tab['0']==self.tab['1']==self.tab['2']!=" "):
            print("Jogador vencedor: %s"%self.tab['0'])
            return True
        elif(self.tab['0']==self.tab['3']==self.tab['6']!=" "):
            print("Jogador vencedor: %s"%self.tab['0'])
            return True
        elif(self.tab['0']==self.tab['4']==self.tab['8']!=" "):
            print("Jogador vencedor: %s"%self.tab['0'])
            return True
        elif(self.tab['1']==self.tab['4']==self.tab['7']!=" "):
            print("Jogador vencedor: %s"%self.tab['1'])
            return True
        elif(self.tab['2']==self.tab['5']==self.tab['8']!=" "):
            print("Jogador vencedor: %s"%self.tab['2'])
            return True
        elif(self.tab['2']==self.tab['4']==self.tab['6']!=" "):
            print("Jogador vencedor: %s"%self.tab['2'])
            return True
        elif(self.tab['3']==self.tab['4']==self.tab['5']!=" "):
            print("Jogador vencedor: %s"%self.tab['3'])
            return True
        elif(self.tab['6']==self.tab['7']==self.tab['8']!=" "):
            print("Jogador vencedor: %s"%self.tab['6'])
            return True
        elif(" " not in self.tab.values()):
            print("Jogo empatado!")
            return True
        return False
    
    def initGame(self):
        self.tabuleiro()
        while(1):
            j = input("Jogada:")
            try:
                res = self.jogada(int(j),self.ids[self.isid])
                if res:
                    self.isid+=1
                    if(self.isid>1):
                        self.isid=0
                self.tabuleiro()
                if self.checkGame():
                    return
            except Exception as e:
                print("Jogada inválida! Jogada deve ser uma posição entre 0 e 8.")
            self.tabuleiro()

if __name__ == "__main__":
    jg = JogoDaVelha()
    jg.initGame()
