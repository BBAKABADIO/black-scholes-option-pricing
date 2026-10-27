# Black-Scholes : pricing d'une option européenne

Script Python qui calcule le prix théorique d'un call et d'un put européens avec la formule de Black-Scholes.

## Prérequis

- Python 3.8+
- `scipy`

```bash
pip install scipy
```

## Utilisation

```bash
python black_scholes_simple.py
```

## Paramètres (modifiables en haut du fichier)

| Variable | Description | Valeur par défaut |
|---|---|---|
| `S` | Prix du sous-jacent | 45 |
| `K` | Prix d'exercice (strike) | 40 |
| `T` | Maturité, en années | 2 |
| `r` | Taux sans risque | 0.1 (10 %) |
| `vol` | Volatilité (σ) | 0.1 (10 %) |

## Formules

```
d1 = [ln(S/K) + (r + σ²/2) · T] / (σ · √T)
d2 = d1 − σ · √T

Call = S · N(d1) − K · e^(−rT) · N(d2)
Put  = K · e^(−rT) · N(−d2) − S · N(−d1)
```

où `N` est la fonction de répartition de la loi normale centrée réduite (`scipy.stats.norm.cdf`).

## Résultat attendu

```
The value of d1 is:  2.3178
The value of d2 is:  2.1764
The price of the call option is: $ 12.27
The price of the put option is: $ 0.02
```

## Hypothèses du modèle

- Option européenne (exercice uniquement à l'échéance)
- Pas de dividendes
- Taux et volatilité constants
- Rendements log-normaux, marché sans frictions
