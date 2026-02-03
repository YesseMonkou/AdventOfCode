def AoC_05_2025(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0

    # Part 1
    ranges: list[tuple[int,int]] = []
    switch: bool = False
    
    for row in datastream:
        if not switch and row != "":
            ranges.append(tuple(map(int, row.split("-"))))
            
        elif not switch and row == "":
            switch = True
            
        else:
            ingredient: int = int(row)
            
            for range_ in ranges:
                if range_[0] <= ingredient <= range_[1]:
                    antwoord1 += 1
                    break
    
    # Part 2            
    sorted_ranges = sorted(ranges)
    current_range: tuple[int,int] = (0,-1)
    
    for range_ in sorted_ranges:
        if range_[0] > current_range[1]:
            antwoord2 += current_range[1] - current_range[0] + 1
            current_range = range_
        else:
            current_range = (current_range[0], max(range_[1], current_range[1]))
    
    antwoord2 += current_range[1] - current_range[0] + 1
    
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2025/AoC_05_2025.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_05_2025(invoer))