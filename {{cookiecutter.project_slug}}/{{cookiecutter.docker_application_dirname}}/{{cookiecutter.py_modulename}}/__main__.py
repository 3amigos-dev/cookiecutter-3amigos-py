"""
Module load handler for execution via:

python -m {{ cookiecutter.py_modulename }}
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


def main():
    """
    Test
    """
    print("""\
For more information view the online documentation at:
https://{{ cookiecutter.readthedocs_name }}.readthedocs.io/en/latest/
""")


if __name__ == '__main__':
    main()
