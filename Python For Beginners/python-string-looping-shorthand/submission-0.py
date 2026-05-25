def print_string_characters(word1: str, word2: str) -> None:
    l = [word1, word2]
    for i in l:
        for j in range(len(i)):
            print(i[j])




# do not modify below this line
print_string_characters("Hello, World!", "Good Job!")
