# testRandom.py

#为啥random.random()生成的数越来越大，错觉
import random

def main():
    for i in range(5):
        temp = random.random()
        print(temp)

main()
