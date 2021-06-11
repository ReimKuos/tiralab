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

- degree of the markov chain, can be anything but 4-6 is recommended
- the program won't play the song and it can be found in the data directory it is the file "new_song.mid"

### Best way to run the program is this at the moment:
Give this command
 - try
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