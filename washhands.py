# Follow the instructions for what to code in this file.
table1 = [18.1, 15.4, 19.0, 13.4, 10.2,
          13.1, 18.1, 14.4, 15.0, 10.8, 5.4, 12.2]
table2 = [0.7, 0.0, 0.7, 1.0, 1.1, 0.4, 0.0, 1.0, 2.3, 2.9, 1.3]
avg_before = round(sum(table1)/len(table1), 1)
avg_after = round(sum(table2)/len(table2), 1)
print("Average mortality rate before hand washing policy:", avg_before)
print("Average mortality rate after hand washing policy:", avg_after)
