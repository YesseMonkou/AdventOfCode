def check_coords(original: list, test: list) -> bool:
    checks: list = [False, False]
    
    if original[2] == "+":
        if original[0] <= test[0]:
            checks[0] = True
    else:
        if original[0] >= test[0]:
            checks[0] = True
    if original[3] == "+":
        if original[1] <= test[1]:
            checks[1] = True
    else:
        if original[1] >= test[1]:
            checks[1] = True
    
    if False not in checks:
        return True
    else:
        return False

def AoC_09_2025(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0

    for x in range(len(datastream)):
        for y in range(x+1, len(datastream)):
            coords1: list = list(map(int,datastream[x].split(",")))
            coords2: list = list(map(int,datastream[y].split(",")))
            
            if coords1[0] == coords2[0] or coords1[1] == coords2[1]:
                continue
            
            area = (abs(coords1[0]-coords2[0])+1)*(abs(coords1[1]-coords2[1])+1)
            
            if area == max(antwoord1, area):
                antwoord1 = area
            if antwoord2 == max(antwoord2, area):
                continue
            
            coords3: list = [coords1[0], coords2[1]]
            coords4: list = [coords2[0], coords1[1]]
            
            if coords3[0] > coords4[0]:
                coords3.append("+")
                coords4.append("-")
            else:
                coords3.append("-")
                coords4.append("+")
                
            if coords3[1] > coords4[1]:
                coords3.append("+")
                coords4.append("-")
            else:
                coords3.append("-")
                coords4.append("+")
            
            corner_check: list = [False, False]
            
            for ranges in datastream:
                coords: list = list(map(int,ranges.split(",")))
                if check_coords(coords3, coords):
                    corner_check[0] = True
                if check_coords(coords4, coords):
                    corner_check[1] = True
                
                if False not in corner_check:
                    antwoord2 = area
                    break
                    
                
    
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2025/AoC_09_2025.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_09_2025(invoer))