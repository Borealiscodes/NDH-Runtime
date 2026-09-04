use pyo3::prelude::*;
use ndh_runtime::constraint::ConstraintEnvelope;

#[pyclass]
pub struct PyConstraint {
    inner: ConstraintEnvelope,
}

#[pymethods]
impl PyConstraint {
    #[new]
    pub fn new() -> Self {
        Self {
            inner: ConstraintEnvelope::new(),
        }
    }

    pub fn validate_altitude(&self, altitude: u8) -> bool {
        self.inner.validate_altitude(altitude)
    }
}

pub fn register(m: &PyModule) -> PyResult<()> {
    m.add_class::<PyConstraint>()?;
    Ok(())
}
