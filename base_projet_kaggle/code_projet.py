import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Filtrer les lignes avec des valeurs non manquantes pour l'entraînement
train_data = X.dropna(subset=['predicted_spot_price'])
train_data.dropna(inplace=True)
# Séparer la variable cible et les variables explicatives
X_train = train_data.drop(columns=['predicted_spot_price', 'DELIVERY_START'])
y_train = train_data['predicted_spot_price']

# Séparer les données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.1, random_state=42)

# Initialiser les modèles
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Lasso Regression": Lasso(alpha=0.1),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=3000, random_state=42,max_features='sqrt')
}

# Dictionnaire pour stocker les résultats
results = {}

# Entraîner chaque modèle et évaluer les performances
for model_name, model in models.items():
    # Entraîner le modèle
    model.fit(X_train, y_train)

    # Prédire les valeurs
    predictions = model.predict(X_test)

    # Calculer RMSE et R^2
    rmse = mean_squared_error(y_test, predictions, squared=False)
    r2 = r2_score(y_test, predictions)

    # Stocker les résultats
    results[model_name] = {
        'RMSE': rmse,
        'R^2': r2
    }

# Afficher les résultats
results_df = pd.DataFrame(results).T  # Transpose pour une meilleure lisibilité
print(results_df)



# Supposons que X est votre DataFrame contenant les données

# 1. Filtrer les lignes avec des valeurs non manquantes pour l'entraînement
train_data = X.dropna(subset=['predicted_spot_price'])

# 2. Séparer la variable cible et les variables explicatives
X_train = train_data.drop(columns=['predicted_spot_price', 'DELIVERY_START'])
y_train = train_data['predicted_spot_price']

# 3. Identifier les lignes avec des valeurs manquantes dans 'predicted_spot_price'
missing_data = X[X['predicted_spot_price'].isna()]

# 4. Entraîner le modèle sur les données sans valeurs manquantes
model = RandomForestRegressor(n_estimators=3000, random_state=42,max_features='sqrt')
model.fit(X_train, y_train)

# 5. Prédire les valeurs manquantes de predicted_spot_price
# On utilise les caractéristiques des lignes avec des valeurs manquantes
missing_data_features = missing_data.drop(columns=['predicted_spot_price', 'DELIVERY_START'])
predictions = model.predict(missing_data_features)

# 6. Remplacer les valeurs manquantes dans le DataFrame d'origine
X.loc[X['predicted_spot_price'].isna(), 'predicted_spot_price'] = predictions

# 7. Vérifiez que les valeurs manquantes ont été remplacées
print(f"Nombre de valeurs manquantes dans 'predicted_spot_price': {X['predicted_spot_price'].isna().sum()}")  # Devrait être 0

# Optionnel : Afficher les 5 premières lignes pour vérification
X.head()




import pandas as pd

# 1. Keep a copy of the original test set
X_test_full = Xtest.copy()



# 3. Make predictions on the test set
y_test_pred = rf_reg.predict(Xtest1)  # Use your features for testing

# 4. Create a DataFrame with predictions and DELIVERY_START
results = pd.DataFrame({
    'DELIVERY_START': X_test_full['DELIVERY_START'],  # Assuming this column exists
    'spot_id_delta': y_test_pred
})

# 5. Save the results to a CSV file
results.to_csv('with_delivery_start.csv', index=False)

# Optionally, display a message
print("Results saved to predictions_with_delivery_start.csv")
