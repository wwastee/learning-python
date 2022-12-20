#test classi


class dipendente:
    
    def __init__(self, nome, cognome, salario):
        self.nome = nome
        self.cognome = cognome
        self.salario = salario
        
    def nomecompleto(self):
        return (self.nome +' '+ self.cognome) 
    
    def emailDip(self):
        return (self.nome + '.' + self.cognome + '@gmail.com')
    
dip1 = dipendente('Francesco' , 'Bertolini' , '100k')

print(dip1.nomecompleto())
print(dip1.emailDip())