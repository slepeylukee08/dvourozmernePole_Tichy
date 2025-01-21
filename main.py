# Původní dvourozměrné pole s 3 řádky a 3 sloupci
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Přidání nového řádku
matrix.append([10, 11, 12])

# Přidání nového sloupce (přidáme hodnotu k jednotlivým řádkům)
for row in matrix:
    row.append(0)  # Přidání hodnoty 0 jako nový sloupec

# Vytisknutí upraveného pole
for row in matrix:
    print(row)
