# User manual

## Installing and running

### Important:

The program needs mido- library to work, this can be installed with command

```bash
pip install mido
```

Also poetry is needed 

```bash
pip install poetry
```

### Setting up poetry

This has to be done before anything can be run

```bash
poetry install
```

### Running the program
At the moment somewhat broken

```bash
poetry run invoke start
```

## What happens

- First the program will be ask for the degree of the markov chain the program recommends a value between (4-6) but larger or samller values will work, non numerical values will crash the program, after this a trie is 'trained'
- Secondly it will ask if you want to create a music file (these will be found in the ./data/created directory) and after this it will ask for a name for the file
- next it will jump bak to the second step (this loop will end when input is not 'y') 

It is important to mention that the program cannot play the files it creates due to complications with poetry and pygmame.mixer, for this reason you need to use an external midi program to listen to the output files

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