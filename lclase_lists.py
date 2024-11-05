# mix = [1, "dos", True, [1,2,3]]
# print (mix)
# print (len(mix))
# print("ultimo elemento", mix[-1])
# print(mix[:2])
# mix.append(False)
# print (mix)
# mix.insert(2, 2)
# print (mix)
numbers = [4, 23, 54, 1, 4.2, 0.8]
print("Mayor:", max(numbers))
print("Menor:", min(numbers))
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
