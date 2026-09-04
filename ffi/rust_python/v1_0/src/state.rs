use pyo3::prelude::*;
use ndh_runtime::state::StateEnvelope;

#[pyclass]
pub struct PyState {
    inner: StateEnvelope,
}

#[pymethods]
impl PyState {
    #[new]
    pub fn new() -> Self {
        Self {
            inner: StateEnvelope::new(),
        }
    }

    pub fn reversible_clone(&self) -> PyState {
        PyState {
            inner: self.inner.reversible_clone(),
        }
    }

    pub fn altitude(&self) -> u8 {
        self.inner.altitude
    }

    pub fn membrane(&self) -> &'static str {
        self.inner.membrane
    }
}

pub fn register(m: &PyModule) -> PyResult<()> {
    m.add_class::<PyState>()?;
    Ok(())
}
