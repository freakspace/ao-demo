# Click and Collect

This is a demo project for a click and collect webapp


### Prerequisites:

1. Python 3.8 or newer.
2. `pip` for managing Python packages.

### Installation

1. Clone the repository to your local machine:
    ```bash
    git clone git@github.com:freakspace/ao-demo.git
    cd ao-demo
    ```

2. Install the required Python packages:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

### Prepare the webapp

    ```bash
        cd clickcollect

        python manage.py migrate

        python manage.py add_data
        ```


### Start the webapp

    ```bash
        python manage.py run server
        ```

