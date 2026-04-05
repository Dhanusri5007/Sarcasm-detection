def detect_sarcasm(sentence):
    s = sentence.lower()

    positive_words = ["great", "amazing", "love", "nice", "good", "awesome", "perfect"]
    negative_words = ["bad", "worst", "late", "tired", "failed", "error", "rain", "problem", "stuck", "missed"]

    sarcastic_phrases = ["yeah right", "as if", "just what i needed", "of course", "how nice"]

    score = 0

    #  Direct sarcastic phrases
    for phrase in sarcastic_phrases:
        if phrase in s:
            return "Sarcastic"

    #  Positive + Negative words together
    for p in positive_words:
        for n in negative_words:
            if p in s and n in s:
                score += 2

    #  Positive word with bad situation
    bad_situations = ["traffic", "exam", "delay", "bug", "issue", "problem"]

    for p in positive_words:
        for b in bad_situations:
            if p in s and b in s:
                score += 1

    # Final decision
    if score >= 2:
        return "Sarcastic"
    else:
        return "Not Sarcastic"


# User input 
while True:
    text = input("Enter a sentence: ")
    print(detect_sarcasm(text))
