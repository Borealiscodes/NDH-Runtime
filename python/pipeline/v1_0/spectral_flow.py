from .core import OperatorContext


def spectral_step(ctx: OperatorContext, adjacency: float, resonance: float) -> OperatorContext:
    """
    NDH spectral operator step.

    Updates spectral envelope fields in a reversible, non-activating way.
    """
    new_ctx = ctx.reversible_clone()
    new_ctx.spectral.reversible_update(adjacency, resonance)
    return new_ctx
