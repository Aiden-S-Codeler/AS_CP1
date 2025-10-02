# AS 2nd multiplication table

table_list = []

for i in range(0, 13):
    for x in range(0, 13):
        table_list.append(i * x)
    print(table_list)
    table_list.clear()