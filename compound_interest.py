def compounded_f_value(i_v, annual_r, t):
    """
    Calculates the future value of a lump-sum investment
    with annual compounding.
    
    Parameters:
        i_v (float): Initial investment (present value).
        annual_r (float): Annual interest rate (decimal).
        t (int): Number of years.
    
    Returns:
        float: Future value of the investment.
    """
    f = i_v * (1 + annual_r) ** (t)
    return f

def compounded_periodic_fvalue(payment, annual_r, m, t):
    """
    Calculates the future value of recurring contributions (annuity).
    
    Parameters:
        payment (float): Contribution made each period.
        annual_r (float): Annual interest rate (decimal).
        m (int): Number of compounding/contribution periods per year.
        t (int): Number of years.
    
    Returns:
        float: Future value of the recurring contributions.
    """
    r = annual_r/m
    n = m * t # número total de períodos

    # é a formula da soma geométrica de FV=P⋅[(1+i)**(n−1)+(1+i)**(n−2)+⋯+(1+i)**1+1]
    fv = payment * ((1 + r)**n - 1) / r 
    return fv

