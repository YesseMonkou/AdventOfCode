def modify_input(datastream: list[str]) -> list[list[int]]:
    new_list: list[list[int]] = []
    for ranges in datastream[0].split(","):
        if ranges:
            new_list.append(list(map(int, ranges.split("-"))))
    
    return new_list
        

def AoC_02_2025(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0
    
    datastream: list[list[str]] = modify_input(datastream)
    length_string: int = 0
    dividers = []
    
    for ranges in datastream:
        for id in range(ranges[0], ranges[1]+1):
            id_string: str = str(id)
            if int(len(id_string)) != length_string:
                length_string: int = int(len(id_string))
                dividers = [i for i in range(1, length_string + 1) if length_string % i == 0]
                dividers = dividers[:-1]
            
            for distance in dividers:
                string_parts: list[str] = []
                for i in range(distance,length_string+distance,distance):
                    string_parts.append(id_string[i-distance:i])
                    
                if all(x==string_parts[0] for x in string_parts):
                    antwoord2 += id
                    break
                    
            left: str = id_string[:length_string//2]
            right: str = id_string[length_string//2:]
            
            if left == right:
                antwoord1 += id
    

    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2025/AoC_02_2025.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_02_2025(invoer))