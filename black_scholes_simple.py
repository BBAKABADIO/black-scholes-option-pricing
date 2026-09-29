import math
from scipy.stats import norm


def demander(message, defaut):
    """Demande un nombre à l'utilisateur ; Entrée = valeur par défaut."""
    while True:
        saisie = input(f"{message} [{defaut}] : ").strip().replace(",", ".")
        if saisie == "":
            return defaut
        try:
            return float(saisie)
        except ValueError:
            print("  Valeur invalide, entre un nombre (ex : 45 ou 0.1).")


# Étape 2 : variables demandées à l'utilisateur
S = demander("Prix du sous-jacent (S)", 45)
K = demander("Strike (K)", 40)
T = demander("Maturité en années (T)", 2)
r = demander("Taux sans risque (r, ex : 0.1 pour 10 %)", 0.1)
vol = demander("Volatilité (σ, ex : 0.1 pour 10 %)", 0.1)

if S <= 0 or K <= 0 or T <= 0 or vol <= 0:
    raise SystemExit("Erreur : S, K, T et vol doivent être strictement positifs.")

# Étape 3 : d1
d1 = (math.log(S / K) + (r + 0.5 * vol**2) * T) / (vol * math.sqrt(T))

# Étape 4 : d2
d2 = d1 - (vol * math.sqrt(T))

# Étape 5 : prix du call
C = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

# Étape 6 : prix du put
P = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Étape 7 : résultats
print()
print('The value of d1 is: ', round(d1, 4))
print('The value of d2 is: ', round(d2, 4))
print('The price of the call option is: $', round(C, 2))
print('The price of the put option is: $', round(P, 2))
