# AA = [15, "aa", 16]
# print(AA)

# actuallist = ''
# for n in AA:
#     actuallist = actuallist +str(n)
# print (actuallist)


travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
country = input("which")
print(travel_log[country])