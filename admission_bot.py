import random

class AdmissionChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm your college admission chatbot. How can I help you today?"

    def admission_procedure_response(self):
        return "To apply for admission, you can visit the college website and follow the online application process. Make sure to submit all required documents."

    def admission_requirements_response(self):
        return "Admission requirements vary, but commonly include high school transcripts, standardized test scores, letters of recommendation, and a personal statement. It's advisable to check the specific requirements on the college website."

    def admission_deadlines_response(self):
        return "Application deadlines depend on the college and program. Check the college website for the most accurate and up-to-date information."

    def handle_user_input(self, user_input):
        if "procedure" in user_input:
            return self.admission_procedure_response()
        elif "requirements" in user_input:
            return self.admission_requirements_response()
        elif "deadlines" in user_input:
            return self.admission_deadlines_response()
        elif "bye" in user_input.lower():
            return "Goodbye! If you have more questions, feel free to ask anytime."
        else:
            return "I'm sorry, I didn't understand that. Can you please ask another question or specify your admission query?"

    def chat(self):
        print(self.greet())

        while True:
            user_input = input("You: ")

            if "thank" in user_input.lower():
                print("Chatbot: You're welcome! If you have more questions, feel free to ask.")
                break

            response = self.handle_user_input(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    admission_chatbot = AdmissionChatbot()
    admission_chatbot.chat()
