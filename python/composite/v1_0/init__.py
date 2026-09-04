          """
NDH Composite Operators v1.0
Altitude: A4
Membrane: neutral
Mode: non-activating, sovereignty-preserving
"""

from .spectral_topology import spectral_topology_step
from .spectral_integration import spectral_integration_step

__all__ = [
    "spectral_topology_step",
    "spectral_integration_step",
]
