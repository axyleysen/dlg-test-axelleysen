# DLG REST API test: dlg-test-axelleysen

This is a bare-bones application providing a REST API, built using Flask, to sum a list of numbers.

The application is contained within the `sum_list.py` file with package requirements defined in `requirements.txt`.

`tests.py` runs some tests written for TDD.


## Install
    git clone git@github.com:axyleysen/dlg-test-axelleysen.git
    cd dlg-test-axelleysen
    pip3 install -r requirements.txt


## Run the app
    python3 sum_list.py


## Run the tests (Run command in another terminal window)
    python3 tests.py


# Sample request

### Request

	curl -i http://localhost:5000/total/0,1,2,3,4

### Response

	HTTP/1.0 200 OK
	Content-Type: application/json
	Content-Length: 18
	Server: Werkzeug/1.0.1 Python/3.7.1
	Date: Mon, 09 Nov 2020 11:01:44 GMT

	{
	  "total": 10
	}


# Assumptions
- Input list is a comma separated string
- Input list contains integer numbers and no fractional numbers 
- Input list may contain positive and negative integers 
