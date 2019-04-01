# A simple server based on Flask for IoT

1. Create an evironment and run virtual environment
    ```bash
    $ virtualenv venv
    $ source venv/bin/activate
    ```
1. Install required packages
    ```bash
    $ pip install -r requirements.txt
    ```
1. Run server
    ```bash
    $ export FLASK_APP=server
    $ export FLASK_DEBUG=1
    $ flask run
    ```