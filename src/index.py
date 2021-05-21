from datastructs.trie import Trie
from trainer import train

def main():
    """
    Is supposed to call the algorithm and play music, but at thi moment just
    reads a one file and saves the results in the trie, this function will be moved
    elsewhere later.
    """
    trie = Trie()
    train(trie, "mond_3.mid")



if __name__ == "__main__":
    main()
