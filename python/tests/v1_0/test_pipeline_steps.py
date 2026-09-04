from ndh_runtime.pipeline.v1_0 import (
    OperatorContext,
    spectral_step,
    topology_step,
    integration_step,
)


def test_spectral_step():
    ctx = OperatorContext()
    out = spectral_step(ctx, adjacency=0.3, resonance=0.7)

    assert out.spectral.adjacency == 0.3
    assert out.spectral.resonance == 0.7


def test_topology_step():
    ctx = OperatorContext()
    out = topology_step(ctx, add_nodes=2, add_edges=1)

    assert out.topology.nodes == 2
    assert out.topology.edges == 1


def test_integration_step():
    ctx = OperatorContext()
    out = integration_step(ctx, delta=0.1)

    assert out.integration.integrated_value == 0.1
