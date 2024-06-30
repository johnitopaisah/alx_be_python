number = int(input("Enter a number to see its multiplication table: "))
for j in range(1, 11):
    # print(f"The multiplication table for {j} from (1 -> 10)")
    for i in range(1, number+1):
        print(f"{j} * {i} = {j * i}", end='\t')