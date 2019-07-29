# {{ cookiecutter.project_long_name }}

[![Azure Status]({{ cookiecutter.build_status_url }})]({{ cookiecutter.build_url }})
[![Travis Status]({{ cookiecutter.travis_status_url }})]({{ cookiecutter.travis_build_url }})
[![Appveyor Status]({{ cookiecutter.appveyor_status_url }})]({{ cookiecutter.appveyor_build_url }})
[![PyPI version](https://img.shields.io/pypi/v/{{ cookiecutter.pypi_name }}.svg)](https://pypi.org/project/{{ cookiecutter.pypi_name }})
[![Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.pypi_name }}.svg)](https://pypi.org/project/{{ cookiecutter.pypi_name }})
[![PyPI downloads per month](https://img.shields.io/pypi/dm/{{ cookiecutter.pypi_name }}.svg)](https://pypi.org/project/{{ cookiecutter.pypi_name }})
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.readthedocs_name }}/badge/?version=latest)](https://{{ cookiecutter.readthedocs_name }}.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/{{ cookiecutter.github_org }}/{{ cookiecutter.github_repo }}/badge.svg)](https://coveralls.io/github/{{ cookiecutter.github_org }}/{{ cookiecutter.github_repo }}/)

{{ cookiecutter.project_long_description }}

# Installation

You can install {{ cookiecutter.project_slug }} for
[Python](https://www.python.org/) via
[pip](https://pypi.org/project/pip/)
from [PyPI](https://pypi.org/).

```
$ pip install {{ cookiecutter.pypi_name }}
```

{{ cookiecutter.installation_notes }}

{% if cookiecutter.app_requirements %}
## Prerequisites:
- {{ cookiecutter.app_requirements|replace('\n', '\n- ') }}
{% endif %}

## Download from PyPI.org

https://pypi.org/project/{{ cookiecutter.pypi_name }}/

{{ cookiecutter.extended_readme }}

# Contributing

Contributions are very welcome, consider using the
[file an issue](https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.github_repo }}/issues)
to discuss the work before beginning, but if you already have a Pull Request
ready then this is no problem, please submit it and it will be very gratefully
considered. The [Contribution Guidelines](CONTRIBUTING.md)
outlines the {{ cookiecutter.community_name }} commitment to ensuring all
contributions receive appropriate recognition.

# License

{% if cookiecutter.license == 'GPLv3+' %}
Distributed under the terms of the [GPLv3](https://opensource.org/licenses/GPL-3.0)
license, "{{ cookiecutter.project_name }}" is free and open source software
{% elif cookiecutter.license == 'MIT' %}
Distributed under the terms of the [MIT](http://opensource.org/licenses/MIT)
license, "{{ cookiecutter.project_name }}" is free and open source software
{% endif %}

# Issues

If you encounter any problems, please
[file an issue](https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.github_repo }}/issues)
along with a detailed description.

# Additional Documentation:

* [Online Documentation](https://{{ cookiecutter.readthedocs_name }}.readthedocs.io/en/latest/)
* [News](NEWS.rst).
* [Template Updates](COOKIECUTTER_UPDATES.md).
* [Code of Conduct](CODE_OF_CONDUCT.md).
* [Contribution Guidelines](CONTRIBUTING.md).
