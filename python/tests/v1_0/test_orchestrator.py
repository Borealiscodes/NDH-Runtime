from ndh_runtime.orchestrator.v1_0 import RuntimeOrchestrator


def test_spectral_topology_flow():
    o = RuntimeOrchestrator()
    o2 = o.run_spectral_topology_flow(
        adjacency=0.3,
        resonance=0.8,
        add_nodes=1,
        add_edges=1,
    )

    assert o2.ctx.spectral.adjacency == 0.3
    assert o2.ctx.topology.nodes == 1


def test_spectral_integration_flow():
    o = RuntimeOrchestrator()
    o2 = o.run_spectral_integration_flow(
        adjacency=0.2,
        resonance=0.5,
        delta=0.1,
    )

    assert o2.ctx.integration.integrated_value == 0.1
