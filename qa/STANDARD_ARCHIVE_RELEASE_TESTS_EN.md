# Standard archive release tests

This file is part of the Base core physiology. It lists the standard test set used when a BOIS-based archive is prepared for download or release.

1. Archive identity test: expected archive name, version, root folder and package_role are stated.
2. ZIP integrity test: the archive opens and CRC checks pass.
3. File inventory test: the file list is complete, intended and free of accidental nested deliverables.
4. Load-order test: load_order, active_source_order and layer/project boundaries are explicit.
5. Manifest test: manifest entries match the archive contents and exclude only generated integrity surfaces by rule.
6. SHA-256 test: every tracked file has a current checksum; no tracked hash fails.
7. JSON test: all JSON files parse and essential schema-like fields are present.
8. CSV test: all CSV files parse, headers are coherent, and rows have expected widths for their own language surface.
9. Active-rule ownership test: active rules, STOP signals, tests and criteria have owners and do not create hidden ownership drift.
10. English canonical PDF test: the English human-readable physiology PDF exists and contains the latest canonical rules for the layer/project.
11. Translation/projection test: Russian and machine-readable surfaces are translations or projections of the English canon, not higher canons.
12. PDF render test: every PDF inside the archive renders all pages without renderer errors.
13. DOCX render test: every DOCX intended for human use renders to pages without clipping, overlap or broken glyphs.
14. Surface contract test: required header, Detail, terminal copy blocks, author support and Versions/debt policies are present.
15. Author support test: BOIS/MaOS support message is included when the archive/product requires it and appears last in the final answer.
16. Local-vs-Versions test: local archive verification is separated from external Versions upload/verification state.
17. Versions debt precheck: before repeating an upload/verify debt, the target Versions folder is checked when access and folder identity are available.
18. Layered-debt test: debts are grouped by Self/Base and by each active project layer; project-owned accounts, platforms, sites and canonical links remain under that project.
19. Philosophical-logical and route-consistency test: the release does not contradict D/V/S, calculation route, authority boundary or evidence boundary; the declared calculation, verification, recovery, publication and debt routes are internally consistent and mutually compatible.
20. Self-closure test: the archive contains enough canonical, translated, machine, manifest, hash and QA surfaces to reload itself.
21. Anti-bureaucracy test: no new rule/organ remains if an existing owner can carry the function cleanly.
22. Positive-formulation test: active rules state the desired route first; restrictions protect that route and include repair action where possible.
23. Semantic-root test: if the archive is a repair release, the root defect and adjacent scenario retest are recorded.
24. Field-effectiveness test: QA-E field effectiveness remains not_claimed unless real external field evidence is present.
25. Final verify report test: a final verification JSON is generated and its status is PASS before the archive is offered.
26. Closed philosophical machine over time test: the archive is simulated as a self-contained philosophical machine across load, repair/release and next-state preparation. It must preserve Base Cycle Guard ownership, English canon priority, cycle continuity, route consistency, recovery path, layered/project ownership, and physiology hierarchy without degradation.
