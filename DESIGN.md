---
name: Biswash Rai — Personal Resume
colors:
  canvas: "#0A0A0F"
  surface: "#12121A"
  surface-2: "#1A1A24"
  border: "#262633"
  ink: "#EDEDF2"
  muted: "#9A9AAB"
  faint: "#6B6B7B"
  primary: "#7C5CFF"
  primary-soft: "#A78BFA"
  accent: "#22D3EE"
  success: "#34D399"
typography:
  fontFamily: "Inter, system-ui, -apple-system, sans-serif"
  mono: "JetBrains Mono, ui-monospace, monospace"
  body-md: "16px / 1.65"
  body-sm: "14px / 1.6"
  heading-xl: "clamp(2.5rem, 6vw, 4.25rem) / 1.05"
  heading-lg: "1.75rem / 1.2"
  heading-md: "1.125rem / 1.3"
rounded:
  sm: "8px"
  md: "14px"
  lg: "22px"
  full: "999px"
spacing:
  section: "96px"
  gutter: "24px"
components:
  button-primary: "bg-primary text-ink rounded-full px-5 py-2.5 font-medium hover:primary-soft transition"
  button-ghost: "border border-border text-ink rounded-full px-5 py-2.5 hover:surface-2 transition"
  card: "bg-surface border border-border rounded-lg p-6 hover:border-primary/40 transition"
  chip: "bg-surface-2 border border-border text-muted rounded-full px-3 py-1 text-sm"
---

# DESIGN.md — Biswash Rai Personal Resume

## Visual Theme
Dark, modern, "AI engineer" aesthetic. Refined and confident — deep near-black canvas, single violet accent,
subtle borders over drop shadows. Generous whitespace, crisp type, a single hero with photo. Feels like a
developer-tool landing page, not a paper CV.

## Design Principles
- Near-black canvas (#0A0A0F), flat surfaces with 1px borders, minimal shadows.
- One accent (violet #7C5CFF) used sparingly for highlights, links, and active states.
- One font family (Inter) + a mono stack for technical tags.
- Whitespace is structural: 96px section rhythm, 24px gutters.
- Subtle motion only: fade/slide on scroll, hover lifts on cards.

## Responsive Behavior
- Mobile: single column, reduced section spacing (64px), stacked header.
- Tablet/Desktop: two-column hero (photo + intro), multi-column skill grid.
- Breakpoints: 640px, 1024px.
