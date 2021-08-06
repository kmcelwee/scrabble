# scrabble

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![pytest](https://github.com/kmcelwee/scrabble/actions/workflows/unittests.yaml/badge.svg)](https://github.com/kmcelwee/scrabble/actions/workflows/unittests.yaml)

[Read article in Nautilus Magazine here](http://nautil.us/issue/67/reboot/does-scrabble-need-to-be-fixed)

This project parses data from Quackle, an automated Scrabble player. Thousands of test games are on file with various tile values (Traditional: the standard tile values, Lewis: the suggested values by Joshua Lewis in 2013 from his [Valett package](https://github.com/jmlewis/valett), One/Fifty: all tiles equal to those values, and Random: randomly assigned values, with an average equal to that of Traditional.)

[View the analysis](results.ipynb)

## Installation

Create a python 3.8 virtual environment and install the requirements:

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### `automateQuackle.py`

This script is a risky, bootstrap way of running multiple Quackle games. The program takes over the keyboard, and manually enters what would be required of a person. The rate is approximately 800 games per hour.

To begin a test, save one file into the desired folder (do not save as `[someNumber].gcg`). This will set the correct destination for all future games. Then, start one more AI/AI game, begin the program, and quickly return to Quackle. 
The program should then run smoothly with `python automateQuackle.py`.

Preferably save to an empty folder. As the destination folder gets larger, Quackle 
may take longer than the allotted time to open the save menu. This would throw
everything out of sync, and waste your time.

Other things to note:

* The process is usually reliable in 1000-game intervals, and it may be helpful
to disconnect your computer from the internet and close all applications. 
Sometimes the game is saved before it finishes. See the `clean` CLI method to help correct these errors.
* This is written for Mac (e.g. keyDown('command')).
* This program takes *TOTAL CONTROL* of your laptop. Use with caution. If you find a better way, I'd be happy to hear from you!

### `clean`
Because we automate Quackle hoping that the timing is correct, some files are saved before the game is over. This program searches for "#rack", a string used gcg files to show Quackle where the game was left off.

A list of the error files are printed, and the program offers to delete those files. On average, automateQuackle.py produces incomplete files 1/500 times.

To run this command from the command-line type `python cli.py clean`.

```
Usage: cli.py clean [OPTIONS]

  Delete incomplete gcg files

Options:
  -d, --data-dir TEXT  The directory (and subdirectories) where we will search
                       for malformed gcg files  [default: data]

  --help               Show this message and exit.
```

### `generate-csvs`

This script runs through the four directories of quackle files -- Traditional, Lewis, One, and Fifty -- and creates  CSVs with their data parsed from parseQuackle.py. It also appends the percent difference.

To run this command from the command-line type `python cli.py generate-csvs`.

```
Usage: cli.py generate-csvs [OPTIONS]

  Generate CSV files for all games in a subdirectory

Options:
  -d, --data-dir TEXT  The directory where we will search for subdirectories
                       and create a CSV file for those subdirectories
                       [default: data]

  --help               Show this message and exit.
```

## Tile values

Tile values are stored in [tile-values.csv](tile-values.csv).

### Install black pre-commit

In order to follow black style guidelines, simply run the following command:

```sh
pre-commit install
```

This will prevent you from committing un-styled code.
