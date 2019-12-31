"""
Test modules for:

{{ cookiecutter.py_modulename }}.__main__
"""

from click.testing import CliRunner
import pytest.mark

from {{ cookiecutter.py_modulename }}.__main__ import main


@pytest.mark.parametrize(
    "args", [
        ([],),
        (["invoke"],),
    ],
)
def test_main(args):
    """
    GIVEN the .__main__ module entry point WHEN calling main THEN the call
    executes successfully.
    """
    # Setup
    runner = CliRunner()
    # Exercise
    result = runner.invoke(main, args)
    # Verify
    assert result.exit_code == 0  # nosec
