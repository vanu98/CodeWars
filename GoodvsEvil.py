def goodVsEvil(good,evil):
	b = []
	sum_good=0
	good_list = good.split(' ')
	[b.append(int(i)) for i in good_list]

	sum_good = b[0]*1
	sum_good+=b[1]*2
	sum_good+=b[2]*3
	sum_good+=b[3]*3
	sum_good+=b[4]*4
	sum_good+=b[5]*10

	c =[]
	sum_evil = 0
	evil_list = evil.split(' ')
	[c.append(int(i)) for i in evil_list]

	sum_evil = c[0]*1
	sum_evil+=c[1]*2
	sum_evil+=c[2]*2
	sum_evil+=c[3]*2
	sum_evil+=c[4]*3
	sum_evil+=c[5]*5
	sum_evil+=c[6]*10

	if(sum_good>sum_evil):
		return 'Battle Result: Good triumphs over Evil'
	if(sum_evil>sum_good):
		return 'Battle Result: Evil eradicates all trace of Good'
	if(sum_evil==sum_good):
		return 'Battle Result: No victor on this battle field'
goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')