def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer? (A, B, C or D)").upper()
        if answer == question["answer"]:
            print("Salute, That is correct Bru!,\n")
            score += 1
        else:
            print(f"Wrong!!! are you even from Cape Town? Try Again!!!")

    print(f"You got {score} out of  {len(questions)} questions correct/")


questions = [
    {
        "prompt" : "What is the best beer to drink before a fight?",
        "options" :["A. Black label" , "B. Castle Lager" , "C. Flying Fish"],
        "answer" : "A"
    },
    {
        "prompt": "Where do you get the best Gatsby's in Cape Town?",
        "options": ["A. Golden Dish", "B. Aneesa's", "C. Mariam's Kitchen"],
        "answer": "A"
    },
    {
        "prompt": "What is the best way to celebrate a Friday?",
        "options": ["A. Fast Food", "B. Intercourse", "C. Smoking a joint"],
        "answer": "C"
    },
    {
        "prompt": "Where is the best place to meet women?",
        "options": ["A. Gym", "B. Club", "C. Hotels"],
        "answer": "A"
    },
    {
        "prompt": "What car is the best car "
                  "to spin with?",
        "options": ["A. Ford Mustang", "B. Mercedes A45 AMG", "C. BMW M4"],
        "answer": "B"
    }
]

run_quiz(questions)