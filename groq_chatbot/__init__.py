if __name__ == "__main__":
    from groq_chatbot import DocumentResponder
    responder = DocumentResponder(r'data/Corpus.pdf')

    while True:
        try:
            user_query = input("You: ")
            result = responder.response(user_query, history='')
            print("Chatbot: ", result)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("Error: ", e)
