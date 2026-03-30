def chatbot():
    print("Welcome to AI Course Assistant Bot!")
    print("Type 'exit' to quit.\n")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Bot: Goodbye!")
            break

        elif "hello" in user or "hi" in user:
            print("Bot: Hello! How can I help you today?")

        elif "course" in user:
            print("Bot: AI course covers Python, Machine Learning, and Data Analysis.")

        elif "python" in user:
            print("Bot: Python is used for Artificial Intelligence, data science, and automation.")

        elif "exam" in user:
            print("Bot: Exams act as a test to evaluate your understanding of concepts and coding.")

        elif "help" in user:
            print("Bot: I can answer questions about courses, exams, and Python.")

        else:
            print("Bot: Sorry, I didn’t understand that.")

chatbot()