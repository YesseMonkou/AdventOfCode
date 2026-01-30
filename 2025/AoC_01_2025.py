def AoC_01_2025(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0
    
    position: int = 50
    
    for instruction in datastream:
        direction: str = instruction[0]
        steps: int = int(instruction[1:])

        if direction == "L":
            position -= steps
            tracked = [i for i in range(position + steps, position, -1) if i % 100 == 0]
        
            
        if direction == "R":
            position += steps
            tracked = [i for i in range(position - steps, position, 1) if i % 100 == 0]
        
        if position % 100 == 0:
            antwoord1 += 1
        
        antwoord2 += len(tracked)
            
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2025/AoC_01_2025.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_01_2025(invoer))