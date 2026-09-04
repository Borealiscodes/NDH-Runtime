use pyo3::prelude::*;
use ndh_runtime::hook::HookEnvelope;

#[pyclass]
pub struct PyHook {
    inner: HookEnvelope,
}

#[pymethods]
impl PyHook {
    #[new]
    pub fn new() -> Self {
        Self {
            inner: HookEnvelope::new(),
        }
    }

    pub fn reversible_register(&mut self) {
        self.inner.reversible_register();
    }

    pub fn registered(&self) -> bool {
        self.inner.registered
    }
}

pub fn register(m: &PyModule) -> PyResult<()> {
    m.add_class::<PyHook>()?;
    Ok(())
}
