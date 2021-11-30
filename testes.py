from gramatica import Gramatica

gramatica0 = Gramatica('gramatica0')
gramatica0.imprimir_gramatica()
#Pertence
gramatica0.testr_palavra_cyk('aabb')
#Não pertence
gramatica0.testr_palavra_cyk('aba')

gramatica1 = Gramatica('gramatica1')
gramatica1.imprimir_gramatica()
#Pertence
gramatica1.testr_palavra_cyk('ab')
#Não pertence
gramatica1.testr_palavra_cyk('aba')

gramatica2 = Gramatica('gramatica2')
gramatica2.imprimir_gramatica()
#Pertence
gramatica2.testr_palavra_cyk('bbaa')
#Não pertence
gramatica2.testr_palavra_cyk('aba')

gramatica3 = Gramatica('gramatica3')
gramatica3.imprimir_gramatica()
#Pertence
gramatica3.testr_palavra_cyk('baba')
#Não pertence
gramatica3.testr_palavra_cyk('aba')

gramatica4 = Gramatica('gramatica4')
gramatica4.imprimir_gramatica()
#Pertence
gramatica4.testr_palavra_cyk('bab')
#Não pertence
gramatica4.testr_palavra_cyk('bbbbb')

gramatica5 = Gramatica('gramatica5')
gramatica5.imprimir_gramatica()
#Pertence
gramatica5.testr_palavra_cyk('baaba')
#Não pertence
gramatica5.testr_palavra_cyk('baab')
