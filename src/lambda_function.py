import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
	"""Return the sum of a list of numbers.

	Argument -- [String] Comma separated integers
	Response -- [Json]:
	{
		"total": int
	}

	"""
	logging.info("Incoming event: %s" % event)
	numbers_to_add = event['queryStringParameters']['list']

	# Converting api inputs into list
	list_to_add = [int(item) for item in numbers_to_add.split(",")]
	total = sum(list_to_add)

	# Return response as json object
	logging.info("Total output: %s" % total)
	return {"total": total}

