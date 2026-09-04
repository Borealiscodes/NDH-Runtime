#[derive(Debug, Clone)]
pub struct TopologyEnvelope {
    pub nodes: usize,
    pub edges: usize,
}

impl TopologyEnvelope {
    pub fn new() -> Self {
        Self { nodes: 0, edges: 0 }
    }

    pub fn reversible_add_node(&mut self) {
        self.nodes += 1;
    }

    pub fn reversible_add_edge(&mut self) {
        self.edges += 1;
    }
}
