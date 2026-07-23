# DESIGN.md — Forge Blog Galaxy Control Room

## Intent

A calm, premium editorial control room for a portfolio that values evidence over
volume. It should feel like a night observatory crossed with a serious
publishing desk: deep ink, luminous data, restrained cosmic references and
paper-like reading surfaces. Never imitate an existing dashboard.

## Principles

1. **Evidence first** — the current pilot, gate and observed revenue dominate.
2. **One orbit at a time** — visually separate the active pilot from gated
   options.
3. **Quiet luminosity** — color signals hierarchy, not decoration.
4. **Editorial rhythm** — generous reading measure, short labels, precise
   numbers.
5. **Honest states** — research, gated and unknown are never styled as success.

## Tokens

- `--ink-950: #080a13` — page background
- `--ink-900: #101425` — primary surface
- `--ink-800: #191f36` — elevated surface
- `--paper: #f5f0e8` — primary copy
- `--mist: #aab3cc` — secondary copy
- `--violet: #8b7cff` — project identity
- `--cyan: #5ee7f4` — verified/active signal
- `--amber: #ffc86b` — research/attention
- `--coral: #ff7c91` — blocked/risk
- radius: 18 / 28 / 999 px
- shadow: diffuse, low opacity, no hard skeuomorphism

## Typography

Use a local system stack only. Headings are compact, high-contrast and slightly
tight. Body text targets 66 characters. Numeric states use tabular figures.

## Layout

- Desktop: 12-column grid, 1200 px maximum, hero split 7/5.
- Tablet: two columns when content remains readable.
- Mobile: one column, 390 px target, no horizontal scroll.
- Portfolio cards: active pilot spans more area; gated options remain quieter.

## Motion

Only ambient radial light and small hover/focus translations. Disable all
non-essential motion under `prefers-reduced-motion`.

## Accessibility

- Semantic landmarks and heading order.
- Visible `:focus-visible` ring in cyan.
- No state conveyed by color alone.
- Minimum 44 px interactive targets.
- Contrast checked against the declared background.

## Content rules

Never show synthetic traffic, fake revenue, fake agents working live or invented
progress. State the measurement date and distinguish target from observation.

