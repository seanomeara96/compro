import celsius_to_kelvin


def pressure(v, t, n):
    """Compute the pressure in pascals of an ideal gas.

    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particles of gas / amount of substance
    """
    k = 1.38e-23  # Boltzmann's constant
    return n * k * t / v


print(pressure(1, celsius_to_kelvin.convert(32), 100))
