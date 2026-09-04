use pyo3::prelude::*;
use ndh_runtime::spectral::SpectralEnvelope;

#[pyclass]
pub struct PySpectral {
    inner: SpectralEnvelope,
}

#[pymethods]
impl PySpectral {
    #[new]
    pub fn new() -> Self {
        Self {
            inner: SpectralEnvelope::new(),
        }
    }

    pub fn reversible_update(&mut self, adjacency: f64, resonance: f64) {
        self.inner.reversible_update(adjacency, resonance);
    }

    pub fn adjacency(&self) -> f64 {
        self.inner.adjacency
    }

    pub fn resonance(&self) -> f64 {
        self.inner.resonance
    }
}

pub fn register(m: &PyModule) -> PyResult<()> {
    m.add_class::<PySpectral>()?;
    Ok(())
}
