import os
import typer

from Quackle import QuackleGame

app = typer.Typer(name="Multiplicative Persistence Explorer", add_completion=False)



# Delete bad files
@app.command()
def clean(
    data_dir: str = typer.Option(
        "data",
        "--data-dir",
        "-d",
        help="The directory where the output JSON be written",
    )
):
    """Delete incomplete gcg files"""

    directories = [subdir for subdir,_,_ in os.walk(data_dir) if subdir != data_dir]

    for directory in directories:
        print('Looking for unfinished games in directory ' + directory + "...")
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
            print('\t' + errorFile)
        if input("Delete the files above? (Y/N)\n").lower() in ['yes', 'y']:
            for errorFile in errorFiles:
                os.unlink(errorFile)
            print("Deletion complete")
        else:
            print("Deletion cancelled")


# Generate CSV summary of all files in a directory

    
if __name__ == "__main__":
    app()
