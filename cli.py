import os
import typer
import pandas as pd

from Quackle import QuackleGame

app = typer.Typer(name="Multiplicative Persistence Explorer", add_completion=False)

# Delete bad files
@app.command()
def clean(
    data_dir: str = typer.Option(
        "data",
        "--data-dir",
        "-d",
        help="The directory (and subdirectories) where we will search for malformed gcg files",
    )
):
    """Delete incomplete gcg files"""

    directories = [subdir for subdir, _, _ in os.walk(data_dir) if subdir != data_dir]

    for directory in directories:
        print("Looking for unfinished games in directory " + directory + "...")
        errorFiles = []
        for filename in os.listdir(directory):
            if filename.endswith(".gcg"):
                path = os.path.join(directory, filename)
                if not QuackleGame.is_finished_game(path):
                    errorFiles.append(path)

    if len(errorFiles) == 0:
        print("All good! No unfinished games found")
    else:
        print("ERROR FILES")
        for errorFile in errorFiles:
            print("\t" + errorFile)
        if input("Delete the files above? (Y/N)\n").lower() in ["yes", "y"]:
            for errorFile in errorFiles:
                os.unlink(errorFile)
            print("Deletion complete")
        else:
            print("Deletion cancelled")


@app.command()
def generate_csvs(
    data_dir: str = typer.Option(
        "data",
        "--data-dir",
        "-d",
        help="The directory where we will search for subdirectories and create a CSV file for those subdirectories",
    )
):
    """Generate CSV files for all games in a subdirectory"""

    directories = [subdir for subdir, _, _ in os.walk(data_dir) if subdir != data_dir]

    for directory in directories:
        print("Parsing games in directory " + directory + "...")
        games = [
            QuackleGame(os.path.join(directory, filename)).to_dict()
            for filename in os.listdir(directory)
            if filename.endswith(".gcg")
        ]
        df = pd.DataFrame(games)
        output_path = f"{directory}.csv"
        print(f"Creating {output_path}...")
        df.to_csv(output_path, index=False)


if __name__ == "__main__":
    app()
