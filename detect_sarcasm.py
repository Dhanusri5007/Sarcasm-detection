def detect_sarcasm(sentence):
    s = sentence.lower()

    score = 0

    #  Sarcastic keywords
    sarcastic_words = ["wow", "great", "amazing", "fantastic", "love"]
    for word in sarcastic_words:
        if word in s:
            score += 1

    #  Negative situations
    negative_words = ["fail", "bad", "worst", "late", "tired", "exam"]
    for word in negative_words:
        if word in s:
            score += 1

    #  Exclamation mark
    if "!" in sentence:
        score += 1

    #  Repeated letters (like "soooo")
    for word in s.split():
        if len(set(word)) < len(word) / 2:
            score += 1

    #  Opposite tone (positive + negative together)
    positive_words = ["love", "great", "awesome"]
    for p in positive_words:
        for n in negative_words:
            if p in s and n in s:
                score += 2

    # Final decision
    if score >= 2:
        return "Sarcastic "
    else:
        return "Not Sarcastic "


# User input
while True:
    text = input("Enter a sentence: ")
    print(detect_sarcasm(text))