from ndh_runtime.pipeline.v1_0 import (
    OperatorContext,
    spectral_step,
    integration_step,
)


def spectral_integration_step(
    ctx: OperatorContext,
    adjacency: float,
    resonance: float,
    delta: float,
) -> OperatorContext:
    """
    Composite operator:
    1. Apply spectral_step.
    2. Apply integration_step.
    All operations are reversible and non-activating.
    """
    ctx1 = spectral_step(ctx, adjacency=adjacency, resonance=resonance)
    ctx2 = integration_step(ctx1, delta=delta)
    return ctx2
