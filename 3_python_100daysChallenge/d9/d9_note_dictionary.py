## dictionaries & nesting

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}
# print(programming_dictionary["Bug"])

# add item
programming_dictionary["Loop"]= "the action of doing something over and over again"
# print(programming_dictionary["Loop"])

# print the whole dictionary
print(programming_dictionary)

# wipe the dictionary, and you could redefine the same "key"
programming_dictionary = {}

# using for loop print out dic. will get key only. 
for thing in programming_dictionary:
    print(thing)
# if you want to get the key and its value, do this
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])


# 1.____________________________________________________________
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for thing in student_scores:
  if student_scores[thing] >= 91:
    student_grades[thing] = "Outstanding"
  elif student_scores[thing] >= 81 and student_scores[thing] <= 90:
    student_grades[thing] = "Exceeds Expectations"
  elif student_scores[thing] >= 71 and student_scores[thing] <= 80:
    student_grades[thing] = "Acceptable"
  else:
    student_grades[thing] = "Fail"

print(student_grades)

## you don't need to add the "" in the for loop []

# 2.____________________________________________________________ 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists
travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

# 3.____________________________________________________________
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Your code here 👇
def add_new_country(name, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")