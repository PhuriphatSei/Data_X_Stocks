def graham_valuation(eps: float, book_value_per_share: float) -> float:
    """
    Graham Number = sqrt(22.5 * EPS * BVPS)
    """
    if eps is None or book_value_per_share is None:
        return None
    try:
        val = (22.5 * eps * book_value_per_share) ** 0.5
        return round(val, 2)
    except:
        return None
