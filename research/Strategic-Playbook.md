# 📔 Strategic Playbook: The Local Lead-Gen Framework

This playbook outlines the "Authority Flex" and "Structured Intelligence" strategy used for **No Dig Canada**. This framework is designed to be repeatable for any local service niche (HVAC, Landscaping, Roofing, etc.).

---

## 🏗️ Phase 1: High-Definition Intelligence
*Goal: Map the entire competitive landscape using automated crawling.*

1.  **Identify "Authority Rivals":** Find the competitors who have the most "Technical" or "High-End" look, not just the biggest ones.
2.  **Firecrawl Ingestion:** Use `tools/firecrawl-researcher/` to crawl the complete sitemaps of the top 5 rivals.
3.  **Gap Analysis:**
    *   What technical standards do they cite? (e.g., ASTM for pipe lining).
    *   What is their "Low-Hanging Fruit" offer? (e.g., "$93 Drain Cleaning").
    *   What locations do they have dedicated pages for?

## 🛡️ Phase 2: The "Authority Flex" Strategy
*Goal: Use high-level expertise to build residential trust.*

1.  **The Authority Lever:** If the business does any Municipal, Industrial, or Commercial work, **lead with it.** 
    *   *Logic:* "If the City trusts them to fix a main sewer line, I can trust them to fix my toilet."
2.  **Trust Architecture:** Place a "Trusted By" banner immediately under the Hero section.
3.  **Technical Credibility:** Create a "Certifications" or "Technology" section that explains the *how* using professional industry terms, then translate them into benefit-driven language for homeowners.

## 🎯 Phase 3: SEO Dominance (Local Clustering)
*Goal: Dominate Google Maps and local searches.*

1.  **The "Location Page" Factory:** Create 100% unique landing pages for every city in the target region.
    *   *Template:* `[Service] in [City] | [Company Name]`
    *   *Content:* Mention local landmarks, weather patterns affecting the service, and city-specific problems.
2.  **Schema Hook:** Use JSON-LD `LocalBusiness` schema with `serviceArea` defined to tell Google exactly where the business operates.

## 🎨 Phase 4: High-Impact Design
*Goal: Use visual psychology to close the lead.*

1.  **Trust Palette:** 
    *   **Primary:** Deep Navy (#0b1121) = Security/Authority.
    *   **Secondary:** Safety Orange (#fb8c00) or High-Vis Yellow = Action/Industry.
2.  **Micro-Interactions:** Use subtle hover effects on CTA buttons to make the site feel "alive" and premium.
3.  **CTA Contrast:** Ensure the primary "Get a Quote" button is the most vibrant element on the page.

---

## 🛠️ Reusable Tools Setup
*   **Workflow:** `.agent/workflows/competitor-research.md` (Already created)
*   **Scraper:** `tools/firecrawl-researcher/crawl_competitors.py` (Already created)
