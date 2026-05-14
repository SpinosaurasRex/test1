def charger_pokemons_csv(nom_fichier):
    pokemons = {}

    with open(nom_fichier, "r") as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:
                continue

            nom, hp, atk, df, spa, spd, spe = ligne.split(",")

            pokemons[nom] = {
                "HP": int(hp),
                "ATK": int(atk),
                "DEF": int(df),
                "SPA": int(spa),
                "SPD": int(spd),
                "SPE": int(spe)
            }

    return pokemons


# Programme principal
pkmn = charger_pokemons_csv("pokemon.csv")
print(pkmn)
