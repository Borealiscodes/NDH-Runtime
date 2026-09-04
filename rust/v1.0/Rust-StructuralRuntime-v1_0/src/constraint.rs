#[derive(Debug, Clone)]
pub struct ConstraintEnvelope {
    pub altitude_min: u8,
    pub altitude_max: u8,
    pub drift_neutral: bool,
    pub reversible: bool,
}

impl ConstraintEnvelope {
    pub fn new() -> Self {
        Self {
            altitude_min: 4,
            altitude_max: 7,
            drift_neutral: true,
            reversible: true,
        }
    }

    pub fn validate_altitude(&self, altitude: u8) -> bool {
        altitude >= self.altitude_min && altitude <= self.altitude_max
    }
}
