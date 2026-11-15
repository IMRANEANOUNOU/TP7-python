import pandas as pd
import matplotlib.pyplot as plt

covid = pd.read_csv(
    "covid-hospit.csv",
    na_values=["NA"],
    parse_dates=["jour"]
)

print(covid.head())
print(covid.tail())
print(covid.dtypes)

covid["jour"] = pd.to_datetime(covid["jour"])

colonnes_numeriques = [
    "hosp", "rea", "HospConv", "SSR_USLD",
    "autres", "rad", "dc"
]

agg_par_jour = (
    covid.drop(["dep", "sexe"], axis=1)
         .groupby("jour")[colonnes_numeriques]
         .sum()
)

print(agg_par_jour.tail())

agg_par_jour.plot(
    figsize=(12, 6),
    logy=True,
    title="Évolution des données COVID par jour"
)

plt.xlabel("Jour")
plt.ylabel("Nombre de personnes")
plt.grid(True, which="both")
plt.tight_layout()
plt.show()

covid_hommes = covid[covid["sexe"] == 1]

agg_hommes = (
    covid_hommes.drop(["dep", "sexe"], axis=1)
                .groupby("jour")[colonnes_numeriques]
                .sum()
)

print(agg_hommes.tail())

agg_hommes.plot(
    figsize=(12, 6),
    logy=True,
    title="Évolution des données COVID chez les hommes"
)

plt.xlabel("Jour")
plt.ylabel("Nombre d'hommes")
plt.grid(True, which="both")
plt.tight_layout()
plt.show()

diff_hommes = agg_hommes.diff()

diff_hommes.plot(
    figsize=(12, 6),
    title="Différences journalières des données COVID chez les hommes"
)

plt.xlabel("Jour")
plt.ylabel("Variation journalière")
plt.grid(True)
plt.tight_layout()
plt.show()

moyenne_mobile_hommes = agg_hommes.rolling(window=7).mean()

moyenne_mobile_hommes.plot(
    figsize=(12, 6),
    title="Moyenne mobile sur 7 jours chez les hommes"
)

plt.xlabel("Jour")
plt.ylabel("Moyenne sur 7 jours")
plt.grid(True)
plt.tight_layout()
plt.show()

diff_moyenne_mobile_hommes = moyenne_mobile_hommes.diff()

diff_moyenne_mobile_hommes.plot(
    figsize=(12, 6),
    title="Différences de la moyenne mobile sur 7 jours chez les hommes"
)

plt.xlabel("Jour")
plt.ylabel("Variation")
plt.grid(True)
plt.tight_layout()
plt.show()
