**Contexte**

Dans le cadre de l’activité de valorisation de l’énergie sur les marchés de l’électricité, Elmy aimerait disposer d’un modèle de prévision permettant de juger en amont si les prix de l’électricité sur le marché 
SPOT (marché d’enchère européen permettant d’acheter de l’électricité la veille pour le lendemain) seront plus ou moins élevés que les prix de l’électricité sur le marché Intraday (marché boursier européen 
permettant d’acheter de l’électricité le jour même).

**But**

L’exercice consiste en la modélisation supervisée de l'écart de prix entre le marché infra-journalier (dit "Intraday") et le marché SPOT. L'écart de prix peut être modélisé par une régression mais aussi par une classification car ce qui importe avant tout est de prédire correctement le sens de cet écart (si tel ou tel prix sera supérieur ou inférieur à l’autre).

**Description des données**

`Index`

`DELIVERY_START` : date et heure de livraison de l'électricité

`Variables explicatives`
load_forecast : prévision de consommation totale d'éléctricité en France
coal_power_available, gas_power_available, nucelear_power_available : capacité de production totale d'électricité des centrales à charbon, gaz et nucléaire respectivement,
wind_power_forecasts_average, solar_power_forecasts_average : moyenne de différentes prévisions de production totale d'électricité éolienne et solaire (respectivement),
wind_power_forecasts_std, solar_power_forecasts_std : écart-type de ces mêmes prévisions,
predicted_spot_price : prévision du prix SPOT de l'électricité issues d'un modèle interne de Elmy. Ce modèle est lancé chaque jour avant la fermeture des enchères SPOT pour le lendemain.

`Variable cible`
spot_id_delta : l'écart entre le VWAP des transactions sur le marché infra-journalier (Intraday) et le prix SPOT pour 1MWh d'électricité (spot_id_delta = Intraday - SPOT) : si la valeur est positive, le prix Intraday est supérieur au prix SPOT et inversement.

**Résultat final**
Mise en place des modèles :
  - Modèle Random Forest
  - Modèle SARIMAX

**Source :** https://challengedata.ens.fr/participants/challenges/140/
