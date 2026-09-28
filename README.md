# EventOps — AI Knowledge Agent

An AI operations copilot for event directors: real-time readiness tracking,
vendor risk intelligence, AI-generated checklists, and a long-term memory
hub, originally designed in Google Stitch and assembled here into one
working app.

## Folder structure

```
eventops_project/
├── index.html            ← The full working app (all 4 screens + tab
│                            navigation + working buttons). Open this
│                            one in a browser to run the app.
├── DESIGN.md              ← Design system: colors, typography, spacing,
│                            component rules (from the original Stitch export)
├── screens/                ← The 4 original individual screens, each a
│   │                          standalone page (kept for reference/editing
│   │                          one screen in isolation)
│   ├── event_hub.html       — Live readiness, budget/queue risk, AI vendor
│   │                          swap recommendation
│   ├── vendor_intel.html    — Vendor reliability scores & delay-risk
│   │                          analysis
│   ├── checklists.html      — AI-generated, post-mortem-informed safeguard
│   │                          checklist
│   └── agent_memory.html    — Long-term memory hub with query box
└── assets/
    └── logo.png            ← App icon/logo
```

## How it fits together

`index.html` is the four `screens/*.html` files merged into a single page:
each screen's markup lives inside its own `<section data-panel="...">`
block, and the shared bottom nav bar switches between them by toggling
which section is visible — no page reloads. All the original interactive
buttons (vendor swap, checklist actions, memory search, etc.) are wired
with `addEventListener` so they work under a strict content-security
policy (inline `onclick="..."` attributes don't).

The individual `screens/*.html` files are self-contained on their own too
(each has its own copy of the Tailwind config and fonts), so you can open
any one of them by itself if you want to edit just that screen.

## Editing

- Change layout/content: edit the relevant file in `screens/`, then re-run
  the same merge (concatenate each screen's body into `index.html`'s
  matching `<section>`), or just edit `index.html` directly since it's
  plain HTML/Tailwind/JS with no build step.
- Colors, type, spacing: defined in `DESIGN.md` and mirrored in each file's
  inline Tailwind config block.
