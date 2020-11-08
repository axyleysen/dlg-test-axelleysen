## Test bank


# Initialise test logging variables
tests = 0
successfulTests = 0

# Defining tests 
test_inputs = [
	{
	'numbers_to_add': list(range(10000001)),
	'expected_result': 50000015000001
	},
	{
	'numbers_to_add': [2,3],
	'expected_result': 6
	}
]


# Loop through tests
for test in test_inputs:
	tests += 1
	print('\nTest #%s started' % tests)
	returned_result = "Error"
	print("Return result:\n%s" % returned_result)
	print("Expected result:\n%s" % test['expected_result'])
	if test['expected_result'] == returned_result:
		successfulTests += 1
		print('Test #%s successful' % tests)
	else:
		print('Test #%s failed' % tests)


print("\n%s/%s tests succeeded" % (successfulTests,tests))
