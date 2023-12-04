cards = [x for x in open("cards.txt").read().strip().split('\n')]
total = 0

for i,card in enumerate(cards):
	winning = set([int(x) for x in card.split(":")[1].split("|")[0].strip().split()])
	have = [int(x) for x in card.split("|")[1].strip().split()]
	have = [x for x in have if x in winning]
	if len(have):
		total += 2**(len(have)-1)

print(total)