import string
while True:
    try:
        sentece=input("Please enter text: ")
        if not sentece:
            raise ValueError("Empty input is not allowed!")
        low_sentence=sentece.lower()
        clean_sentece=sentece.translate(str.maketrans("", "", string.punctuation))
        words=sentece.split()
        word_counter={}
        
        for kelime in words:
            if kelime in word_counter:
                word_counter[kelime]+=1
            else:
                word_counter[kelime]=1
        print(word_counter)
    except ValueError as e:
        print(f"Error:{e}")