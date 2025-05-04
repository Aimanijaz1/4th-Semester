prompts = [
    # Greeting and showing options
    [r"(hi|hello|hey)", [
    "👋 Hello! Welcome to the Medical Center. How can I assist you today?\n"
    "Here are the things you can ask:\n"
    "1. I want an appointment tomorrow\n"
    "2. What are your business hours?\n"
    "3. Do you have specialists?\n"
    "4. Where are you located?\n"
    "5. How much do tests cost?\n"
    "6. What should I do in an emergency\n"
    "7. Thank you / Goodbye\n\n"
    "Please type your question."]],

    [r"(I want an appointment tomorrow|How can i get appointment?|Please tell me appointment process|Can I schedule an appointment for tomorrow?|How do I book an appointment?)", 
        ["You can book an appointment by calling our reception at 042-1234567.", 
         "Appointments can be scheduled online or via phone call. Do you want the link?", 
         "You can call our office or visit our website to book an appointment. Would you like more details?"]],

    [r"(What time do you open?|When are you open?|What are your business hours?)", 
        ["We are open from 9 AM to 8 PM, Monday to Saturday.", 
         "Our center operates from 9 in the morning till 8 in the evening.", 
         "Our working hours are from 9 AM until 8 PM every weekday, and we are closed on Sundays."]],

    [r"(What should I do in an emergency|What if I have an urgent issue?)", 
        ["For emergencies, please visit our ER directly or call our 24/7 helpline: 042-7654321.", 
         "In case of an emergency, come directly to our emergency room or dial 042-7654321 for immediate assistance.",
         "If it's an emergency, please head straight to our emergency room or reach us at our 24/7 helpline."]],

    [r"Do you have specialists?|What kind of specialists are available?", 
        ["We have specialists in cardiology, neurology, dermatology, and pediatrics. Which one are you looking for?", 
         "We have highly qualified specialists in several fields, including cardiology, dermatology, pediatrics, and neurology. Let me know what you're looking for.",
         "We offer expert consultations in cardiology, neurology, dermatology, and pediatrics. Which specialist would you like to consult?"]],

    [r"Can you tell me your address?|Where are you located?", 
        ["We are located at 123 Medical Road, Lahore.", 
         "The Medical Center is near the University Gate, opposite City Pharmacy."]],

    [r"How much do tests cost?|What is the price of a medical test?", 
        ["Can you please specify which test? We offer blood tests, X-rays, MRIs and more.",
         "Prices vary based on the test you require. Can you tell me what kind of test you're looking for?",
         "Test prices depend on the type of test. Could you tell me which test you're referring to?"]],

 
    [r"Thank you for your help|I appreciate your assistance", 
        ["You're welcome!", "Happy to help!", "Any time!", 
         "You're very welcome. Let me know if you need anything else.", 
         "Glad I could assist. Don't hesitate to reach out if you need more help!"]],

    [r"Goodbye|See you later|Take care", 
        ["Goodbye! Take care!", "See you again. Stay healthy!", 
         "Take care and have a great day! Don't hesitate to contact us again.",
         "Goodbye! Wishing you good health and hope to assist you again soon."]]]
