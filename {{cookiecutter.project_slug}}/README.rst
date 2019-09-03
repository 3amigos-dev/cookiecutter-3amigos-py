====================================
{{ cookiecutter.project_long_name }}
====================================

.. image:: https://dev.azure.com/AnthonyShaw/pytest-azurepipelines/_apis/build/status/tonybaloney.pytest-azurepipelines?branchName=master
   :target: https://dev.azure.com/AnthonyShaw/pytest-azurepipelines/_build/latest?definitionId=3?branchName=master
   :alt: Build status


.. image:: {{ cookiecutter.build_status_url }}
   :target: {{ cookiecutter.build_url }}
   :alt: Azure Status

.. image:: {{ cookiecutter.travis_status_url }}
   :target: {{ cookiecutter.travis_build_url }}
   :alt: Travis Status

.. image:: {{ cookiecutter.appveyor_status_url }}
   :target: {{ cookiecutter.appveyor_build_url }}
   :alt: Appveyor Status

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.pypi_name }}.svg
   :target: https://pypi.org/project/{{ cookiecutter.pypi_name }}
   :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.pypi_name }}.svg
   :target: https://pypi.org/project/{{ cookiecutter.pypi_name }}
   :alt: Python Versions

.. image:: https://img.shields.io/pypi/dm/{{ cookiecutter.pypi_name }}.svg
   :target: https://pypi.org/project/{{ cookiecutter.pypi_name }}
   :alt: PyPI downloads per month

.. image:: https://readthedocs.org/projects/{{ cookiecutter.readthedocs_name }}/badge/?version=latest
   :target: https://{{ cookiecutter.readthedocs_name }}.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/{{ cookiecutter.github_org }}/{{ cookiecutter.github_repo }}/badge.svg
   :target: https://coveralls.io/github/{{ cookiecutter.github_org }}/{{ cookiecutter.github_repo }}/
   :alt: Coverage Status

.. image:: https://camo.githubusercontent.com/28a51fe3a2c05048d8ca8ecd039d6b1619037326/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667
   :target: https://github.com/psf/black
   :alt: Black

{{ cookiecutter.project_long_description }}

More details can be found in the
`Online Documentation`_.

============
Installation
============

You can install {{ cookiecutter.project_slug }} for
`Python`_ via `pip`_ from `PyPI`_.

.. code-block:: bash

    pip install {{ cookiecutter.pypi_name }}

{{ cookiecutter.installation_notes }}

{% if cookiecutter.app_requirements %}
=============
Prerequisites
=============
- {{ cookiecutter.app_requirements|replace('\n', '\n- ') }}
{% endif %}

======================
Download from PyPI.org
======================

https://pypi.org/project/{{ cookiecutter.pypi_name }}/

{{ cookiecutter.extended_readme }}

============
Contributing
============

Contributions are very welcome, consider using the
`file an issue`_
to discuss the work before beginning, but if you already have a Pull Request
ready then this is no problem, please submit it and it will be very gratefully
considered. The `Contribution Guidelines`_
outlines the {{ cookiecutter.community_name }} commitment to ensuring all
contributions receive appropriate recognition.

=======
License
=======

{% if cookiecutter.license == 'GPLv3+' %}
Distributed under the terms of the `GPLv3`_
license, "{{ cookiecutter.project_name }}" is free and open source software
{% elif cookiecutter.license == 'MIT' %}
Distributed under the terms of the `MIT`_
license, "{{ cookiecutter.project_name }}" is free and open source software
{% endif %}

======
Issues
======

If you encounter any problems, please
`file an issue`_
along with a detailed description.

========================
Additional Documentation
========================

- `Online Documentation`
- `News`_
- `Template Updates`_
- `Code of Conduct`_
- `Contribution Guidelines`_

.. _`Online Documentation`: https://{{ cookiecutter.readthedocs_name }}.readthedocs.io/en/latest/
.. _`News`: NEWS.rst
.. _`Template Updates`: COOKIECUTTER_UPDATES.md
.. _`Code of Conduct`: CODE_OF_CONDUCT.md
.. _`Contribution Guidelines`: CONTRIBUTING.md
.. _`Python`: https://www.python.org/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/
.. _`file an issue`: https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.github_repo }}/issues)
{% if cookiecutter.license == 'GPLv3+' %}.. _`GPLv3`: https://opensource.org/licenses/GPL-3.0
{% elif cookiecutter.license == 'MIT' %}.. _`MIT`: http://opensource.org/licenses/MIT
{% endif %}

