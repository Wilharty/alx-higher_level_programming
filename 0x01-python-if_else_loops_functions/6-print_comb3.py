#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if i < j:
             if i + j != 17:
                  print(f"{i}{j}, ", end ="")
             else:
                  print(f"{i}{j}")
        else:
            continue
