"""Functions to prevent a nuclear meltdown."""
def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.
 
    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?
 
    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    if temperature<800 and neutrons_emitted>500 and temperature*neutrons_emitted<500000:
        return True
    else:
        return False