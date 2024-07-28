# Click and Collect

This is a demo project for a click and collect webapp


### Prerequisites:

1. Python 3.8 or newer.
2. `pip` for managing Python packages.

### Installation

1. Clone the repository to your local machine:
```
git clone git@github.com:freakspace/ao-demo.git
```

```
cd ao-demo
```

2. Install the required Python packages:
```
python -m venv venv
```

```
source venv/bin/activate
```

```
pip install -r requirements.txt
```

### Prepare the webapp
```
cd clickcollect
```

```
python manage.py migrate
```

```
python manage.py add_test_data
```


### Start the webapp
```
python manage.py runserver
```

