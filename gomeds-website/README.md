# GoMeds 24/7 Website Redesign — Preview Build

This is a static, multi-page website project built around the exact GoMeds logo supplied for the design. It includes the current important routes plus Health Timeline, GoMeds PRO, Medicines, Healthcare Partners, Research Partnerships, and an Institutional Collaboration information page.

## Pages included

- `/` — redesigned homepage
- `/about`
- `/contact`
- `/privacy`
- `/return-policy`
- `/terms-conditions`
- `/pharmacy-terms-conditions`
- `/health-timeline`
- `/pro`
- `/medicines`
- `/healthcare-partners`
- `/research`
- `/institutional-collaboration`

Each route has its own folder and `index.html`. Assets and JS/CSS are referenced from root paths (`/assets/...`), so deploy this project at the domain root, not inside a nested subdirectory, unless paths are updated.

## Preview locally

From this folder, run a local static server:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/`.

The form currently uses `mailto:` as a transparent temporary action. It does not submit to a server. Before production, connect a secure form handler or CRM endpoint and test its privacy/security settings.

## Important production checks

1. **Official logo:** `assets/gomeds-official-logo.png` is the exact image supplied by the user and is used without redrawing or cropping. It is intentionally displayed with its original turquoise background and proportions.
2. **Anatomical illustration:** `assets/anatomy-3d-illustration.webp` is a generated 3D anatomical illustration with interactive CSS parallax and clickable system hotspots. It is not a rotatable clinical 3D model or diagnostic tool. If true geometry-level rotation is needed, replace it with a properly licensed 3D model and an implemented Three.js/React Three Fiber viewer.
3. **Institutional collaboration:** The current copy remains cautious because the uploaded draft MoU was unsigned and required public-disclosure approval. After signing, confirm the executed scope and written permission to announce/use the institution's name/logo before activating stronger public claims.
4. **GoMeds PRO:** The page reflects the planned three-touchpoint package: 128, 64 and 64 parameters; ₹3,999 for one person/year and ₹6,999 for two/year. Confirm the final clinical calendar and exact commercial inclusions before accepting payments.
5. **Legal pages:** The existing routes are retained in a redesigned layout, but the content is not legal advice. Privacy Policy needs a substantive review before launch. The current privacy page contains dated legal references, indefinite-retention statements and an unresolved jurisdiction placeholder. The site's homepage says zero pharmacy commission while the published Partner Pharmacy Terms give broad power to set/deduct commissions. Resolve this contradiction before publishing.
6. **Contact consistency:** The live site and app listings have different contact number presentations. The build uses `+91 75758 48500` from the Contact page; confirm the canonical public support number.
7. **Operational claims:** Check delivery times, coverage area, free-delivery terms, medicine substitutions and app-store links before launch.
8. **Backend:** There is no live health-record database, account system, consent management, real report upload, checkout or research dataset connected to this static design. Those functions must be integrated and security-reviewed before being advertised as available.
9. **Accessibility/performance:** The anatomy section uses a large generated image; compress it for production, run Lighthouse/accessibility checks, and retain the non-animated fallback for reduced-motion and lower-powered devices.

## Structure

- `index.html` and each route's `index.html`: static shell
- `assets/site.css`: responsive design system
- `assets/site.js`: route content and interactions
- `assets/gomeds-official-logo.png`: exact logo asset supplied by the user
- `assets/anatomy-3d-illustration.webp`: 3D anatomical hero illustration

This is a frontend preview build, not a deployed change to `gomeds247.com`.
