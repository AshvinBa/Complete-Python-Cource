def count_word_freq(input_string):
    words = input_string.split()
    frequency = {}
    
    for word in words:
        
        if word.isalpha():
            frequency[word] = frequency.get(word , 0) + 1
            
            
    print("The Pairs of the Number is: ")
    for word,count in frequency.items():
        print(f"{word} : {count}")

input_string = input("Enter the string: ")
count_word_freq(input_string)