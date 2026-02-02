def calculation(bank: list[int], batteries: int) -> int:
    highest: list[list[str, int]] = [["",-1]]
    
    for joltage_length in range(batteries,0,-1):
        boundary: list[int] = [highest[-1][1]+1, len(bank)-joltage_length+1]
        
        maximum: int = max(bank[boundary[0]:boundary[1]])
        highest.append([str(maximum), bank.index(maximum, boundary[0], boundary[1])])
        
    joltage: str = "".join([x[0] for x in highest])
    
    return int(joltage)


def AoC_03_2025(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0
    
    for bank in datastream:
        bank: list[int] = list(map(int, list(bank)))
        antwoord1 += calculation(bank, 2)
        antwoord2 += calculation(bank, 12)

    return antwoord1,antwoord2


if __name__ == "__main__":
    with open("2025/AoC_03_2025.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_03_2025(invoer))