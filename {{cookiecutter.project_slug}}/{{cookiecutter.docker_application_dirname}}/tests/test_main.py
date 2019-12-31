"""
Test modules for:

{{ cookiecutter.py_modulename }}.__main__
"""

from click.testing import CliRunner

from {{ cookiecutter.py_modulename }}.__main__ import main


def test_main():
    """
    GIVEN the .__main__ module entry point WHEN calling main THEN the call
    executes successfully.
    """
    # Setup
    runner = CliRunner()
    # Exercise
    runner.invoke(main, [])
    # Verify
    assert result.exit_code == 0  # nosec
