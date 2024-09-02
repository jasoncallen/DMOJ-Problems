how_far = int(input())
if how_far == 1:
    this_far = ("A long time ago in a galaxy far away...")
else:
    this_far = ("A long time ago in a galaxy "+"far, "*(how_far - 1)+ "far away...")
print(this_far)