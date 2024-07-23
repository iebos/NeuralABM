from enum import IntEnum

# Agent kinds and their order used in the SEIRD+ model


class Compartments(IntEnum):
    susceptible = 0
    infected = 1
    recovered = 2
    deceased = 3
