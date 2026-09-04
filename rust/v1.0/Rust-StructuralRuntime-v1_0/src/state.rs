#[derive(Debug, Clone)]
pub struct StateEnvelope {
    pub altitude: u8,
    pub membrane: &'static str,
    pub adjacency_field: f64,
    pub resonance_field: f64,
    pub flow_field: f64,
    pub calm_load: f64,
    pub precl_buffer: f64,
}

impl StateEnvelope {
    pub fn new() -> Self {
        Self {
            altitude: 5,
            membrane: "neutral",
            adjacency_field: 0.0,
            resonance_field: 0.0,
            flow_field: 0.0,
            calm_load: 0.0,
            precl_buffer: 0.0,
        }
    }

    pub fn reversible_clone(&self) -> Self {
        self.clone()
    }
}
