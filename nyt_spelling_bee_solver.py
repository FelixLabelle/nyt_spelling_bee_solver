# Spelling bee NYT puzzle solver

with open('words.txt') as words_fh:
    # Converts strips and lowercases lexicon (space seperated txt file)
    # Use set to remove duplicates (decasing)
	lexicon = set(list(map(lambda x: x.strip().lower(), words_fh.readlines())))

# NOTE: Could add a CLI to allow users to input this. Manual edits are the way for now
MANDATORY_LETTER = 'l'
LETTERS = set(['t','i','e','v','p','x'] + [MANDATORY_LETTER])

# Search for valid words 
valid_words = [word for word in lexicon if set(word).issubset(LETTERS) and MANDATORY_LETTER in set(word) and len(word) >= 4]
sorted_valid_words = sorted(valid_words, key=lambda x: len(x))
print(sorted_valid_words)