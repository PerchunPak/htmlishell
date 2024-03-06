import pathlib
import subprocess
import sys

from htmlishell.parsing import Parser


def main(file_to_read: str) -> None:
    file_path = pathlib.Path(file_to_read)
    result = Parser.parse(file_path.read_text())
    subprocess.run(result, shell=True, check=True)


if __name__ == "__main__":
    main(sys.argv[1])
