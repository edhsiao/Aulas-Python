def ex5():
    ganho= input("Quanto voce ganha por hora? ")
    hora = input("Trabalha quantos horas por mes? ")
    bruto = ganho*hora
    desconto = bruto*0.11 + bruto*0.08 + bruto*0.05
    print "O valor do seu salario bruto eh: ", bruto  
    print "O valor do Imposto de renda eh:", bruto*0.11
    print "O valor do INSS eh: ",bruto*0.08
    print "O valor pago a sndicato eh: ", bruto*0.05
    print "O valor do desconto total:" ,desconto
    print "O valor do salario liquido eh:", bruto - desconto
