# User manual

At the moment running the program does nothing

## Installing and running

### Important:

The program needs mido- and pygame- library to work, this can be installed with command

```bash
pip install mido
```
```bash
pip install pygame
```

### Installing poetry

This has to be done before anything can be run

```bash
poetry install
```

### Running the program
At the moment somewhat broken

```bash
poetry run invoke start
```

## Commands for the program

At the moment there are 5 commands which are 
- train: which adds data to the trie
    - when it asks for a filename, that file has to be in the data/training/ directory
    - all trains whit all hard programmed files
- create: creates a midi file using the algorithm, replaces the previous one (saving comes later)
- play: plays the created tune
- stop: ends the music
- quit: end the program

Alltough play and stop won't seem to work if program was started trough poetry

if the program won't play the music, you can play the saved piece externally on a midi player, the file name is new_song.mid and it's located in the data directory

### Best way to run the program is this at the moment:
Give these commands in order
 - train
 - all
 - create
 - play 
(if play gives an error just open the afformentioned file in an external midi player, running by using the index.py in visual studio should run the program)

## Testing

### Running tests

```bash
poetry run invoke test
```

### Creating a coverage- report

```bash
poetry run invoke coverage-report
```

## Pylint

The .pylintrc- file was copied from the OT-project

```bash
poetry run invoke lint
```