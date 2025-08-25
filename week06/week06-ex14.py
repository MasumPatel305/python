def add_tax(price: float) -> float:
    if price >= 100:
        return price * 1.10
    return price * 1.05

taxed = [add_tax(p) for p in [75, 120, 100, 30]]
print("Taxed prices:", taxed)
