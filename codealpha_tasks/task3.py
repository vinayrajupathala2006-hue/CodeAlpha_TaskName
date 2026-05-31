def get_bot_response(user_input):
    """
    Function to match user input to predefined rules using if-elif-else.
    """
    # Normalize input: convert to lowercase and remove trailing/leading spaces
    processed_input = user_input.lower().strip()
    
    # Predefined rules for mapping matching keywords to responses
    if "hello" in processed_input or "hi" in processed_input:
        return "Bot: Hi there! How can I help you today?"
        
    elif "how are you" in processed_input:
        return "Bot: I'm doing great, thank you for asking! How are you?"
        
    elif "your name" in processed_input:
        return "Bot: I am a simple rule-based Python chatbot."
        
    elif "bye" in processed_input or "exit" in processed_input:
        return "Bot: Goodbye! Have a wonderful day!"
        
    # Default fallback reply if the bot doesn't recognize the input
    else:
        return "Bot: I'm sorry, I didn't quite catch that. Could you try rephrasing?"


def run_chatbot():
    """
    Main loop function handling console Input/Output.
    """
    print("==================================================")
    print("       Welcome to the Rule-Based Chatbot!        ")
    print("  Type your message below (or 'bye' to exit).   ")
    print("==================================================")
    
    # Keep the conversation active using a loop
    while True:
        # Get console input from user
        user_message = input("\nYou: ")
        
        # Get the corresponding rule-based response from the function
        bot_reply = get_bot_response(user_message)
        
        # Display the bot's response
        print(bot_reply)
        
        # Break out of the infinite loop if the user wants to say goodbye
        if "bye" in user_message.lower().strip() or "exit" in user_message.lower().strip():
            break


if __name__ == "__main__":
    run_chatbot()