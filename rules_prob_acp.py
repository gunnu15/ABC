def prob_a_or_b(event_a, event_b, sample_space):
    union = event_a.union(event_b)
    prob = len(union) / len(sample_space)
    return prob

evens = {2, 4, 6}
greater_than_two = {3, 4, 5, 6}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

print("Probability of getting an even number or a number greater than two:")
print(prob_a_or_b(evens, greater_than_two, all_possible_rolls))