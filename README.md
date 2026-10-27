# Black-Scholes : pricing d'options européennes

Script Python qui calcule le prix théorique d'un call et d'un put européens avec la formule de Black-Scholes, et vérifie la cohérence du résultat avec la parité call-put.

## Prérequis

- Python 3.8+
- `scipy`

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python black_scholes.py
```

Le script demande les paramètres (Entrée = valeur par défaut) puis affiche d1, d2, le prix du call, le prix du put et l'écart de parité.

Les fonctions sont aussi réutilisables dans un autre script :

```python
from black_scholes import prix_call, prix_put

prix_call(S=100, K=100, T=1, r=0.03, vol=0.2)   # 9.4134
prix_put(S=100, K=100, T=1, r=0.03, vol=0.2)    # 6.4580
```

## Paramètres

| Variable | Description | Valeur par défaut |
|---|---|---|
| `S` | Prix du sous-jacent | 100 |
| `K` | Prix d'exercice (strike) | 100 |
| `T` | Maturité, en années | 1 |
| `r` | Taux sans risque | 0.03 (3 %) |
| `vol` | Volatilité (σ) | 0.2 (20 %) |

## Formules

```
d1 = [ln(S/K) + (r + σ²/2) · T] / (σ · √T)
d2 = d1 − σ · √T

Call = S · N(d1) − K · e^(−rT) · N(d2)
Put  = K · e^(−rT) · N(−d2) − S · N(−d1)
```

où `N` est la fonction de répartition de la loi normale centrée réduite (`scipy.stats.norm.cdf`).

## Vérification : parité call-put

Pour une option européenne sans dividende :

```
C − P = S − K · e^(−rT)
```

Le script affiche l'écart entre les deux membres : il doit être proche de 0 (de l'ordre de 1e-15).

## Résultat attendu (valeurs par défaut)

```
d1            : 0.2500
d2            : 0.0500
Prix du call  : 9.4134
Prix du put   : 6.4580
Écart parité  : 0.00e+00
```

## Hypothèses du modèle

- Option européenne (exercice uniquement à l'échéance)
- Pas de dividendes
- Taux et volatilité constants
- Rendements log-normaux, marché sans frictions

## Pistes d'amélioration

- Calcul des grecques (delta, gamma, vega, theta, rho)
- Comparaison avec une simulation Monte Carlo
