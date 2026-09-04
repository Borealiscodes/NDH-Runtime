use pyo3::prelude::*;
use ndh_runtime::topology::TopologyEnvelope;

#[pyclass]
pub struct PyTopology {
    inner: TopologyEnvelope,
}

#[pymethods]
impl PyTopology {
    #[new]
    pub fn new() -> Self {
        Self {
            inner: TopologyEnvelope::new(),
        }
    }

    pub fn reversible_add_node(&mut self) {
        self.inner.reversible_add_node();
    }

    pub fn reversible_add_edge(&mut self) {
        self.inner.reversible_add_edge();
    }

    pub fn nodes(&self) -> usize {
        self.inner.nodes
    }

    pub fn edges(&self) -> usize {
        self.inner.edges
    }
}

pub fn register(m: &PyModule) -> PyResult<()> {
    m.add_class::<PyTopology>()?;
    Ok(())
}
