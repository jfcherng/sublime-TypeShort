import re
from .settings import get_package_name


def msg(msg: str) -> str:
    """
    @brief Format the message for this plugin.

    @param msg The message

    @return The formatted message
    """

    return "[{name}] {msg}".format(name=get_package_name(), msg=msg)


def snake_to_camel(snake: str, upper_first: bool = False) -> str:
    # title-cased words
    words = [word.title() for word in snake.split("_")]

    if words and not upper_first:
        words[0] = words[0].lower()

    return "".join(words)


def camel_to_snake(camel: str) -> str:
    # first upper-cased camel
    camel = camel[0].upper() + camel[1:]

    return "_".join(re.findall(r"[A-Z][^A-Z]*", camel)).lower()
