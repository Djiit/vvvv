# vvvv

[![Build Status](https://travis-ci.org/Djiit/vvvv.svg)](https://travis-ci.org/Djiit/vvvv)
[![PyPI](https://img.shields.io/pypi/v/vvvv.svg)](https://pypi.python.org/pypi/vvvv)

## About

Minimal vvvv Python OSC client. Compatible with **Python 3.4+**

## Quick start

Install **vvvv** with pip :

```bash
pip install vvvv
```

Use the VVVVClient in your project and start sending OSC messages to vvvv :

```python
>>> from vvvv import VVVVClient
>>> vc = VVVVClient('127.0.0.1', '4444')
>>> vc.send_msg('/filter', [0,255,255])
```

See more :

* vvvv: http://vvvv.org/
* OSC: http://opensoundcontrol.org/

## License

See [LICENSE](./LICENSE)
