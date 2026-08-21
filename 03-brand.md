# Bramble brand

*Built on the Refinery Labs palette and type.*

---

## 1. Colour

### Primary

Forest and Sage lead. Forest carries the header band, every panel title, the tile figures and all trend lines. Sage is its light counterpart.

| | Hex | Where it is used |
|---|---|---|
| **Forest** | `#1F3D2E` | Header band, panel titles, tile figures, trend lines, positive bars |
| Forest light *(derived)* | `#2E6B4A` | Positive change, hover states |
| **Sage** | `#90A682` | Logo mark, source status dot, "back to normal" badges |

### Secondary

Clay is the warm counterweight. It carries the active tab and every negative bar, which is what puts warmth across the whole screen rather than leaving it all green.

| | Hex | Where it is used |
|---|---|---|
| **Clay** | `#B7845A` | Active tab underline, negative bars, above-range points |
| Clay deep *(derived)* | `#9C6A42` | Clay text on a tint |
| **Ivory** | `#FAF8F3` | Wordmark and text on the Forest band |

### Accent and ink

Navy is text and tooltips only, not a surface. Teal is held back for links and secondary actions so it does not compete with Forest. Brick handles anything genuinely wrong.

| | Hex | Where it is used |
|---|---|---|
| **Deep Navy** | `#0F1B2D` | Primary text, tooltip background |
| **Teal** | `#0D5D63` | Links and secondary actions |
| Brick *(derived from Clay)* | `#A14A32` | Safety flags, alert count, negative change |

### Neutrals

Sand is the page, not a border colour. Everything sits on it and the panels lift off it. Five steps derived so a dense table has enough range.

| | Hex | Where it is used |
|---|---|---|
| **Sand** | `#E2DACB` | Page background |
| Sand deep *(derived)* | `#CFC5B2` | Table header rules, neutral bar in split charts |
| Sand edge *(derived)* | `#C0B49D` | Panel borders |
| Card *(derived)* | `#FDFCF8` | Panel surfaces |
| Card tint *(derived)* | `#F4F0E6` | Sub bar, tags, hover |
| Warm grey *(derived)* | `#857D6F` | Axis labels and captions |
| Slate *(derived)* | `#4A5563` | Secondary text |

### Badge tints

Each one is a different hue, not three variations of beige. This was the readability problem in the last version.

| Badge | Fill | Text | Border |
|---|---|---|---|
| Back to normal | `#E1EBD6` green | `#1F3D2E` | `#BFD1AC` |
| Source behind, watch | `#F6E2C6` amber | `#8A6224` | `#E3C58F` |
| Above usual range, safety | `#F0D6CB` rose | `#94402A` | `#E0B7A6` |
| Neutral | `#F4F0E6` | `#4A5563` | `#C0B49D` |

### Charts

Forest for positive and for every trend line, Sand deep for neutral, Clay for negative, Brick for anything above its usual range.

---

## 2. Typography

| Use | Typeface | Fallback |
|---|---|---|
| Wordmark, tabs, panel titles | **Source Serif 4** | Georgia, serif |
| Everything else, including every number | **Inter** | system-ui, Segoe UI, sans-serif |

The reference sheet names Calibre Serif, which cannot be sourced. Source Serif 4 is the closest available match. Numbers stay in Inter throughout, because serif figures do not line up in a column.

---

## 3. Surfaces and shape

The page is Sand and the panels are near-white with a Sand edge border and a soft green-cast shadow, so cards read as sitting on the surface rather than being drawn on it. Panel titles sit above a Sage hairline. Radius 10px on cards, 8px on controls, 20px on badges. Tiles lift on hover.

The Forest band runs full width and holds the wordmark, the tabs and the source status. Nothing else on the page is a solid block of colour.

## 4. The mark

Three overlapping circles in Sage, Clay and Ivory, a bramble berry at its simplest. Inline SVG, readable at 16px.

## 5. Dark mode

Built from Forest rather than by inverting the light theme. Page `#101A15`, panels `#18241D`, band `#0C1A13`. Forest, Sage, Clay and Brick each lift to a brighter step to hold against the dark surface.
