data = int(input())
for _ in range(data):
    subjects = []
    verbs = []
    objects_list = []
    num_of_subjects = int(input())
    num_of_verbs = int(input())
    num_of_objects = int(input())
    for _ in range(num_of_subjects):
        subjects.append(input().strip())
    for _ in range(num_of_verbs):
        verbs.append(input().strip())
    for _ in range(num_of_objects):
        objects_list.append(input().strip())
    
    for s in subjects:
        for v in verbs:
            for o in objects_list:
                print(s+" "+v+" "+o+".")
