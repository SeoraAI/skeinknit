# skeinknit.com

The marketing site for **Skein — Knit and Grade**, the iOS and Mac knitwear
grading app. Static HTML served by GitHub Pages from the repository root, with
`CNAME` pointing the apex domain at it.

The app itself lives in a different repository, `SeoraAI/skein-knit-and-grade`.
Nothing here builds, tests, or ships the app. If a request is about screens,
grading, or app behaviour, it belongs in that repository, not this one.

## No build step

There is no framework, no bundler, no package manager, and no test suite. Edit
the HTML and push. Each page carries its own CSS in a `<style>` block in the
head; there is no shared stylesheet, so a palette or type change has to be made
in each file that shows it.

Verify by reading the rendered markup and checking the page at a phone width.
There is no way to run anything here.

| File | What it is |
| --- | --- |
| `index.html` | The whole landing page, styles included |
| `support.html` | Real contact info. Apple requires the Support URL to lead here, not to the privacy policy |
| `privacy-policy.html` | Must describe what the app actually does |
| `terms-of-service.html` | Terms |
| `img/` | App screenshots used on the landing page |
| `og-image.png` | Social card image, 1200x630 |
| `robots.txt`, `sitemap.xml` | Crawling |
| `CNAME` | `skeinknit.com` |

## The palette mirrors the app

```
--cream:#FFFFFF  --paper:#F7F6F4  --ink:#1C1C1E   --taupe:#8E8E93
--sage:#8BA4A8   --spruce:#B8C9CC --clay:#D4776B  --line:#E8E5E0
```

These are the same values as `SkeinTheme` in the app. If one side changes, both
change. The wordmark is wide-tracked light caps, matching the app's nav titles.

## Every claim on this page has to be true

This is the rule that matters most here, and the one most easily broken by a
well-meaning edit.

- **Prices must match App Store Connect.** The page states an annual and a
  monthly price and a trial length. So does the JSON-LD block in the head, and
  so does the pricing section. All three have to agree with what the App Store
  actually charges.
- **Feature claims must match the shipped build**, not the roadmap. The app
  currently grades four sweater constructions across nine sizes. It does not do
  hats, socks, or shawls. Do not let aspirational copy describe them.
- **The free and paid split stated here is a promise.** Row counter, yarn stash,
  gauge tool, pattern library, and one fully graded size are free forever.
- **The privacy policy must match actual behaviour.** It names Mixpanel, says
  analytics are opt-out, and says data stays on the device. If the app's data
  handling changes, this page changes in the same breath.

A third-party site already publishes false claims about Skein. Do not add to the
problem from the official domain.

## Two things that have gone wrong before

- **The App Store button was a dead `href="#"` for ten weeks** while the app was
  live, so every visitor who tried to download it went nowhere. Check that link
  works after any edit to the hero or the calls to action.
- **The Support URL used to point at the privacy policy**, which does not
  satisfy Apple's requirement for reachable contact information. `support.html`
  exists for that reason. Keep it reachable from the footer.

## Structured data and SEO

The head of `index.html` carries a JSON-LD `SoftwareApplication` block plus
Open Graph and Twitter card tags. The description, price, and operating system
in that block are duplicated from the visible page. Change one, change both, or
search results will disagree with the page they link to.

`sitemap.xml` lists every page. Add new pages to it.

## Email signup

The signup section embeds a Kit (formerly ConvertKit) inline form as a script
tag that mounts the form where it sits. It is a real form with a real form ID,
not a placeholder. Do not replace it with a `mailto:` link, which is what it
used to be.
