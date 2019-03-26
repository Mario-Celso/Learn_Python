class Pokemon(object):
    __slots__ = ['name','__HP']
    
    def __init__(self, name, HP):

        self.name = name #publico
        self.__HP = HP #privado
    #getter tradicional
    #def get_HP(self):
        #return self.__HP
    
    #getter decorator
    @property
    def HP(self):
        """Returns pokemon HP."""
        return self.__HP
    
    #setter
    '''def set_HP(self, HP):
        self.__HP = HP'''
    
    #setter decorator
    @HP.setter
    def HP(self, HP):
        """Returns pokemon HP."""
        self.__HP = HP



#código principal do programa
def main():
    #cria um pokemon
    pikachu = Pokemon('Pikachu', 100)
    print("Nome: %s" %(pikachu.name))
    print("HP: %d" %(pikachu.HP))
    print()
    
    
    pikachu.HP = 50
    
    #Exibe informaçoes do pokemon
    print("Nome: %s" %(pikachu.name))
    print("HP: %d" %(pikachu.HP))
    print()
    

    #print(pikachu.__dict__)
    print(pikachu.__slots__)
  

if __name__ == "__main__":
    main()