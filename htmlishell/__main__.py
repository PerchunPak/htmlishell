import pathlib
import subprocess
import sys
import typing as t

from htmlishell.parsing import Parser


def main(file_to_read: t.Optional[str] = None) -> None:
    if file_to_read is None:
        try:
            file_to_read = sys.argv[1]
        except IndexError:
            print("Please provide file to read from!")
            return

    file_path = pathlib.Path(file_to_read)
    result = Parser.parse(file_path.read_text())
    subprocess.run(result, shell=True, check=True)


if __name__ == "__main__":
    main()
