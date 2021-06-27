import os
from datastructs.trie import Trie
from trainer import train
from chain_creator import create_sequence
from music_file_creator import create_music
from time_trainer import train_time


class CommandlineUI:
    """
    A crude commandline interface for operating the music
    creation
    """

    def __init__(self):
        """
        Sets both tries ready for training and sets the base degree of
        the markov chain 
        """

        self.trie = Trie()
        self.time = Trie()
        self.degree = 4

    def execute(self):
        """
        Takes input trought the command line and executes methods accordingly 
        """
        
        print(
            "Give the degree of the markov chain (range 3-6)"
        )
        degree = int(input())
        self.degree = degree

        print("Reading files and training")

        self.train()

        while input("Create a file? (y/n)\n") == "y":
            name = input(
                "Give a name for the created file (without file ending)\n"
                )
            self.create(name)

        print("\nDone - the program ha s closed")

    def train(self):
        """
        Trains the note trie by using every file in the data/training
        directory and also trains the time trie with the hard coded file
        in the time training function
        """

        path = "data/training//"

        for file in os.listdir(path):
            if file.endswith(".mid"):
                train(self.trie, file, self.degree)

        train_time(self.time, "chpn-p1.mid")

        print("Training complete!\n")

    def create(self, name):
        """
        Creates a sequnce based on the trie and creates a midi file based on
        that file
        """
        seq = create_sequence(self.trie, self.time, self.degree)
        create_music(seq, name)
        print(f"file {name}.mid created\n")
