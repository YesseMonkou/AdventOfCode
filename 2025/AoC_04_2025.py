def get_neighbours(x: int, y: int, x_max: int, y_max: int) -> list[tuple[int,int]]:
    coords: list[tuple[int,int]] = []
    
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx or dy:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= x_max and 0 <= ny <= y_max:
                    coords.append((nx, ny))
    return coords


def AoC_04_2025(datastream: list[list[str]]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0

    # Part 1
    for y, row in enumerate(datastream):
        for x, cel in enumerate(row):
            if cel == "@":
                coords: list[tuple[int,int]] = get_neighbours(x, y, len(row)-1, len(datastream)-1)
                paper_count: int = 0
                
                for coord in coords:
                    if datastream[coord[1]][coord[0]] == "@":
                        paper_count += 1
                
                antwoord1 += 1 if paper_count < 4 else 0
    
    # Part 2
    past_answer: int = -1
    
    while past_answer < antwoord2:
        past_answer = antwoord2
        
        for y, row in enumerate(datastream):
            for x, cel in enumerate(row):
                if cel == "@":
                    coords: list[tuple[int,int]] = get_neighbours(x, y, len(row)-1, len(datastream)-1)
                    paper_count: int = 0
                    
                    for coord in coords:
                        if datastream[coord[1]][coord[0]] == "@":
                            paper_count += 1
                    
                    if paper_count < 4:
                        antwoord2 += 1
                        datastream[y][x] = "."
    
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2025/AoC_04_2025.txt", "r") as fh:
        invoer: list[list[str]] = [list(regels.strip()) for regels in fh]

    print(AoC_04_2025(invoer))