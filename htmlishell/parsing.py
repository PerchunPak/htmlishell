from bs4 import BeautifulSoup
from bs4.element import Tag


class Parser:
    def __init__(self, soup: BeautifulSoup) -> None:
        self.soup = soup

    @classmethod
    def parse(cls, as_string: str) -> str:
        soup = BeautifulSoup(as_string, "html.parser")
        self = cls(soup)

        result = ""
        for command in soup.children:
            if command == "\n":
                continue
            result += self._parse_command(command)
            for argument in command.children:
                if argument == "\n":
                    continue
                result += self._parse_argument(argument)

        return result.strip()

    def _parse_command(self, command: Tag) -> str:
        return "\n" + command.name  # type: ignore[no-any-return] # lol idc

    def _parse_argument(self, argument: Tag) -> str:
        if argument.get_attribute_list("short")[0] == "true":
            return " -" + argument.name  # type: ignore[no-any-return] # lol idc
        return " --" + argument.name  # type: ignore[no-any-return] # lol idc
