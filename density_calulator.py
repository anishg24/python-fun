#!/usr/bin/env python3
def calculate_density(m,v):
    """ 
    Calculates the density when given a mass and volume

    >>> calculate_density(m,v)
        m = given mass
        v = given volume
    
    Outputs in "calculate_density.density"
    """
    calculate_density.density = m/v

def calculate_mass(d,v):
    """
    Calculates the mass when given a density and volume

    >>> calculate_mass(d,v)
        d = given density
        v = given volume

    Outputs in "calculate_mass.mass"
    """
    calculate_mass.mass = d * v

def calculate_volume(m,d):
    """
    Calculates the volume when given a mass and density

    >>> calculate_volume(m,v)
        m = given mass
        d = given density

    Outputs in "calculate_volume.volume"
    """
    calculate_volume.volume = m/d
