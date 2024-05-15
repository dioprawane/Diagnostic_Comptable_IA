import pandas as pd

# Données d'exemple
data = {
    "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"],
    "Description": ["Achat de fournitures", "Vente de produits", "Paiement de loyer", "Remboursement de prêt"],
    "Montant": [500.00, 1000.00, 1200.00, 800.00],
    "Compte": ["Fournisseur A", "Client B", "Propriétaire C", "Banque D"]
}

# Créer un DataFrame
df = pd.DataFrame(data)

# Sauvegarder le DataFrame en fichier Excel
df.to_excel("ecritures_comptables_test.xlsx", index=False)
