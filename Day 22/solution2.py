import numpy as np


def main():
    # with open("Day 22/data.txt", "r") as file:
    #     data = file.read().split("\n")
    data = np.loadtxt("Day 22/data.txt", dtype=int)
    # print(data)

    interations = range(2000 - 1)
    seqs = {}
    for num in data:
        prices = [(num % 10, None)]
        price_seqs = set()
        for i in interations:
            num ^= (num << 6)
            num &= 16777215
            num ^= (num >> 5)
            num &= 16777215
            num ^= (num << 11)
            num &= 16777215
            
            price = num % 10
            prices.append((price, price - prices[i][0]))

            if i >= 3:
                price_seq = tuple(prices[j][1] for j in range(i - 2, i + 2))
                if price_seq not in price_seqs:
                    price_seqs.add(price_seq)
                    seqs[price_seq] = seqs.get(price_seq, []) + [price]

    return max(sum(seq) for seq in seqs.values())


if __name__ == "__main__":
    print(main())
