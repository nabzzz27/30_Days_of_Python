# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(len(it_companies))
print()

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
print()

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['Samsung', 'Xiaomi'])
print(it_companies)
print()

#Remove one of the companies from the set it_companies
it_companies.remove('Apple')
print(it_companies)
print()

#What is the difference between remove and discard
#remove will provide key error if that item is missing, discard will not

#Join A and B
C = A.union(B)
print(C)

#Find A intersection B
print(A.intersection(B))

#Is A subset of B
print(A.issubset(B))

#Are A and B disjoint sets
print(A.isdisjoint(B))

#Join A with B and B with A
print(A | B)

#What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#Delete the sets completely
del A
del B
print()

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(len(age), len(age_set))

#Explain the difference between the following data types: string, list, tuple and set
#string is iterable characters
#list is iterable items of any datatype
#tuple is immutable list
#set is a list of disctint items in a random order


#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
string = 'I am a teacher and I love to inspire and teach people.'
string = string.strip('.').split(' ')
print(string)
print(len(set(string)))