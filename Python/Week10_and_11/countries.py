# Files 1.
# &
# Exceptions 1. Use the file "countries.txt".
# Catch min 2 differenr exceptions when reading or writing to the file.


try:
    # Add more countries and populations to the file.
    f = open("countries.txt", "a", encoding="utf8")
    f.write("Tonga,100651\n")
    f.write("Macau (China),682800\n")
    f.write("Nauru,10535")
    f.close
except FileNotFoundError as exc:
    print("Cannot open the file:",exc)
except PermissionError as exc:
    print("File is read only:",exc)

try:
    # Read a file that has countries and populations 
    f = open("countries.txt", "r", encoding="utf8")
    lines = f.readlines()
    stripped_lines = []
    for line in lines:
        # Remove possible whitespaces.
        line = line.strip()
        split_line = line.split(",")
        stripped_lines.append(split_line)
    # Search for the population of some given country.
    country = "Fiji"
    found = "Couldn't found country: " + country + " on this list"
    for i in range(len(stripped_lines)):
        if stripped_lines[i][0] == country:
            found = "Population of " + country + " is: " + stripped_lines[i][1]
    print(found)
    # Print the country that has the biggest population.
    biggest = 0
    for i in range(len(stripped_lines)):
        if int(stripped_lines[i][1]) > biggest:
            biggest = int(stripped_lines[i][1])
            country = stripped_lines[i][0]
    print("Biggest population of",biggest,"is in",country)      
    f.close
    # Remove possible whitespaces (from txt file)
    f = open("countries.txt", "w", encoding="utf8")
    for i in range(len(stripped_lines)):
        f.write(stripped_lines[i][0] + "," + stripped_lines[i][1] + "\n")
    f.close()

except FileNotFoundError as exc:
    print("Cannot open the file:",exc)

