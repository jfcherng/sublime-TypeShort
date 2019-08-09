import sublime
import time


def get_package_name() -> str:
    return __package__


def get_package_path() -> str:
    return "Packages/" + get_package_name()


def get_settings_file() -> str:
    return "TypeShort.sublime-settings"


def get_settings_object() -> sublime.Settings:
    return sublime.load_settings(get_settings_file())


def get_setting(key: str, default=None):
    return get_settings_object().get(key, default)


def get_timestamp() -> float:
    return time.time()