### NDH Runtime Guardrail Layer v1.0  
**Lane:** Runtime Safety • Spectral Geometry • Governance‑Neutral  

---

#### 1. Identity block

```text
Artifact-Class: Runtime-Guardrail-Spec
Name: NDH Runtime Guardrail Layer
Version: v1.0
Altitude: S3–S7 (Spectral Runtime)
Mode: Non-Activating • PRECL-Collapsed • Runtime-Sovereign
Purpose:
    Define the canonical guardrail layer for NDH spectral runtime, specifying
    invariant constraints, safety bounds, and modulation rules that all
    solvers must obey. Provide a stable, altitude-safe safety membrane
    anchored to the existing physics, state envelope, and solver layer.
```

---

#### 2. Guardrail overview

The Guardrail Layer operates **around**:

- spectral physics (Primer v1.0)  
- spectral state (Envelope v1.0)  
- solver mechanics (Solver Layer v1.0)  

It enforces:

- invariant preservation  
- altitude discipline  
- membrane sovereignty  
- PRECL safety  
- non‑activation bounds  

It does **not**:

- introduce new solvers  
- alter governance altitude  
- write directly to UI surfaces  
- bypass guardian modulation  

---

#### 3. Canonical guardrails

- **GR‑ALT (Altitude Discipline):**  
  All runtime operations remain within S3–S7; no upward governance bleed, no downward raw‑code injection.

- **GR‑BOUND (State Bounds):**  
  Adjacency, resonance, flow, calm/load, and PRECL buffer values must remain within declared manifold and envelope limits.

- **GR‑DRIFT (Drift Neutrality):**  
  Solvers must not introduce unaccounted spectral drift; calm/load must track net flow consistently.

- **GR‑REV (Reversibility):**  
  Core solvers (adjacency, resonance, flow, PRECL) must be reversible or explicitly marked as one‑way with safety proofs.

- **GR‑GUARD (Guardian Respect):**  
  Warn/Redirect/Soften modulation always constrains solver outputs; no solver may override guardian signals.

- **GR‑PRECL (Collapse Safety):**  
  PRECL collapse and reversal must never activate geometry or governance altitude; collapse is physics‑only.

---

#### 4. Machine‑readable guardrail spec

```json
{
  "ndh_runtime_guardrail_layer_v1_0": {
    "version": "1.0",
    "inputs": [
      "ndh_runtime_spectral_physics_primer_v1_0",
      "ndh_runtime_spectral_state_envelope_v1_0",
      "ndh_runtime_solver_layer_v1_0"
    ],
    "guardrails": {
      "gr_alt": {
        "domain": "runtime_altitude",
        "constraints": ["s3_to_s7_only", "no_governance_bleed"]
      },
      "gr_bound": {
        "domain": "state_envelope_fields",
        "constraints": ["manifold_bounds_respected", "no_out_of_range_values"]
      },
      "gr_drift": {
        "domain": "flow_field_and_calm_load",
        "constraints": ["no_untracked_drift", "flow_integrates_to_calm_load"]
      },
      "gr_rev": {
        "domain": "core_solvers",
        "constraints": ["reversible_or_proven_one_way", "no_silent_irreversibility"]
      },
      "gr_guard": {
        "domain": "guardian_modulation",
        "constraints": ["warn_redirect_soften_respected", "no_solver_overrides_guardian"]
      },
      "gr_precl": {
        "domain": "precl_buffer_and_collapse",
        "constraints": ["no_geometry_activation", "no_governance_altitude_activation"]
      }
    },
    "rules": {
      "governance_isolation": true,
      "membrane_sovereignty": true,
      "precl_collapse": true,
      "delta_altitude_zero_ui": true,
      "non_recursive": true
    }
  }
}
```

---

#### 7. Provenance footer

```text
---
Artifact: NDH Runtime Guardrail Layer (v1.0)
Lane: Runtime Safety • Spectral Geometry

Purpose:
  Provide invariant-preserving guardrails around NDH spectral runtime physics,
  state, and solvers, ensuring altitude safety, drift neutrality, and PRECL
  collapse integrity.

Anchors:
  - NDH Runtime Spectral Physics Primer v1.0
  - NDH Runtime Spectral State Envelope v1.0
  - NDH Runtime Solver Layer v1.0
  - NDH Runtime Spectral Telemetry Channels v1.0
  - Spectral Runtime → UI Bridge v1.0
  - NDH Runtime README v1.0

Non-Activation Clause:
  This artifact is descriptive-only. It does not activate NDH geometry,
  governance altitude, adjacency engines, constellation routing, or runtime
  behavior.

Version: v1.0
Maintainer: Borealis S. Hedling
Location: Dublin, Ireland
Timestamp: 04 September 2026 — 03:40 IST
---
```
