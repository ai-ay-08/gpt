import torch
import torch.nn as nn 

from tokenizer import Tokenizer

class GPT(nn.Module):
    def __init__(self, vocab_size, embedding_dim, block_size):
        super().__init__() # initialize the parent class nn.Module

        self.embedding = nn.Embedding(vocab_size, embedding_dim) # create an embedding layer for text
        self.position_embedding = nn.Embedding(block_size, embedding_dim) # create an embedding layer that tracks position

        self.output = nn.Linear(embedding_dim, vocab_size) # create a linear layer that predicts the next token

        # create an attention layer; currently there is only 1 attention head 
        # and the number of batches is the first parameter
        self.attention = nn.MultiheadAttention(embedding_dim, num_heads = 1, batch_first = True) 

    def forward(self, tokens):
        positions = torch.arange(tokens.shape[0])

        token_vectors = self.embedding(tokens)
        position_vectors = self.position_embedding(positions)

        x = token_vectors + position_vectors
        x = x.unsqueeze(0)

        mask = torch.triu(torch.ones(x.shape[1], x.shape[1]), diagonal = 1).bool()

        x, _ = self.attention(x, x, x, attn_mask = mask)

        # i will potentially have to run x.squeeze(0) here, will see later
        logits = self.output(x)

        return logits

model = GPT(1000, 64, 1024)
tokenizer = Tokenizer("abcdefghijklmnopqrstuvwxyz !*@(&*$^*&@!#)*!&#*()DHSAUIHICABISADODJQWHIX")
tokens = torch.tensor(tokenizer.encode("hello world!"))

inputs = tokens[:-1]
targets = tokens[1:]

for _ in range(10):
    output = model(tokens)
    last_token_scores = output[0, -1, :]
    probabilities = torch.softmax(last_token_scores, dim = 0)
    next_token = torch.multinomial(probabilities, num_samples = 1)

    tokens = torch.cat((tokens, next_token))

    print(tokenizer.decode(tokens.tolist()))