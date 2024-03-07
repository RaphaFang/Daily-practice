## return func. can call the function to stop
## return, can replace where the place func. is, and be the output of the original func.


# 1.____________________________________________________________
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1] 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

# 2.____________________________________________________________
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "Leap year"
      else:
        return "Not leap year"
    else:
      return "Leap year"
  else:
    return "Not leap year"
  
# TODO: Add more code here 👇
def days_in_month(a_year, a_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year) == "Leap year":
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month-1]
  else:
    return month_days[month-1]
  
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)


# 2.____________________________________________________________
# use """A""" below the def func. to indicate the detail of the func.
# have to be 3 "
# it's called documenting your func. 