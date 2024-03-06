import sys
import pathlib
from bs4 import BeautifulSoup
import subprocess


def main(file_to_read: str) -> None:
    file_path = pathlib.Path(file_to_read)
    with file_path.open("r") as file:
        soup = BeautifulSoup(file, "html.parser")

    result = ""
    for command in soup.children:
        if command == "\n":
            continue
        result = result + "\n" + command.name
        for argument in command.children:
            if argument == "\n":
                continue
            result += " --" + argument.name
    result = result.strip()
    subprocess.run(result, shell=True, check=True)


if __name__ == "__main__":
    main(sys.argv[1])
