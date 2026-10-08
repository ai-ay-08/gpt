import torch
import torch.nn as nn 

from tokenizer import Tokenizer

class GPT(nn.Module):
    def __init__(self, vocab_size, embedding_dim, block_size):
        super().__init__() # initialize the parent class nn.Module

        self.embedding = nn.Embedding(vocab_size, embedding_dim) # create an embedding layer for text
        self.position_embedding = nn.Embedding(block_size, embedding_dim) # create an embedding layer that tracks position

    def forward(self, tokens):
        positions = torch.arange(tokens.shape[0])

        token_vectors = self.embedding(tokens)
        position_vectors = self.position_embedding(positions)

        return token_vectors + position_vectors # add together token_vectors and position_vectors (combined information)