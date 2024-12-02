list1: list[int] = list()
list2: list[int] = list()
with open('data-real.txt') as file:
    for line in file:
        value1, value2 = line.strip().split('   ')
        list1.append(int(value1))
        list2.append(int(value2))

sorted1: list[int] = sorted(list1)
sorted2: list[int] = sorted(list2)

total_distance: int = sum(abs(a - b) for a, b in zip(sorted1, sorted2))
print(f"Total distance: {total_distance}")
assert total_distance == 1110981

similarity_score: int = sum(value * sorted2.count(value) for value in sorted1)
print(f"Similarity score: {similarity_score}")
assert similarity_score == 24869388