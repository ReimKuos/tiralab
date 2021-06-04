# Implementation

## Project Structure

Simplification of structure wia the process of music generation, this is for the purpose of making code review easier will be updated to more throughout later

 - A trie is created
 - A midi file is used to create a list of notes
 - this list is used to update the trie by saving instances of six last notes into it
 - this is done for many files
 - a note sequnce is created by looking back at last five notes and randomizing one of the possible following notes (this is weighted by the frekvency of notes in the training phase)
 - from this sequnce a midifile is created and played

## Time complexity

### Data structure

Explanations for some will be added later

 - Trie
    - adding is O(n), where n is length of the input string
    - finding is O(n), where n is length of the input string
    - finding nextt is O(nm), where n is the depth m largest number of childs in one note in the path (this is worst case, best is O(n))
- Queue
    - adding is O(1)
    - removing is O(1)
    - going trough the whole queue is O(n)

    