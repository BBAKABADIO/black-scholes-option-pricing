"""Pricing d'options européennes avec la formule de Black-Scholes."""

import math

from scipy.stats import norm


def valider(S, K, T, vol):
    """Vérifie que les paramètres sont strictement positifs."""
    if S <= 0 or K <= 0 or T <= 0 or vol <= 0:
        raise ValueError("S, K, T et vol doivent être strictement positifs.")


def d1_d2(S, K, T, r, vol):
    """Calcule d1 et d2."""
    valider(S, K, T, vol)
    d1 = (math.log(S / K) + (r + 0.5 * vol**2) * T) / (vol * math.sqrt(T))
    d2 = d1 - vol * math.sqrt(T)
    return d1, d2


def prix_call(S, K, T, r, vol):
    """Prix d'un call européen."""
    d1, d2 = d1_d2(S, K, T, r, vol)
    return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)


def prix_put(S, K, T, r, vol):
    """Prix d'un put européen."""
    d1, d2 = d1_d2(S, K, T, r, vol)
    return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


def parite_call_put(S, K, T, r, vol):
    """Vérifie la parité call-put : C - P = S - K * exp(-rT).

    Renvoie l'écart entre les deux membres (proche de 0 si le calcul est juste).
    """
    C = prix_call(S, K, T, r, vol)
    P = prix_put(S, K, T, r, vol)
    return (C - P) - (S - K * math.exp(-r * T))


def demander(message, defaut):
    """Demande un nombre à l'utilisateur ; Entrée = valeur par défaut."""
    while True:
        saisie = input(f"{message} [{defaut}] : ").strip().replace(",", ".")
        if saisie == "":
            return defaut
        try:
            return float(saisie)
        except ValueError:
            print("  Valeur invalide, entre un nombre (ex : 100 ou 0.2).")


def main():
    S = demander("Prix du sous-jacent (S)", 100)
    K = demander("Strike (K)", 100)
    T = demander("Maturité en années (T)", 1)
    r = demander("Taux sans risque (r, ex : 0.03 pour 3 %)", 0.03)
    vol = demander("Volatilité (σ, ex : 0.2 pour 20 %)", 0.2)

    try:
        d1, d2 = d1_d2(S, K, T, r, vol)
    except ValueError as erreur:
        raise SystemExit(f"Erreur : {erreur}")

    print()
    print(f"d1            : {d1:.4f}")
    print(f"d2            : {d2:.4f}")
    print(f"Prix du call  : {prix_call(S, K, T, r, vol):.4f}")
    print(f"Prix du put   : {prix_put(S, K, T, r, vol):.4f}")
    print(f"Écart parité  : {parite_call_put(S, K, T, r, vol):.2e}")


if __name__ == "__main__":
    main()
