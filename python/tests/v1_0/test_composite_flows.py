from ndh_runtime.pipeline.v1_0 import OperatorContext
from ndh_runtime.composite.v1_0 import (
    spectral_topology_step,
    spectral_integration_step,
)


def test_spectral_topology_step():
    ctx = OperatorContext()
    out = spectral_topology_step(
        ctx,
        adjacency=0.2,
        resonance=0.9,
        add_nodes=3,
        add_edges=2,
    )

    assert out.spectral.adjacency == 0.2
    assert out.spectral.resonance == 0.9
    assert out.topology.nodes == 3
    assert out.topology.edges == 2


def test_spectral_integration_step():
    ctx = OperatorContext()
    out = spectral_integration_step(
        ctx,
        adjacency=0.1,
        resonance=0.4,
        delta=0.05,
    )

    assert out.spectral.adjacency == 0.1
    assert out.spectral.resonance == 0.4
    assert out.integration.integrated_value == 0.05
