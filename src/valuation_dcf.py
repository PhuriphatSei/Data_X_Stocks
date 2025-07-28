def dcf_valuation(
    fcff_now: float,
    growth_rate: float,
    wacc: float,
    n_years: int = 5,
    terminal_growth: float = 0.02,
    shares_outstanding: float = None
) -> dict:
    if shares_outstanding is None or shares_outstanding == 0:
        raise ValueError("shares_outstanding ต้องไม่เป็น None หรือ 0")

    fcf_list = [fcff_now * ((1 + growth_rate) ** i) for i in range(1, n_years + 1)]
    discounted_fcf = [fcf / ((1 + wacc) ** i) for i, fcf in enumerate(fcf_list, start=1)]
    terminal_value = fcf_list[-1] * (1 + terminal_growth) / (wacc - terminal_growth)
    discounted_terminal = terminal_value / ((1 + wacc) ** n_years)
    total_dcf = sum(discounted_fcf) + discounted_terminal
    intrinsic_value_per_share = total_dcf / shares_outstanding
    return {
        'dcf_value': round(total_dcf, 2),
        'intrinsic_value_per_share': round(intrinsic_value_per_share, 2)
    }
