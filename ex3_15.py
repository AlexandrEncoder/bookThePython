cigarretDay = int(input("Number of cigarrete per day: "))
yearCigarret = int(input("How many years have you smoked? "))

# Here it happens the convert yers to day
yearDay =  (yearCigarret*365)
# Here calculated the lost day
mountCigarret = yearDay * cigarretDay

minuteLost = mountCigarret* 10
timeDeath = int(minuteLost / 1440)

print("You lost %d days"%timeDeath)

# here it is transformed  day in minute




