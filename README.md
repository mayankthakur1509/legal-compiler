MintSite Enterprise – Multi-Lawyer Legal Compiler (Phase 1)

What this build does:
- Multi-lawyer authority pages
- Multi-persona pages (CFO / CPA / Client)
- Multi-practice area expansion
- FormFree download page per lawyer
- Semantic ontology scaffold

How to run:
1. pip install pyyaml python-slugify
2. python compiler/compile.py
3. Deploy /dist folder to Cloudflare Pages

Routing in this phase:
/lawyers/<slug>/index.html
/lawyers/<slug>/persona-cfo.html
/lawyers/<slug>/persona-cpa.html
/lawyers/<slug>/persona-client.html
/lawyers/<slug>/formfree.html
