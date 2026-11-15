import pandas as pd
import numpy as np

temperature = pd.read_csv(
    "temperature.csv",
    na_values=["NA"]
)

temperature["month"] = temperature["month"].astype(int)
temperature["day"] = temperature["day"].astype(int)
temperature["year"] = temperature["year"].astype(int)

print(temperature.describe(include="all"))

mois_selectionnes = [3, 6, 9, 12]

temperature_filtre = temperature[
    temperature["month"].isin(mois_selectionnes)
].copy()

if "Region" in temperature_filtre.columns:
    temperature_filtre = temperature_filtre[
        temperature_filtre["Region"].str.lower() != "east"
    ]

elif "region" in temperature_filtre.columns:
    temperature_filtre = temperature_filtre[
        temperature_filtre["region"].str.lower() != "east"
    ]

temperature_filtre = temperature_filtre.dropna(
    subset=["AverageTemperatureFahr"]
)

print(temperature_filtre.head())

donnees_numpy = temperature_filtre[
    ["month", "AverageTemperatureFahr"]
].to_numpy()

moyennes_par_mois = {}

for mois in mois_selectionnes:
    temperatures_mois = donnees_numpy[
        donnees_numpy[:, 0] == mois, 1
    ]

    moyennes_par_mois[mois] = np.mean(temperatures_mois)

print("Moyenne des temperatures par mois :")

for mois, moyenne in moyennes_par_mois.items():
    print(f"Mois {mois} : {moyenne:.2f} °F")

temperature_pivot = temperature_filtre.pivot_table(
    index=["City", "year"],
    columns="month",
    values="AverageTemperatureFahr",
    aggfunc="mean"
)

temperature_pivot = temperature_pivot.rename(
    columns={
        3: "Mars",
        6: "Juin",
        9: "Septembre",
        12: "Decembre"
    }
)

temperature_pivot = temperature_pivot[
    ["Mars", "Juin", "Septembre", "Decembre"]
]

matrice_correlation = temperature_pivot.corr()

print("\nMatrice de correlation :")
print(matrice_correlation)
