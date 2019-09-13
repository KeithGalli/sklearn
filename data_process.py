import json
import random

data = []
file_name = 'Books'
with open(f'./data/{file_name}.json') as f:
	for line in f:
		review = json.loads(line)
		year = int(review['reviewTime'].split(' ')[-1])
		if year == 2014:
			data.append(review)

final_data = random.sample(data, 1000)

print(len(final_data))

print(final_data[0:5])

with open(f'./data/{file_name}_small.json', 'w') as f:
	for review in final_data:
		f.write(json.dumps(review)+'\n')