# User manual

At the moment running the program does nothing

## Installing and running

### Important:

The program needs mido- library to work, this can be installed with command

```bash
pip install mido
```

### Installing poetry

This has to be done before anything can be run

```bash
poetry install
```

### Running the program

```bash
poetry run invoke start
```

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