
import math

def dhondt_gen():
    """Generate a d'Hondt divider sequence: 1, 2, 3..."""
    n = 1.0
    while True:
        yield n
        n += 1.0

def sainte_lague_gen():
    """Generate a Sainte-Lague divider sequence: 1, 3, 5..."""
    n = 1.0
    while True:
        yield n
        n += 2.0

def nordic_sainte_lague_gen():
    """Generate a Nordic Sainte-Lague divide sequence: 1.4, 3, 5..."""
    yield 1.4
    n = 3.0
    while True:
        yield n
        n += 2.0

def imperiali_gen():
    """Generate Imperiali divider sequence: 1, 1.5, 2, 2.5,..."""
    n = 1.0
    while True:
        yield n
        n += 0.5

def danish_gen():
    """Generate Danish divider sequence: 0.33, 1.33, 2.33,..."""
    n = 0.33
    while True:
        yield n
        n += 1.0

def huntington_hill_gen():
    """Generate Huntington-Hill divider sequence; modified for hh(0) -> \inf"""
    n = 0
    yield 10000000000
    while True:
        n += 1
        yield math.sqrt(n*(n+1))