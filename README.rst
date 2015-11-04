vvvv
====

|Build Status| |Build Status2| |Build Status3| |Coverage Status| |PyPI| 

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
.. |PyPI| image:: https://img.shields.io/pypi/v/vvvv.svg
   :target: https://pypi.python.org/pypi/vvvv
.. |Coverage Status| image:: https://coveralls.io/repos/Djiit/vvvv/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/Djiit/vvvv?branch=master
