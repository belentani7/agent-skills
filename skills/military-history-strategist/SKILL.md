---
name: military-history-strategist
description: Researches, structures, and writes historical military campaigns, battles, strategy, factions, and orders of battle — for worldbuilding a fictional war, designing a wargaming/tabletop scenario, running a persistent narrative campaign, or analyzing a real historical conflict. Use this whenever the user is building a war, battle, campaign, army, faction, siege, or military conflict for a story, game, or historical study — even if they just say "battle scene", "army list", "faction", "what would have happened if [historical war]", or ask about a real commander/campaign/doctrine/logistics. Maintains persistent campaign state across sessions so a world keeps evolving instead of resetting each time — trigger it again on any follow-up about a campaign already in progress.
---

# Military History Strategist

Wars, on the page or on the table, fall apart the same way: factions want things
that don't connect to what they actually do about it, battles happen in
geography that doesn't constrain anyone, and outcomes don't follow from the
forces and decisions involved. This skill exists to keep the causal chain
intact — who wants what, what they can actually field, where the ground and
supply lines force their hand, and how that produces the battle or campaign
in question. That discipline is what makes a real historical analysis useful
*and* what makes a fictional war or wargame scenario feel inevitable rather
than arbitrary.

## Mode: real history vs. fiction/game — don't ask, infer and say so

Figure out from the request which mode applies, state your read in one line,
and proceed. Only ask if it's genuinely unclear (e.g., a fantasy-sounding
faction name paired with a request for "accurate" logistics).

- **Real historical analysis**: ground everything in actual sources and
  events. Flag speculation clearly ("this is inference, not attested") and
  don't invent unit numbers or quotes that aren't in the record.
- **Fiction / worldbuilding / wargaming**: invent freely, but borrow the
  *mechanics* of real warfare for the era and tech level involved (see
  `references/eras.md`) so the result holds together. A fictional war is
  allowed to have dragons; it is not allowed to have supply lines that make
  no sense once you remove the dragons.

## Persistent campaign state — the "vida propia" part

A one-shot answer forgets everything the moment the conversation ends. This
skill instead keeps a campaign alive across sessions:

1. **On first use for a given war/campaign**, ask (or infer from context)
   what to call it, then create `campaigns/<slug>/state.md` in the current
   project (create the `campaigns/` folder if it doesn't exist). This file is
   the campaign's memory — factions, forces, terrain, timeline of events,
   decisions made, and current state of the world. Structure it with the
   sections from "Output structure" below, kept current rather than
   append-only.
2. **On every subsequent use that touches the same campaign**, read
   `campaigns/<slug>/state.md` first. Treat everything in it as established
   fact — don't silently contradict a faction's stated strength, a battle's
   recorded outcome, or a timeline date from a prior session. If the user
   asks for something that *would* contradict it, point out the conflict
   instead of quietly overwriting history.
3. **After producing new material** (a battle resolved, a decision made, a
   faction's fortunes changed), update `state.md` to reflect the new
   present — advance the timeline, adjust force strengths, record what
   happened. The campaign should read like it kept living while you were
   away, not like it's being reconstructed from scratch each time.
4. If the user is clearly just asking a one-off historical question with no
   ongoing campaign in mind ("what happened at Cannae"), skip all of this —
   state is for campaigns being built or run, not every question.

## Output structure

Use judgment on how much of this a given request actually needs — a
one-battle skirmish doesn't need a full campaign timeline, and a single
historical question doesn't need any of it. For a full campaign or scenario,
this is the shape `state.md` (and most substantial answers) should take:

```markdown
# [Campaign/Battle name]

## Context
Era, tech level, scale (skirmish / battle / campaign / war), what's actually
at stake for each side.

## Factions & Forces
Per faction: goals, leadership, order of battle (unit types and rough
strength — don't fabricate precise historical numbers that aren't attested;
for fiction, numbers should still be plausible for the logistics involved).

## Terrain & Logistics
The geography that constrains movement, supply lines and what happens if
they're cut, season/weather if relevant, and how each faction's supply
situation shapes what they can actually attempt.

## Timeline / Order of Events
Chronological. For an ongoing campaign, this is the section that grows each
session — most recent events last.

## Key Decision Points
The moments where a commander's choice (not just force ratios) determined
what happened next, and why that choice made sense to them at the time.

## Outcome & Analysis
What happened and the causal reasoning for why, tied back to forces, terrain,
logistics, and decisions above — not asserted as a conclusion floating free
of the rest of the document.

## Branches (fiction/wargaming only)
Plausible "what if" divergences the user can pick up and run with, each
grounded in a specific decision point rather than an arbitrary twist.
```

## For wargaming scenario design specifically

Translate the above into what a game table needs: relative unit strengths
and matchups (not tied to one ruleset unless the user names one), objectives
per side that create actual tension rather than a foregone conclusion, and a
turn/phase structure that follows from the logistics already established —
if supply is the bottleneck in the fiction, make it the bottleneck on the
table too.

## Reference material

`references/eras.md` has quick-reference notes on how warfare's mechanics —
command reach, logistics, dominant arms, typical battle duration — shift
across eras (ancient, medieval, gunpowder, industrial, modern). Read the
relevant section when grounding a fictional scenario or sanity-checking a
historical claim against the tech level involved; don't load the whole file
for a question that only touches one era.
