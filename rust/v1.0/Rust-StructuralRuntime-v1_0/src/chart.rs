#[derive(Debug, Clone)]
pub struct ChartEnvelope {
    pub flow_map: Vec<f64>,
}

impl ChartEnvelope {
    pub fn new() -> Self {
        Self { flow_map: vec![] }
    }

    pub fn reversible_push(&mut self, value: f64) {
        self.flow_map.push(value);
    }
}
