# Simple URL Shortener in Python (with DRF)

## Usage

### Installation

Tested on Python 3.10

```
pip3 install -r requirements.txt
```

### Running

Run with manage.py script
```
python manage.py runserver
```

### Handling DB migrations
Run
```commandline
python manage.py migrate
```

### Available endpoints

* / -> Handles a POST request, with application/json body and a "url" param, e.g.:

```
{
    "url": "https://google.com"
}
```
Returns 400 if the request body is malformed.

* /<shortened> -> Redirects to full URL corresponding to given shortened URL, if no full URL is found returns 404.