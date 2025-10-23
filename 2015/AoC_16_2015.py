def extract(data: str) -> tuple[int, dict]:
    splitted: list[str] = data.split(" ")
    id: int = int(splitted[1][:-1])
    compounds: dict = {
        splitted[2][:-1]: int(splitted[3][:-1]),
        splitted[4][:-1]: int(splitted[5][:-1]),
        splitted[6][:-1]: int(splitted[7]),
    }
    
    return id, compounds
    

def AoC_16_2015(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0
    
    ticker: dict = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    
    for auntie in datastream:
        is_auntie1: bool = True
        is_auntie2: bool = True
        id, compounds = extract(auntie)
        
        for compound in compounds:
            if ticker[compound] != compounds[compound]:
                is_auntie1 = False
                
            if compound in ["cats", "trees"]:
                if compounds[compound] <= ticker[compound]:
                    is_auntie2 = False
            elif compound in ["pomeranians", "goldfish"]:
                if compounds[compound] >= ticker[compound]:
                    is_auntie2 = False
            else:
                if ticker[compound] != compounds[compound]:
                    is_auntie2 = False
        
        if is_auntie1:
            antwoord1 = id
            
        if is_auntie2:
            antwoord2 = id

    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2015/AoC_16_2015.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_16_2015(invoer))