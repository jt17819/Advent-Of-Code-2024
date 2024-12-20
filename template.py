import os


day = input("Which day to create?: ")

if len(day) == 1:
    day = "0" + day


os.makedirs(os.path.dirname(f"Day {day}/solution1.py"), exist_ok=True)
os.makedirs(os.path.dirname(f"Day {day}/solution2.py"), exist_ok=True)
os.makedirs(os.path.dirname(f"Day {day}/data.txt"), exist_ok=True)

template = f"""import numpy as np

def main():
    with open("Day {day}/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day {day}/data.txt", dtype=str)
    print(data)

    return 

if __name__ == "__main__":
    print(main())

"""

with open(f"Day {day}/solution1.py", "a") as file:
    file.write(template)

with open(f"Day {day}/solution2.py", "a") as file:
    file.write(template)

with open(f"Day {day}/data.txt", "a") as file:
    pass
