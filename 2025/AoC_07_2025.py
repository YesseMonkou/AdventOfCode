def AoC_07_2025(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0
    
    for y, row in enumerate(datastream):
        if y == len(datastream) - 1:
            break
        
        for x, cel in enumerate(row):
            if cel == "S":
                if datastream[y+1][x] == ".":
                    datastream[y+1][x] = 1
            
            if type(cel) == int:
                if datastream[y+1][x] == ".":
                    datastream[y+1][x] = cel
                    
                elif datastream[y+1][x] == "^":
                    antwoord1 += 1
                    
                    if type(datastream[y+1][x-1]) == int:
                        datastream[y+1][x-1] += cel
                    else:
                        datastream[y+1][x-1] = cel
                    
                    if type(datastream[y+1][x+1]) == int:
                        datastream[y+1][x+1] += cel
                    else:
                        datastream[y+1][x+1] = cel
                
                else:
                    datastream[y+1][x] += cel
    
    for cel in datastream[-1]:
        if cel == ".":
            continue
        antwoord2 += cel
    
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2025/AoC_07_2025.txt", "r") as fh:
        invoer: list[str] = [list(regels.strip()) for regels in fh]

    print(AoC_07_2025(invoer))