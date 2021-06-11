from pygame import mixer
import os
from datastructs.trie import Trie
from trainer import train
from chain_creator import create_sequence
from music_file_creator import create_music


class CommandlineUI:
    """
    A crude commandline interface for operating the music
    creation
    """

    def __init__(self):

        self.trie = Trie()
        self.degree = 4

    def execute(self):
        print(
            "Give the degree of the markov chain (range 3-6)"
        )
        degree = int(input())
        self.degree = degree
        self.train()
        self.create()

    def train(self):

        print("Reading files and training")
        path = "data/training//"
        for file in os.listdir(path):
            if file.endswith(".mid"):
                train(self.trie, file, self.degree)

    def create(self):

        print("Creating music")
        seq = create_sequence(self.trie, self.degree)
        print("Creating a music file")
        create_music(seq)
        print("Done!")
