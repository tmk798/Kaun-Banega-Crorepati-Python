
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
questions = [
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
    ["Which language has become popular nowadays for android asapp development?","java","C","HTML","Kotlin","None",4],
]
levels=[1000,5000,8000,9000]
money = 0
for i in range(0,len(questions)):
    question= questions[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"a.{question[1]}                                                b.{question[2]}")
    print(f"c.{question[3]}                                                 d.{question[4]}")
    reply = int(input("Enter your answer (1-4)"))
    
    if(reply == question[-1]):
        print(f"Correct Answer ,you have won Rs.{levels[i]}")
        if(i==4):
            money = 10000
        
    else:
      print("Afsos Ye Galat Jawab Hai!")
      break
