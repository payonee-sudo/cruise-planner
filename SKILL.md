---
name: family-cruise-planner
description: Create or update a Korean, browser-ready family cruise planner that compares themes, regions, cruise lines, departure months, sailing lengths, budgets, shore excursions, and booking channels. Use for family cruise schedule HTML, cruise itinerary comparison, or a practical cruise decision tool; do not treat seasonal examples or estimated prices as confirmed inventory.
---

# Family Cruise Planner

Build the decision tool itself, not a promotional page. Let a user choose family composition, one of ten travel themes, region, departure month, cruise line, sailing length, and cabin class, then show usable itinerary and budget recommendations immediately.

## Required behavior

- Cover departure months from 2026 Q4 through December 2030.
- Include the eight requested region groups: Eastern Mediterranean, Western Mediterranean, Alaska, Eastern Caribbean, Western Caribbean, Southeast Asia, Northeast Asia, and Other.
- Include mainstream cruise lines led by Royal Caribbean, Norwegian Cruise Line, and Disney Cruise Line, with sensible regional alternatives.
- Offer exactly ten clear themes spanning children, parents, distance, nature, heritage, cities, relaxation, food, first-time cruising, and milestone travel.
- Filter or rank itinerary candidates by seasonal fit, duration, cruise line, theme, and family composition.
- Estimate a range rather than a single guaranteed price. Break out cruise fare, taxes and gratuities, flights, pre/post hotel, and shore excursions in KRW.
- Recommend port activities with mobility and child suitability where relevant.
- Present booking channels as comparison options, never as a guaranteed cheapest seller. Encourage an apples-to-apples comparison of cabin category, taxes, gratuities, onboard credit, cancellation terms, and change support.

## Data integrity

Read [references/planning-rules.md](references/planning-rules.md) before adding or changing itinerary, price, seasonality, or booking guidance. Future cruise inventory changes often: distinguish official bookable inventory from season-pattern planning, show the data/reference date, and link users to live searches before purchase.

When an exact sailing has not been verified, label it `계절 운항 예상` or `판매 일정 확인 필요`. Never invent a ship name, departure date, fare, or remaining cabin count.

## Deliverable

Prefer a responsive, accessible single-file HTML experience when the user asks for HTML. Keep JavaScript and CSS self-contained unless image assets are deliberately included. Reuse `dist/index.html` as the starter for similar requests and adapt its visible text and data to the user's requirements.

Before handoff, verify that every filter works, at least one recommendation is visible on load, unavailable month-region combinations are explained, estimates update when party size or cabin changes, external links are real HTTPS URLs, and the page has no horizontal overflow on mobile.
