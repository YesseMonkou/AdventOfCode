from math import prod

def extract(data:list[str]) -> dict:
    ingredients: dict = {}
    
    for ingredient in data:
        splitted = ingredient.split(" ")
        ingredients[splitted[0][:-1]] = {
            "capacity": int(splitted[2][:-1]),
            "durability": int(splitted[4][:-1]),
            "flavor": int(splitted[6][:-1]),
            "texture": int(splitted[8][:-1]),
            "calories": int(splitted[10]),
        }
    
    return ingredients

def AoC_15_2015(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0

    ingredients: dict = extract(datastream)
    
    for k in range(1, 101):
        sum: int = k
        
        if sum == 100:
            score_list: list = []
            for attr in ingredients["Butterscotch"].keys():
                score_list.append(ingredients["Butterscotch"][attr] * k)
            antwoord1 = max(antwoord1, prod(score_list))
            
        for n in range(1, 101):
            sum = k + n
            
            if sum == 100:
                score_list: list = []
                for attr in ingredients["Butterscotch"].keys():
                    score_list.append(ingredients["Butterscotch"][attr] * k + ingredients["Cinnamon"][attr] * n)
                antwoord1 = max(antwoord1, prod(score_list))
                break
    
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2015/AoC_15_2015.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_15_2015(invoer))