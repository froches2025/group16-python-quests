# Quest 9: The Greedy Goblin
# Concept: The Modulo Operator (%) - This gives you the remainder of a division.

gold_pieces = 27
friends = 4

pieces_per_friend = gold_pieces // friends
goblin_keeps = gold_pieces % friends

print(f"Total gold pieces: {gold_pieces}")
print(f"Number of friends: {friends}")
print(f"Each friend gets: {pieces_per_friend} gold pieces")
print(f"The goblin keeps: {goblin_keeps} gold pieces")
