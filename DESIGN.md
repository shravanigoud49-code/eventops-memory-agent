---
name: Kinetic Operational Intelligence
colors:
  surface: '#0d1322'
  surface-dim: '#0d1322'
  surface-bright: '#33394a'
  surface-container-lowest: '#080e1d'
  surface-container-low: '#151b2b'
  surface-container: '#191f2f'
  surface-container-high: '#242a3a'
  surface-container-highest: '#2f3445'
  on-surface: '#dde2f8'
  on-surface-variant: '#c7c4d7'
  inverse-surface: '#dde2f8'
  inverse-on-surface: '#2a3040'
  outline: '#908fa0'
  outline-variant: '#464554'
  surface-tint: '#c0c1ff'
  primary: '#c0c1ff'
  on-primary: '#1000a9'
  primary-container: '#8083ff'
  on-primary-container: '#0d0096'
  inverse-primary: '#494bd6'
  secondary: '#4edea3'
  on-secondary: '#003824'
  secondary-container: '#00a572'
  on-secondary-container: '#00311f'
  tertiary: '#ffb95f'
  on-tertiary: '#472a00'
  tertiary-container: '#ca8100'
  on-tertiary-container: '#3e2400'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffddb8'
  tertiary-fixed-dim: '#ffb95f'
  on-tertiary-fixed: '#2a1700'
  on-tertiary-fixed-variant: '#653e00'
  background: '#0d1322'
  on-background: '#dde2f8'
  surface-variant: '#2f3445'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.025em
  headline-xl-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  label-numeric:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.06em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 0.75rem
  gutter-tablet: 1rem
  margin: 1rem
  margin-tablet: 1.5rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-lg: 1.25rem
  space-xl: 1.75rem
---

## Brand & Style

This design system expresses authoritative situational awareness, proactive operational intellect, and real-time mission readiness. Tailored specifically for high-stakes event executives, floor directors, and field leads, the visual style blends disciplined technical ergonomics with a sophisticated intelligence layer. 

The aesthetic is precision-engineered: dark obsidian-slate architectural foundations paired with crisp, high-legibility functional surfaces, accented by razor-sharp predictive telemetry. Surfaces project structural clarity rather than ornamental gloss—delivering high data density without cognitive saturation. The user interface communicates certainty, speed, and continuous systemic adaptation.

## Colors

The system uses a calibrated dual-tier environment optimized for intense lighting fluctuations (from backlit production control rooms to outdoor field deployments):

- **Foundation Slate Core:** The viewport canvas relies on Deep Slate (#0B1120) and Structure Charcoal (#1E293B) to minimize glare and maximize contrast ratios for operational dashboards.
- **Surface Elevation Cards:** Primary operational modules, log monitors, and risk telemetry cards use high-clarity Off-White (#F8FAFC) to Pure White (#FFFFFF) foreground surfaces when surfacing daytime task checklists, or deep-sheen structured sub-slates (#131D31 and #1E293B) within core views.
- **Predictive Intelligence (Indigo/Violet #6366F1, #4F46E5):** Reserved exclusively for active machine learning telemetry, automated schedule optimizations, probabilistic staffing forecasts, and executive AI action suggestions.
- **Operational Status & Risk Flags:** 
  - Cautionary Amber (#F59E0B) flags vendor variances, queue bottlenecks, and critical path timeline shifts.
  - Critical Coral (#EF4444) demands immediate incident escalation and emergency deployment overrides.
  - Emerald Mint (#10B981) validates verified milestone completions, safe capacity thresholds, and locked post-event telemetry.

## Typography

Typography prioritizes micro-legibility and spatial economy:

- **Plus Jakarta Sans:** Provides balanced geometric headlines that remain friendly yet sharp under stress.
- **Inter:** Drives all operational content, logs, dynamic narrative summaries, and user inputs to maximize scanning speed across varying device pixel densities.
- **JetBrains Mono:** Reserved for timestamps, attendee count gauges, run-of-show cues, predictive confidence percentages, and delta indicators. 

Numbers must render with tabular figures (`tnum`) across all telemetry readouts to eliminate horizontal layout jitter during real-time updates.

## Layout & Spacing

The layout model is mobile-first, prioritizing thumb-zone reachability and critical mission density:

- **Mobile Viewport Grid:** Operates on a 4-column fluid structure with tight 12px (`gutter`) gutters and 16px (`margin`) outer screen margins, preserving maximum surface area for high-density monitoring feeds.
- **Vertical Rhythm:** Relies on an 8-point spatial cadence, dropping to 4-point micro-spacing (`space-xs`) for internal card metadata, badge padding, and metric grouping.
- **Tablet Expansion:** Adapts to a 6-to-8 column structure with 16px gutters and 24px margins, introducing sticky side-rail telemetry summaries alongside live stream checklists.
- **Touch Targets:** Interactive action points strictly adhere to a minimum 44px vertical dimension, regardless of compact text sizes.

## Elevation & Depth

Visual hierarchy uses a refined hybrid of tonal surface layering and precise, low-contrast structural outlines:

- **Canvas Foundation:** Layer 0 sits at Deep Slate (#0B1120).
- **Structural Elevation:** Cards and panels (Layer 1) reside at Deep Navy (#131D31) or crisp contrasting white (#FFFFFF) for focused action modes, outlined by a 1px border of Slate Alpha (`rgba(255, 255, 255, 0.08)` on dark or `rgba(15, 23, 42, 0.08)` on light).
- **Proactive Intelligence Glow:** AI recommendation nodes introduce subtle directional ambient drop-shadows with violet tinting (`box-shadow: 0 4px 20px -2px rgba(99, 102, 241, 0.18)`), creating instant focal contrast against standard operational logs.
- **Modal & Critical Sheets:** Bottom sheets and alert drawers (Layer 2) leverage a dark translucent backdrop blur (`backdrop-filter: blur(12px)`) framed by a distinct 1px border highlight at the top edge.

## Shapes

The design system enforces a soft, disciplined geometry (`roundedness: 1`). Metric pods, incident cards, and interactive chips use 4px (`0.25rem`) inner radii and 8px (`0.5rem`) outer radii. This restrained curvature communicates industrial efficiency and allows dense metric grids to nest tightly without circular dead space. Modal sheets and primary CTA floating bars transition to 12px (`0.75rem`) along top edges to soften structural framing.

## Components

### Buttons & Action Bars
- **Predictive AI Actions:** Saturated Indigo background (#6366F1), white text, 8px radius, paired with a leading micro-sparkle icon. Displays active gradient shimmer during background inference.
- **Standard Primary:** Slate Light (#F8FAFC) background with dark ink (#0B1120) text on dark canvas for high-visibility operational triggers.
- **Risk Override:** Crimson border (#EF4444) with tinted fill (`rgba(239, 68, 68, 0.12)`) and bold label.

### Chips & Telemetry Badges
- **Status Indicators:** 4px radius with monospace metrics. 
- Emerald Mint chip (`#10B981` at 10% opacity, `#10B981` solid text) for "NOMINAL".
- Amber chip (`#F59E0B` at 12% opacity, `#F59E0B` solid text) for "DELAY DETECTED".
- Indigo chip (`#6366F1` at 15% opacity, `#818CF8` text) for "AI SUGGESTION READY".

### Structured Operational Risk Cards
- Contain a top status border accent (2px solid in status color).
- Group data using a 2-column key-value matrix (Time Impact / Variance Percentage) rendered in `label-numeric`.
- Inline quick-action triggers sit at the bottom edge, spanning full card width.

### AI Operational Recommendation Widgets
- Framed in subtle indigo gradient outlines (`border: 1px solid rgba(99, 102, 241, 0.3)`).
- Header features an "AI Reasoning" micro-tag with a dynamic confidence score (e.g., "94% CONFIDENCE").
- Split layout: human-readable rationale on top, single-tap acceptance button below ("Execute Re-route", "Approve Schedule Shift").

### Form Inputs & Checklists
- Minimalist inset boxes with 1px border (`#334155`). Focus state introduces a crisp #6366F1 ring.
- Checklists feature auto-sorting based on dynamic operational priority determined by real-time run-of-show drift.