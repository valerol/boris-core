# BOIS/Self transition package template

Used at operator message #50 and after #50 if the operator continues work.

## Package role
- `full_boot_transfer`: contains active base core/physiology plus memory/state or a verifiable pointer with SHA-256.
- `memory_snapshot`: contains memory/state only and is not a boot package.
- `bare_physiology`: physiology without memory, but with formation tools and QA.

## Required blocks for full transition
- package_role;
- active_source_order;
- active physiology version and SHA-256;
- D/V/S;
- accepted decisions;
- artifacts and links;
- open operator questions;
- open debts;
- active risks and STOP signals;
- rollback/fallback path;
- author support message if the package is delivered as a downloadable BOIS product or #50 transition package;
- loading instruction for the next chat;
- state_delta.
