def chatbot():
    print("🤖: Hi! I'm a rule-based chatbot. How can I help you today?😊")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["exit", "quit", "bye"]:
            print("🤖: Goodbye! 👋 Have a great day! 🌟")
            break
        elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print("🤖: Hello! 👋 How can I assist you today? 😊")
        elif "how are you" in user_input:
            print("🤖: I'm just a program, but I'm running smoothly! ⚙️ How about you?😃")
        elif "your name" in user_input:
            print("🤖: I'm a simple rule-based chatbot. You can call me Chatbot! 🤖")
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"🤖: The current time is 🕒 {current_time}.")
        elif "date" in user_input:
            from datetime import datetime
            current_date = datetime.now().strftime("%Y-%m-%d")
            print(f"🤖: Today's date is 📅 {current_date}.")
        elif "help" in user_input:
            print("🤖: Sure! 🆘 I can answer basic questions like the time, date, or simple greetings. 🤝")
        elif "what is your favorite color" in user_input:
            print("🤖: I like blue 💙 because it reminds me of the sky and the ocean! What about you? 🎨")
        elif "what do you do" in user_input:
            print("🤖: I chat with people like you and try to make their day better! 😊 What do you do?")
        elif "tell me a joke" in user_input:
            print("🤖: Sure! Why don't skeletons fight each other? Because they don't have the guts! 😂")
        elif "what is your favorite food" in user_input:
            print("🤖: I don't eat food, but if I could, I'd probably love pizza! 🍕")
        elif "Can you sing a song?" in user_input:
            print("🤖: A good song can make your day better!😊 What do you recommend?")
        elif "What movies do you like?" in user_input:
            print("🤖: I love classic movies!😊What's your favorite movie?")
        elif "where are you from" in user_input:
            print("🤖: I'm from the digital world, where every bit counts! 🌐")
        elif "what is love" in user_input:
            print("🤖: Love is... complicated, but I think it's about connection and care! ❤️ What do you think?")
        elif "thank you" in user_input or "thanks" in user_input:
            print("🤖: You're welcome! 😊 Let me know if there's anything else I can do for you.")
        else:
            print("🤖: I'm sorry, I didn't understand that. ❓ Could you please rephrase? 🤔")
chatbot()