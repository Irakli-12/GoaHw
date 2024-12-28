# 1) გაიარეთ sololearn'ი Modulo 4 Quiz'ის ჩათვლით
# Done
# 2) გამოიყენეთ for loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი
product = 1  

for i in range(1, 11): 
    product *= i  

print(product)  

# 3) გამოიყენეთ while loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი
product = 1  # ნამრავლი იწყება 1-ით
i = 1  # ლუპის სტარტული რიცხვი

while i <= 10:  
    product *= i  
    i += 1  

print(product)  
