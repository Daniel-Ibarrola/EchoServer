# Echo Server

## Developing

Uses python 3.12. To install open a terminal and run the following commands:

```shell
git clone git@github.com:Daniel-Ibarrola/EchoServer.git
cd EchoServer
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements/dev.txt
pip install -e .
```

Run the tests with pytest

```shell
pytest tests
```
