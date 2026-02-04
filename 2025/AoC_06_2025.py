def extract_data(datastream: list[str]) -> list[list]:
    problems: list[list] = []
    
    for x, row in enumerate(datastream):
        i: int = 0
        for entity in row.split(" "):
            if x == 0:
                if entity != "":
                    problems.append([int(entity)])
            
            else:        
                if entity == "":
                    continue
                if entity in ["*", "+"]:
                    problems[i].append(entity)
                    i += 1  
                    continue
                    
                problems[i].append(int(entity))
                i += 1
    
    return problems


def extract_data2(datastream: list[str]) -> list[list[str]]:
    problems: list[list] = []
    equation: list[str] = []
    
    for x in range(len(datastream[0])-1, -1, -1):
        number: str = ""
        for y in range(len(datastream)-1):
            if datastream[y][x] == " ":
                continue
            number += datastream[y][x]
        
        if number != "":
            equation.append(number)
            
        if datastream[-1][x] in ["*", "+"]:
            equation.append(datastream[-1][x])
            problems.append(equation)
            equation = []
        
    return problems


def AoC_06_2025(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0

    # PART 1
    problems: list[list] = extract_data(datastream)
    
    for problem in problems:
        if problem[-1] == "+":
            antwoord1 += sum(problem[:-1])
        elif problem[-1] == "*":
            result = 1
            for number in problem[:-1]:
                result *= number
            antwoord1 += result
            
    # PART 2
    problems2: list[list] = extract_data2(datastream)
    
    for problem in problems2:
        if problem[-1] == "+":
            antwoord2 += sum(map(int, problem[:-1]))
        elif problem[-1] == "*":
            result = 1
            for number in problem[:-1]:
                result *= int(number)
            antwoord2 += result
    
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2025/AoC_06_2025.txt", "r") as fh:
        invoer: list[str] = [regels.strip("\n") for regels in fh]

    print(AoC_06_2025(invoer))