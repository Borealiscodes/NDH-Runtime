from ndh_runtime.pipeline.v1_0 import OperatorContext


def test_reversible_clone():
    ctx = OperatorContext()
    ctx.spectral.adjacency = 0.5

    clone = ctx.reversible_clone()

    assert clone.spectral.adjacency == 0.5
    assert clone is not ctx
    assert clone.spectral is not ctx.spectral
