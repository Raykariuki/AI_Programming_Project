def chatbot():
    print("Course Assistant Bot")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye! Have a great day!")
            break

        matched = next((key for key in responses if key in user_input), None)

        response_function = responses.get(matched, default_response)

        print("Bot:", response_function())
def greet():
    return "Hello! How can I assist you today?"

def course_info():
    return "This course covers AI basics, Python programming, real-world applications, Machine Learning, and Data Analysis."

def exam_info():
    return "Exams are scheduled for the end of the semester. Make sure to review all materials and practice coding exercises."

def help_response():
    return "Sure! You can ask me about courses, exams, or AI topics."

def ai_definition():
    return "Artificial Intelligence (AI) refers to machines that perform tasks requiring human intelligence."

def default_response():
    return "I'm sorry, I didn't understand that. Could you please rephrase?"


responses = {
    "hello": greet,
    "hi": greet,
    "course": course_info,
    "exam": exam_info,
    "exams": exam_info,
    "help": help_response,
    "ai": ai_definition,
    "artificial intelligence": ai_definition
}


chatbot()