# Option 1 -- manually check if the key exists
def count(string):
  counts = {}
  for s in string:
    if s in counts.keys():
      counts[s] += 1
    else:
      counts[s] = 1
  return counts

# Option 2 -- use setdefault to ensure the key exists
def count(string):
  counts = {}
  for s in string:
    counts.setdefault(s, 0)
    counts[s] += 1
  return counts

# Option 3 - initiate counts with the letters from the string and set to zero
def count(string):
    counts = dict.fromkeys(set(list(string)), 0)
    for s in string:
      count[s] += 1
  return counts

print(count("hello") == {"h": 1, "e": 1, "l": 2, "o": 1})