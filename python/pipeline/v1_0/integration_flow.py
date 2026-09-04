from .core import OperatorContext


def integration_step(ctx: OperatorContext, delta: float) -> OperatorContext:
    """
    NDH integration operator step.

    Integrates over runtime flows in a reversible, non-activating way.
    """
    new_ctx = ctx.reversible_clone()
    new_ctx.integration.reversible_integrate(delta)
    return new_ctx
