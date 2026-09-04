#[derive(Debug, Clone)]
pub struct SpectralEnvelope {
    pub adjacency: f64,
    pub resonance: f64,
}

impl SpectralEnvelope {
    pub fn new() -> Self {
        Self {
            adjacency: 0.0,
            resonance: 0.0,
        }
    }

    pub fn reversible_update(&mut self, adj: f64, res: f64) {
        self.adjacency = adj;
        self.resonance = res;
    }
}
