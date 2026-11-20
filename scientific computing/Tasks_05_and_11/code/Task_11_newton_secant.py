"""Task 11: calculate the return on an equipment investment.

Inputs: purchase cost $12,000 and four years of forecast savings.
Operation: solve NPV(rate)=0 with Newton-Raphson and secant methods.
Parameter change: increase purchase cost by $1,500 and recalculate.
Run: python code/Task_11_newton_secant.py
"""
from scipy.optimize import root_scalar

cash_flows = [-12000.0, 3500.0, 3900.0, 4200.0, 4500.0]

def npv(rate, flows):
    return sum(value / (1.0 + rate) ** year for year, value in enumerate(flows))

def derivative(rate, flows):
    return sum(-year * value / (1.0 + rate) ** (year + 1)
               for year, value in enumerate(flows) if year > 0)

for purchase_cost in (12000.0, 13500.0):
    flows = cash_flows.copy()
    flows[0] = -purchase_cost
    newton = root_scalar(lambda r: npv(r, flows), fprime=lambda r: derivative(r, flows),
                         x0=0.10, method="newton", xtol=1e-12)
    secant = root_scalar(lambda r: npv(r, flows), x0=0.05, x1=0.20,
                         method="secant", xtol=1e-12)
    print(f"Purchase cost ${purchase_cost:,.0f}: Newton IRR={newton.root:.4%}, "
          f"secant IRR={secant.root:.4%}, NPV={npv(newton.root, flows):.6f}")
