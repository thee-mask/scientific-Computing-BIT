# Task 11: Root Finding with Newton-Raphson and Secant Methods (`Task_11_newton_secant.py`)

## B. Input Values and Mathematical Operations

- **Inputs:** An equipment purchase of $12,000 followed by estimated savings of $3,500, $3,900, $4,200, and $4,500 at the ends of years 1 through 4. The modified case raises the purchase price to $13,500.
- **Mathematical operations:** The program defines net present value as NPV(r) = sum(CF_t / (1+r)^t) and finds the rate r for which NPV is zero. Newton-Raphson uses the derivative of NPV; the secant method estimates the slope from two rate guesses. The two methods are compared as a check.

## C. Parameter Modification and Impact

- **Change made:** Increase the initial purchase cost from $12,000 to $13,500, leaving the future savings unchanged.
- **Result change:** Both methods give an IRR of about 12.3156% for the $12,000 purchase and about 7.1224% for the $13,500 purchase.
- **Explanation:** The higher initial cost lowers NPV at any fixed discount rate. A lower rate is therefore needed for discounted savings to balance the initial investment.

## D. Output Interpretation

- **Numerical output:** The two methods agree to the displayed precision. NPV at each computed root is approximately zero.
- **Meaning:** The IRR is the annual discount rate at which the present value of forecast savings equals the purchase cost. Agreement between Newton-Raphson and secant supports the computed result, but does not validate the savings forecast itself.
- **Graph:** No graph is generated for this task.

## E. Modified Real-World Case: Equipment Investment Payback Rate

- **Problem statement:** Estimate the annual return implied by purchasing energy-saving equipment and receiving forecast savings over four years.
- **Assumptions:** The initial purchase is paid at time zero; savings arrive once per year; cash flows are known and do not change; no taxes, maintenance, resale value, or inflation are included.
- **Input data:** Initial cost $12,000 or $13,500; annual savings $3,500, $3,900, $4,200, and $4,500.
- **Output:** The script reports Newton-Raphson IRR, secant IRR, and NPV at the Newton solution for both costs.
- **Interpretation:** Under these assumptions, raising the purchase cost reduces the estimated return from about 12.32% to 7.12%. The result is sensitive to forecast savings and should be interpreted as a model estimate.

## F. Individual Repository Note

Keep the Python file and this documentation in your own repository. Run the script from the repository root with `python code/Task_11_newton_secant.py`, then include your observed output in your submission.
