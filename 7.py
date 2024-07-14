from collections import Counter
import re

text = "GeekBrains is a Russian company in the field of online education. Founded in 2010. An educational platform that helps to master a profession and get an IT education. Teachers-practitioners have been teaching information technology, programming, analytics, testing, marketing, management, and design for more than 10 years. Since 2016, it has been a part of VK. One of the top five Russian online education companies."

cleaned_text = re.sub(r'[^\w\s]', '', text).lower()

words = cleaned_text.split()
word_counts = Counter(words)

most_common_words = word_counts.most_common(10)

print("10 самых часто встречающихся слов:")
for word, count in most_common_words:
    print(f"{word}: {count}")
