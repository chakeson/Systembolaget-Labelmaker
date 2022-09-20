import sys, os


def resource_path(relative_path):  # for pyinstaller to work with extra files
    try:
        base_path = sys._MEIPASS  # pylint: disable=no-member
    except Exception:
        base_path = os.path.dirname(__file__)
        # base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
