from gramatica import Gramatica

gramatica0 = Gramatica('gramatica0')
#Pertence
gramatica0.testr_palavra_cyk('aabb')
#Não pertence
gramatica0.testr_palavra_cyk('aba')

gramatica1 = Gramatica('gramatica1')
#Pertence
gramatica1.testr_palavra_cyk('ab')
#Não pertence
gramatica1.testr_palavra_cyk('aba')

gramatica2 = Gramatica('gramatica2')
#Pertence
gramatica2.testr_palavra_cyk('bbaa')
#Não pertence
gramatica2.testr_palavra_cyk('aba')

gramatica3 = Gramatica('gramatica3')
#Pertence
gramatica3.testr_palavra_cyk('baba')
#Não pertence
gramatica3.testr_palavra_cyk('aba')

gramatica4 = Gramatica('gramatica4')
#Pertence
gramatica4.testr_palavra_cyk('bab')
#Não pertence
gramatica4.testr_palavra_cyk('bbbbb')
