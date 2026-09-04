use pyo3::prelude::*;
use ndh_runtime::chart::ChartEnvelope;

#[pyclass]
pub struct PyChart {
    inner: ChartEnvelope,
}

#[pymethods]
impl PyChart {
    #[new]
    pub fn new() -> Self {
        Self {
            inner: ChartEnvelope::new(),
        }
    }

    pub fn reversible_push(&mut self, value: f64) {
        self.inner.reversible_push(value);
    }
}

pub fn register(m: &PyModule) -> PyResult<()> {
    m.add_class::<PyChart>()?;
    Ok(())
}
