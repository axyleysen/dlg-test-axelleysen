## Test bank
import requests

# Define api url
url = "https://4p49pw9rf3.execute-api.eu-west-2.amazonaws.com/?list="

# Initialise test logging variables
tests = 0
successfulTests = 0

# Defining tests 
test_inputs = [
	{
	'numbers_to_add': list(range(10)),
	'expected_result': 45
	},
	{
	'numbers_to_add': [2,3],
	'expected_result': 5
	},
	{
	'numbers_to_add': [1,3],
	'expected_result': 4
	},
	{
	'numbers_to_add': [-1,3],
	'expected_result': 2
	},
	{
	'numbers_to_add': [1,-3],
	'expected_result': -2
	}
]


# Loop through tests
for test in test_inputs:
	# Iterate loop
	tests += 1
	print("\033[1mTest #%s started\033[0m" % tests)

	# Get respose from local rest api
	response = requests.get("%s%s" % (url, ",".join(map(str, test['numbers_to_add']))))
	returned_result = response.json()['total']

	# Print results out to console
	print("Return result:\n%s" % returned_result)
	print("Expected result:\n%s" % test['expected_result'])

	# Check for success in results
	if test['expected_result'] == returned_result:
		successfulTests += 1
		print('Test #%s successful\n' % tests)
	else:
		print('Test #%s failed\n' % tests)

# Display aggregated test results
print("\033[1m%s/%s tests succeeded\033[0m" % (successfulTests,tests))
