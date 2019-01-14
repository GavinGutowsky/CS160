enter = input("Enter a list of numbers seperated by spaces: ");
five = list(map(int,enter.split(' ')));

max = five[0];

for x in five:
   if x > max:
      max = x;

print ("The largest number you inputed is "+str(max));
