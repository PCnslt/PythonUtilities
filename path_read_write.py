from pathlib import Path

p1 = Path('abc.txt')

# with open(p1,mode='r') as file:
#     print(file.read())

if p1.exists():
    with open(p1,mode='r') as file:
        print(file.read())
        file.close()

# if not p1.exists():
#     with open(p1,mode='w') as file:
#         file.write('Content 3')
#         file.close()
