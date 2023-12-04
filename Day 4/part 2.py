cards = [x for x in open("cards.txt").read().strip().split('\n')]
total = 0
multiplier = [1 for i in cards]
num_cards = 0

for i,card in enumerate(cards):
	winning = set([int(x) for x in card.split(":")[1].split("|")[0].strip().split()])
	have = [int(x) for x in card.split("|")[1].strip().split()]
	have = [x for x in have if x in winning]
	if len(have):
		total += 2**(len(have)-1)
	mult = multiplier[i]
	for j in range(i+1,min(i+len(have)+1,len(cards))):
		multiplier[j]+=mult
	num_cards += mult
	
print(num_cards)