# DLG REST API test: dlg-test-axelleysen

This is a bare-bones application providing a REST API, built using Flask, to sum a list of numbers.

The application is contained within the `sum_list.py` file with package requirements defined in `requirements.txt`.

`tests.py` runs some tests written for TDD.


## Install
    git clone git@github.com:axyleysen/dlg-test-axelleysen.git
    cd dlg-test-axelleysen
    git checkout aws-deployment


## Deploy

	sam package --resolve-s3 --output-template-file out.yaml
	sam deploy --template-file out.yaml --capabilities CAPABILITY_IAM --stack-name dlg-serverless

## Run the tests
    python3 tests.py


# Sample request

### Request

	curl -i https://4p49pw9rf3.execute-api.eu-west-2.amazonaws.com/?list=0,1,2,3,4

### Response

	HTTP/2 200 
	date: Wed, 11 Nov 2020 08:46:32 GMT
	content-type: application/json
	content-length: 13
	apigw-requestid: V1a0Wg-urPEEMqQ=

	{"total": 10}


# Assumptions
- Input list is a comma separated string
- Input list contains integer numbers and no fractional numbers 
- Input list may contain positive and negative integers 
