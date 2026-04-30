import re
import sys

def verificacao(cell):
    # remove tudo que não for número
    cell = re.sub(r"\D", "", cell)
        
    if cell[0] != "5" and cell[1] != "5":
        cell = "+55" + cell

    if cell[0] == "5" and cell[1] != "5":
        cell = "+5" + cell

    return cell