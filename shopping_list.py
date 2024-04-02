shop_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shop_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shop_list:
    if item == "spam":
        continue
    print("Buy " + item)
