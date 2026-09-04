#[derive(Debug, Clone)]
pub struct HookEnvelope {
    pub registered: bool,
}

impl HookEnvelope {
    pub fn new() -> Self {
        Self { registered: false }
    }

    pub fn reversible_register(&mut self) {
        self.registered = true;
    }
}
