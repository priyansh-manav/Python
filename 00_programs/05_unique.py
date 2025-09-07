items = ["apple","banana","orange","apple","mango"]

unique_items = set()

for i in items:
    if i in unique_items:
        print(f"Duplicate : {i}")
        break
    unique_items.add(i)

print(unique_items)