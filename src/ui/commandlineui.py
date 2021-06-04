from pygame import mixer
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
        self.running = True
        mixer.init()

    def start(self):
        """
        starts the mainloop
        """

        self.mainloop()

    def mainloop(self):
        """
        Mainloop that takes command and takes actions based on them
        """

        while self.running:

            command = input("Give a command: ")

            if command == "play":
                self.play_music()

            elif command == "stop":
                self.stop_music()

            elif command == "train":
                filename = input("Give filename: ")

                if filename == "all":
                    self.train_all()
                else:
                    self.train(filename)
            
            elif command == "save":
                pass

            elif command == "create":
                self.create_piece()

            elif command == "quit":
                self.running = False

            elif command == "try":
                self.tester()

            else:
                print("Command not right")

        print("")

    def train(self, filename):
        """
        'Trains' the trie by saving notes of a given midi file in it

        Args:
            filename: name of the midi file used for training
        """

        train(self.trie, filename)

    def create_piece(self):
        """
        creates a midi file cointaining the music created by the algorithm
        """

        seq = create_sequence(self.trie)
        create_music(seq)

    def train_all(self):
        """
        At the moment has all the music files hard coded, will use a file that
        has all their names later
        """

        train(self.trie, "cs3-1pre.mid")
        train(self.trie, "cs3-2all.mid")
        train(self.trie, "cs3-3cou.mid")
        train(self.trie, "cs3-4sar.mid")
        train(self.trie, "cs3-5bou.mid")
        train(self.trie, "cs3-6gig.mid")

        train(self.trie, "jsbtafc.mid")

        train(self.trie, "mozk309a.mid")
        train(self.trie, "mozk309b.mid")
        train(self.trie, "mozk309c.mid")

        train(self.trie, "mozk246a.mid")
        train(self.trie, "mozk246b.mid")
        train(self.trie, "mozk246c.mid")

    def play_music(self):
        """
        plays the music file the algorithm creates
        """

        mixer.music.load("data/new_song.mid")
        mixer.music.play()

    def stop_music(self):
        """
        stops music if it's not playing
        """

        mixer.music.stop()

    def tester(self):
        """
        Creates a piece from with all training
        """

        self.train_all()
        self.create_piece()
        self.play_music()
