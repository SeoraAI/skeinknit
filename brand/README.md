# Skein logo

Clean vector versions of the Skein logo, redrawn 2026-11-17 to replace the
AI-rendered lettering in the branding image collection.

- **Mark:** the S from the app icon, rebuilt from exact geometry: two equal
  rings whose centres sit two radii apart, each cut through 230 degrees,
  ring thickness 36% of the centreline radius.
- **Wordmark:** SKEIN in Inter ExtraLight (200), capitals tracked 0.42em,
  the same treatment as the site header and the app's navigation titles.
  Converted to outlines, so no font is needed to display it.

| File | Use |
| --- | --- |
| `skein-mark-*.svg` | The S on its own |
| `skein-wordmark-*.svg` | SKEIN on its own |
| `skein-lockup-horizontal-*.svg` | Mark beside the word: headers, letterhead |
| `skein-lockup-stacked-*.svg` | Mark above the word: covers, square posts |
| `skein-app-icon.svg` | Ink mark on card cream, 1024 square |
| `skein-avatar.svg` | Cream mark on chestnut, sized for a circular crop |

Each comes in `ink` (#2B1F18), `chestnut` (#8A4B2F) and `cream` (#FAF6F0,
for dark backgrounds), as SVG and as a PNG export. Colours are the app's
`SkeinTheme` palette; if that changes, change these with it.

To rebuild after a change: `pip install fonttools cairosvg`, then
`python3 brand/make-logo.py` for the SVGs. The PNGs were exported from the
SVGs with cairosvg at 2000 px wide (1024 for the icon and avatar).
