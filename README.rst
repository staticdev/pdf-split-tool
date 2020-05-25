
Pdf Split Tool
==============

|Tests| |Codecov| |PyPI| |Python Version| |Read the Docs| |License| |Black| |pre-commit| |Dependabot|

.. |Tests| image:: https://github.com/staticdev/pdf-split-tool/workflows/Tests/badge.svg
   :target: https://github.com/staticdev/pdf-split-tool/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/staticdev/pdf-split-tool/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/staticdev/pdf-split-tool
   :alt: Codecov
.. |PyPI| image:: https://img.shields.io/pypi/v/pdf-split-tool.svg
   :target: https://pypi.org/project/pdf-split-tool/
   :alt: PyPI
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/pdf-split-tool
   :target: https://pypi.org/project/pdf-split-tool
   :alt: Python Version
.. |Read the Docs| image:: https://readthedocs.org/projects/pdf-split-tool/badge/
   :target: https://pdf-split-tool.readthedocs.io/
   :alt: Read the Docs
.. |License| image:: https://img.shields.io/pypi/l/pdf-split-tool
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Dependabot| image:: https://api.dependabot.com/badges/status?host=github&repo=staticdev/pdf-split-tool
   :target: https://dependabot.com
   :alt: Dependabot


Features
--------

Split documents by size (20mb) (this is an experimental versio, soon there will be an option to choose the max size).


Requirements
------------

You need Python 3.8 or above installed on your machine.

Windows users should download `Windows x86-64 executable installer` and in the installer screen be ensure the option `Add Python 3.8 to PATH` is checked:

.. image:: docs/_images/winpath.png
   :alt: Windows Installation PATH checkbox


Installation
------------

You can install *Pdf Split Tool* via pip_ from PyPI_:

.. code:: console

   pip install pdf-split-tool

Note: on Windows you can copy the above command in the `cmd` program.


Usage
-----

1) Go to the directory with PDFs.
2) Execute the program with the command:

.. code:: console

   pdf-split-tool


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the MIT_ license,
*Pdf Split Tool* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.


.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _MIT: http://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/staticdev/pdf-split-tool/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
