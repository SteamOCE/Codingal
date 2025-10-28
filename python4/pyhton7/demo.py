abc = ('mike', 'ronaldo', 'messi', 'neymar', 'salah')

print(abc)

# abc[0] = 'tom'  This will raise an error because tuples are immutable
# abc.append('jack')
# abc.add('harry')

for frnd in abc:
    print(frnd)

# sets: unordered and unindexed collection of items. No duplicate members.
xyz = {'mike', 'mike', 'ronaldo', 'messi', 'ronaldo', 'neymar', 'messi', 'salah'}

print(xyz)  # Duplicates will be removed in sets

xyz.add('jack')

for frnd in xyz:
    print(frnd)

print(len(xyz))

# print(xyz[0])  This will raise an error because sets are unindexed
