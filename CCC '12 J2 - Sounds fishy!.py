original_depths = []
fish = False
for _ in range(4):
    original_depths.append(int(input()))

if original_depths[0] < original_depths[1]:
    if original_depths[1] < original_depths[2]:
        if original_depths[2] < original_depths[3]:
            print("Fish Rising")
            fish = True

if original_depths[0] > original_depths[1]:
    if original_depths[1] > original_depths[2]:
        if original_depths[2] > original_depths[3]:
            print("Fish Diving")
            fish = True

if original_depths[0] == original_depths[1]:
    if original_depths[1] == original_depths[2]:
        if original_depths[2] == original_depths[3]:
            print("Fish At Constant Depth")
            fish = True

if fish == False:
    print("No Fish")
