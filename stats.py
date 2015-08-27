def mean(vals):
	total = sum(vals)
	length = len(vals)
	return float(total)/length

print mean([2,4,4,532])


def std(vals):
	if len(vals) == 0:
		return 0.0
	return vals[-1]/2.0

