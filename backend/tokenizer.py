# tokenizer class converts text into an array of tokens to be used in model.py

class Tokenizer:
    def __init__(self, text): 
        chars = sorted(list(set(text)))

        self.vocab_size = len(chars)

        self.char_to_id = {}
        self.id_to_char = {}

        for i, char in enumerate(chars):
            self.char_to_id[char] = i
            self.id_to_char[i] = char

    def encode(self, text):
        return [self.char_to_id[char] for char in text]

    def decode(self, ids):
        return ''.join([self.id_to_char[i] for i in ids])