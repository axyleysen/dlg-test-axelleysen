## Test bank
import requests

# Define api url
url = "http://localhost:5000/total/"

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
	print('\nTest #%s started' % tests)

	# Get respose from local rest api
	response = requests.get("%s%s" % (url, ",".join(map(str, test['numbers_to_add']))))
	returned_result = response.json()['total']

	# Print results out to console
	print("Return result:\n%s" % returned_result)
	print("Expected result:\n%s" % test['expected_result'])

	# Check for success in results
	if test['expected_result'] == returned_result:
		successfulTests += 1
		print('Test #%s successful' % tests)
	else:
		print('Test #%s failed' % tests)

# Display aggregated test results
print("\n%s/%s tests succeeded" % (successfulTests,tests))
