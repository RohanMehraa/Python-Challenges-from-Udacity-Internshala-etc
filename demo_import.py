import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("\nScores : ", scores)
print("\nOriginal Mean : ", mean, "\nNew Mean : ", mean_c)

print("\n",__name__)
print("\n",uf.__name__)
