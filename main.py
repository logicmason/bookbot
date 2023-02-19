with open("books/frankenstein.txt") as f:
  file_contents = f.read()
  words = file_contents.split()
  char_counts = {}
  for word in words:
    for char in word:
      l = char.lower()
      if l in char_counts:
        char_counts[l] += 1
      else:
        char_counts[l] = 1

print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} words found in document\n")
chars = list(char_counts.keys())
chars.sort()
for letter in chars:
  if letter.isalpha():
    print(f"The '{letter}' character was found {char_counts[letter]} times")
print("--- End report ---")
