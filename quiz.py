#Build a quiz game that reads questions and answers from a 

'''name=open("quiz.txt",'w')
questions = [
    {
        'question': 'What is the capital of France?',
        'options':['Berlin', 'Madrid', 'Paris', 'Rome'],
        'answer': 'Paris'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options':['Mars', 'Jupiter', 'Venus', 'Saturn'],
        'answer': 'Mars'
    },
    {
        'question': 'What is the largest mammal on Earth?',
        'options':['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
        'answer': 'Blue Whale'
    },
    {
        'question': 'In which year did Christopher Columbus reach the Americas?',
        'options':['1492', '1601', '1776', '1832'],
        'answer': '1492'
    },
    {
        'question': 'Who wrote "Romeo and Juliet"?',
        'options':['William Shakespeare', 'Jane Austen', 'Charles Dickens', 'Homer'],
        'answer': 'William Shakespeare'
    },
    {
        'question': 'What is the capital of Japan?',
        'options': ['Seoul', 'Beijing', 'Tokyo', 'Bangkok'],
        'answer': 'Tokyo'
    },
    {
        'question': 'Which programming language is known for its readability and simplicity?',
        'options': ['Java', 'Python', 'C++', 'Ruby'],
        'answer': 'Python'
    },
    {
        'question': 'What is the chemical symbol for gold?',
        'options': ['Au', 'Ag', 'Fe', 'Cu'],
        'answer': 'Au'
    },
    {
        'question': 'Who painted the Mona Lisa?',
        'options': ['Vincent van Gogh', 'Leonardo da Vinci', 'Pablo Picasso', 'Claude Monet'],
        'answer': 'Leonardo da Vinci'
    },
    {
        'question': 'Which of the following is a primary color?',
        'options': ['Green', 'Orange', 'Blue', 'Brown'],
        'answer': 'Blue'
    },
]

name.write(str(questions))
name.close()'''

name=open("quiz.txt",'r')
content=name.readlines()
score=0

for i in content:
    i=i.split(';')
    #print(i)
    print(i[0])
    print(i[1][9:-1])
    ans=input("Enter the answer according to yhe option:")
    if ans==i[2][7:-1]:
        score+=1
        print("Correct answer")
    else:
        print("Wrong answer")

print(f"The final score is {score}")

    
        
        


