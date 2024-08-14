
input_sentence = input("문장을 입력하세요: ")
text = str(input_sentence)
word_count = 0
target_word = "사랑"
words = text.lower().split() 
for word in words:
    cleaned_word = word.strip(".,!?")
    if cleaned_word == target_word:
        word_count += 1

# 단어의 개수를 출력
print(f"'{target_word}'의 개수:", word_count)
