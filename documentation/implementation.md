# Implementation

## Algorithm Structure

### General idea

The process of the algorithm is as follows

 - First two tries are created, one for notes and a second for time
 - The note trie is trained by adding sequnences by first using the reading files and passing their output sequnces trought the train function, this is done for every file used for training
 - after this same is done with a sigle specified to the time trie 
 - Next the sequnce of notes is created using the create_sequnce function
 - Last this sequence is used to create the midi file 

### Pseudo code

    def create_music(degree):

        note_trie = Trie
        time_trie = Trie

        for file in files:
            train(note_trie, degree)
        time_train(time_trie)

        sequence = create_sequence(note_trie, time_trie, degree)
        create_music_file(sequence)


## Time complexity

### Data structure

 - Trie
    - Add
        - As the only repeated operations in the method are inside a singular loop that goes trough all the nodes in the input key, the time complexity of adding is O(n), where n is length of the input queue
    - find
        - As the only repeated operations in the method are inside a singular loop that goes trough all the nodes in the input key, the time complexity of adding is O(n), where n is length of the input queue
    - find_next
        - First the find method is called once to find a node then a loop size 129 is used to find the return value, as it can be at index 1 to 129 whit equal change the time is linear as smaller values on avarage result in less loops due to the aggregating value that stops the loop, for these reasons the time complexity is O(n + k), where n is the size of the key and k is the size of the limit value

- Queue
    - add
        - As the method does not call any function nor have any loops the time complexity si constant meaning O(1)
    - remove
        - As the method does not call any function nor have any loops the time complexity si constant meaning O(1)
    - As the next location of the next node can be found in the current node going trough the whole queue is O(n), where n is the size of queue

### Algorithms/Functions

 - readfile
    - The reading of the file (using the mido function) has the time complecity of O(n), convertinfg this data
 - train
    - Construction of the key stays constant during the loop, but as the tries add method is called we get the time complexity O(kn), where n is the lenght of the inout sequnce and k is the degree of the makrov chain
 - train_time
    - else identical to trainer, but n is always 2 and for this reason the time complexity is O(k), where k is the lenght of the file
 - find_transposing_value
    - size of the file is the only affecting time complexity of the function hence the time complexity is O(n) 
 - create_sequence
    - As the exit condition of the function is based in randomness there is no spesific relation, but we can give an estima. Based on probability calculus we can say that the file made by the function is approximately avarage file lenght of all input files of the training function this effects the base loop which also calls the tries method find next (as the limit value is random we can that it functions as a constant in this case) we can get the avarage time complexity O(nm), where the n is the degree and m the avarage lenght of the training files
 - create_music_file
    - This function just employs a simple loop to create a file from a given sequence, for this reason the time coplecity is simply O(n) 

### The total time complexity

Based on totality of all parts the time complexity is O(kmn), where k is the degree of makrov chain, m is the avarage length of the training files and n is the number of training files