use pyo3::prelude::*;
use ndh_runtime::integration::IntegrationEnvelope;

#[pyclass]
pub struct PyIntegration {
    inner: IntegrationEnvelope,
}

#[pymethods]
impl PyIntegration {
    #[new]
    pub fn new() -> Self {
        Self {
            inner: IntegrationEnvelope::new(),
        }
    }

    pub fn reversible_integrate(&mut self, delta: f64) {
        self.inner.reversible_integrate(delta);
    }

    pub fn integrated_value(&self) -> f64 {
        self.inner.integrated_value
    }
}

pub fn register(m: &PyModule) -> PyResult<()> {
    m.add_class::<PyIntegration>()?;
    Ok(())
}
