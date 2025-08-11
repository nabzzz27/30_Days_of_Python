#Declare an empty list
list = []
print(list)
print()

#Declare a list with more than 5 items
list = [1, 2, 3, 4, 5]
print(list)
print()

#Find the length of your list
print(len(list))
print()

#Get the first item, the middle item and the last item of the list
print(list[0], list[int(len(list)/2)], list[-1])
print()

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_type = ['Nabil', 24, 183.0, 'Taken', '530428']
print(mixed_data_type)
print()

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[int(len(it_companies)/2)], it_companies[-1])
print()

#Print the list after modifying one of the companies
i = it_companies.index('Facebook')
it_companies[i] = 'Meta'
print(it_companies)
print()

#Add an IT company to it_companies
it_companies.append('OpenAI')
print(it_companies)
print()

#Insert an IT company in the middle of the companies list
it_companies.insert(int(len(it_companies)/2), 'Samsung')
print(it_companies)
print()

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)
print()

#join the it_companies with a string '#;  '
new_it_companies = '#; '.join(it_companies)
print(new_it_companies)
print()

#Check if a certain company exists in the it_companies list.
print('Xiaomi' in it_companies)
print()

#Sort the list using sort() method
it_companies = sorted(it_companies)
print(it_companies)
print()

#Reverse the list in descending order using reverse() method
print(it_companies[::-1])
print()

#Slice out the first 3 companies from the list
print(it_companies)
print()
print(it_companies[3:])

#Slice out the middle IT company or companies from the list
print(it_companies[int(len(it_companies)/2)])
print()

#Remove the first IT company from the list
print(it_companies[1:])
print()

#join the lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
print()

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end.copy()
i = full_stack.index('Redux') + 1
full_stack[i:i] = ['Python', 'SQL']
print(full_stack)
print()

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))
print()

#Add the min age and the max age again to the list
ages.extend([min(ages), max(ages)])
print(ages)
print()

#Find the median age (one middle item or two middle items divided by two)
ages.sort()
length = len(ages)
if length % 2 == 0:
    median = (ages[int(length/2)] +  ages[int(length/2 + 1)]) / 2
    print(median)
else:
    median = ages[int(length/2)]
    print(median)


#Find the average age (sum of all items divided by their number
print()
avg = sum(ages) / len(ages)
print(avg)
print()

#Find the range of the ages (max minus min)
print(max(ages) - min(ages))
print()

#Compare the value of (min - average) and (max - average), use abs() method
min_avg = abs(min(ages) - avg)
print(min_avg)
max_avg = abs(max(ages) - avg)
print(max_avg)


#Find the middle country(ies)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
  
]

length = len(countries)

if length % 2 == 0:
    middle = [countries[int(length / 2)], countries[int(length / 2 + 1)]]
    print(middle) 
else:
    middle = countries[int(length / 2)]
    print(middle) 

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
if length % 2 == 0:
    first_half = countries[:int(length / 2)]
    second_half = countries[int(length / 2):]
    print(len(first_half), len(second_half))
else:
    first_half = countries[:int(length / 2) + 1]
    second_half = countries[int(length / 2):]
    print(len(first_half), len(second_half))

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic = countries
print(first, second, third, scandic)















