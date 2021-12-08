mensagem = "Por favor insira a operação matemática que deseja." 
mensagem += "\n+ para adição" 
mensagem += "\n- para subtração" 
mensagem += "\n/ para divisão" 
mensagem += "\n* para multiplicação: " 
mensagem += "\n** para potenciação: " 
operação = input (mensagem) 
num_1 = int(input("Digite um número: ")) 
num_2 = int(input("Digite outro número: ")) 
if operação == "+": print(f"{num_1} {operação} {num_2} = {num_1 + num_2}") 
elif operação == "-": print(f"{num_1} {operação} {num_2} = {num_1 - num_2}") 
elif operação == "/": print(f"{num_1} {operação} {num_2} = {num_1 / num_2}") 
elif operação == "*": print(f"{num_1} {operação} {num_2} = {num_1 * num_2}") 
elif operação == "**": print(f"{num_1} {operação} {num_2} = {num_1 ** num_2}") 
else : print("Operação matemática inválida, tente novamente!")