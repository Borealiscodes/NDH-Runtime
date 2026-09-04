use pyo3::prelude::*;

mod state;
mod constraint;
mod spectral;
mod chart;
mod topology;
mod integration;
mod hook;

#[pymodule]
fn ndh_runtime_ffi(_py: Python, m: &PyModule) -> PyResult<()> {
    state::register(m)?;
    constraint::register(m)?;
    spectral::register(m)?;
    chart::register(m)?;
    topology::register(m)?;
    integration::register(m)?;
    hook::register(m)?;
    Ok(())
}
