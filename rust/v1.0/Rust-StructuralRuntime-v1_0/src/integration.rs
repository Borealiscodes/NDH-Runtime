#[derive(Debug, Clone)]
pub struct IntegrationEnvelope {
    pub integrated_value: f64,
}

impl IntegrationEnvelope {
    pub fn new() -> Self {
        Self { integrated_value: 0.0 }
    }

    pub fn reversible_integrate(&mut self, delta: f64) {
        self.integrated_value += delta;
    }
}
