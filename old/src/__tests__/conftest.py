"""This is a configuration file for pytest.
Pytest looks for fixtures in the current test file and any `conftest.py` file in the current and parent directories
(cf https://docs.pytest.org/en/7.1.x/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files).

All my fixtures are organized per topic in the `src.__fixtures__` folder.
They must all be imported in this file so that they are made available for tests in this `src.__tests__` directory.
(As a consequence, there is no need to import fixtures in any of the test files).

Also, in this file these fixtures are imported but not used.
The `# noqa: F401` statement is here to ignore the `module imported but unused` errors (cf documentation to ignore
errors at https://flake8.pycqa.org/en/latest/user/violations.html#in-line-ignoring-errors and documentation about the
error codes at https://flake8.pycqa.org/en/2.5.5/warnings.html).
"""

from old.src.__fixtures__.autouse_fixtures import *  # noqa: F401
from old.src.__fixtures__.log_segment import *  # noqa: F401
