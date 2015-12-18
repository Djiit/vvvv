vvvv
====

|Build Status| |Build Status2| |Build Status3| |Build Status4| |Coveralls Status| |Codecov Status| |PyPI| |RequiresIO|

About
-----

Minimal vvvv Python OSC client. Compatible with **Python 3.4+**

Quick start
-----------

Install **vvvv** with pip :

.. code:: bash

    pip install vvvv

Use the VVVVClient in your project and start sending OSC messages to
vvvv :

.. code:: python

    >>> from vvvv import VVVVClient
    >>> vc = VVVVClient('127.0.0.1', '4444')
    >>> vc.send_msg('/filter', [0,255,255])

See more :

-  vvvv: http://vvvv.org/
-  OSC: http://opensoundcontrol.org/

License
-------

See `LICENSE <./LICENSE>`__

.. |Build Status| image:: https://travis-ci.org/Djiit/vvvv.svg
   :target: https://travis-ci.org/Djiit/vvvv
.. |Build Status2| image:: https://drone.io/github.com/Djiit/vvvv/status.png
   :target: https://drone.io/github.com/Djiit/vvvv/latest
.. |Build Status3| image:: https://circleci.com/gh/Djiit/vvvv/tree/master.svg?style=svg
   :target: https://circleci.com/gh/Djiit/vvvv/tree/master
.. |Build Status4| image:: https://codeship.com/projects/f2285bc0-69c2-0133-a6e2-6e257542035e/status?branch=master
   :target: https://codeship.com/projects/114635
.. |PyPI| image:: https://img.shields.io/pypi/v/vvvv.svg
   :target: https://pypi.python.org/pypi/vvvv
.. |Coveralls Status| image:: https://coveralls.io/repos/Djiit/vvvv/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/Djiit/vvvv?branch=master
.. |Codecov Status| image:: https://codecov.io/github/Djiit/vvvv/coverage.svg?branch=master
   :target: https://codecov.io/github/Djiit/vvvv?branch=master
.. |RequiresIO| image:: https://requires.io/github/Djiit/vvvv/requirements.svg?branch=master
   :target: https://requires.io/github/Djiit/vvvv/requirements/?branch=master
