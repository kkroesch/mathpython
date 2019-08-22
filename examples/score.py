ranges = {
	"10": range(90,100),
	"9": range(80,89),
	"8": range(70,79),
	"7": range(60,69),
	"6": range(50,59),
	"5": range(40,49),
	"4": range(30,39),
	"3": range(20,29),
	"2": range(10,19),
	"1": range(1,9)
}

radius = 66.3

for score, range in ranges.iteritems():
    if round(radius) in range:
        print score
