#!/usr/bin/env python3
"""
Möbii³us MCP Workbook for Analogs
Combines functions from multiple system documents into a structured
MCP tool catalog, crosswalk, and deployment reference.
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import FormulaRule, ColorScaleRule
from openpyxl.chart import BarChart, Reference

wb = Workbook()

# Styles
header_font = Font(name="Arial", bold=True, size=12, color="FFFFFF")
title_font = Font(name="Arial", bold=True, size=16, color="1A1A40")
section_font = Font(name="Arial", bold=True, size=11, color="1A1A40")
body_font = Font(name="Arial", size=10)
mono_font = Font(name="Consolas", size=9)
blue_fill = PatternFill("solid", fgColor="2E5090")
purple_fill = PatternFill("solid", fgColor="5B2C6F")
teal_fill = PatternFill("solid", fgColor="0E6655")
amber_fill = PatternFill("solid", fgColor="B9770E")
light_blue = PatternFill("solid", fgColor="D6EAF8")
light_purple = PatternFill("solid", fgColor="E8DAEF")
light_teal = PatternFill("solid", fgColor="D5F5E3")
light_amber = PatternFill("solid", fgColor="FCF3CF")
light_gray = PatternFill("solid", fgColor="F4F6F7")
green_fill = PatternFill("solid", fgColor="27AE60")
red_fill = PatternFill("solid", fgColor="C0392B")
thin = Border(
    left=Side(style="thin", color="BFBFBF"),
    right=Side(style="thin", color="BFBFBF"),
    top=Side(style="thin", color="BFBFBF"),
    bottom=Side(style="thin", color="BFBFBF"),
)
center = Alignment(horizontal="center", vertical="center", wrap_text=True)
left_align = Alignment(horizontal="left", vertical="center", wrap_text=True)

def style_header(ws, row, cols, fill=blue_fill):
    for col in range(1, cols + 1):
        cell = ws.cell(row=row, column=col)
        cell.font = header_font
        cell.fill = fill
        cell.alignment = center
        cell.border = thin

def auto_width(ws, min_w=10, max_w=45):
    from openpyxl.cell.cell import MergedCell
    for col in ws.columns:
        max_length = 0
        column = None
        for cell in col:
            if isinstance(cell, MergedCell):
                continue
            if column is None:
                column = cell.column_letter
            try:
                if cell.value:
                    max_length = max(max_length, min(len(str(cell.value)), 80))
            except Exception:
                pass
        if column:
            ws.column_dimensions[column].width = min(max(max_length + 2, min_w), max_w)

# ═══════════════════════════════════════════════════════════
# SHEET 1: Overview
# ═══════════════════════════════════════════════════════════
ws = wb.active
ws.title = "01_Overview"

ws["A1"] = "Möbii³us MCP Workbook for Analogs"
ws["A1"].font = title_font
ws.merge_cells("A1:F1")

ws["A2"] = "Combined System Functions → MCP Tool Catalog · Trust Floor α=0.743 · Generated 2026-11-05"
ws["A2"].font = Font(name="Arial", size=10, italic=True, color="555555")
ws.merge_cells("A2:F2")

ws["A4"] = "PURPOSE"
ws["A4"].font = section_font
ws["A5"] = (
    "This workbook synthesizes functions from the Möbii³us fullerene-sedenion architecture, "
    "MOTIIV8II(IONS) synthesis package, MCP server reference (TypeScript + Neo4j), "
    "MöbiiiOS Coherence Bridge, adaptive-cycle ecosystem patterns, distributed domain infrastructure, "
    "skill-integration audit, and skill-library snippets into a single MCP-oriented analog registry. "
    "Each row maps a native system capability to a proposed MCP tool signature that can be implemented "
    "under the Evidence Clamp / Guardian Gate (trust floor 0.743)."
)
ws["A5"].alignment = left_align
ws.merge_cells("A5:F5")
ws.row_dimensions[5].height = 80

ws["A7"] = "SOURCE SYSTEMS INGESTED"
ws["A7"].font = section_font

headers = ["ID", "System / Document", "Primary Domain", "Key Primitives", "MCP Relevance", "Status"]
for i, h in enumerate(headers, 1):
    ws.cell(row=8, column=i, value=h)
style_header(ws, 8, 6, purple_fill)

sources = [
    ("S01", "Fullerene-Sedenion arXiv Module Registry", "Λ.core / Quantum", "C60 mesh, QuantumBridge, Chern sectors, Ising map", "Hardware-mapped quantum tools", "Scaffold"),
    ("S02", "MOTIIV8II(IONS) Deployment Manifest", "Event Kernel", "MobiusEvent, Guardian Stamp, Tee+latch+unify, ledger", "Core process / ethics tools", "Locked v1.0"),
    ("S03", "Native MCP Server + Neo4j Reference", "MCP Runtime", "resolve_coordinate, semantic_search, traverse_lineage", "Direct tool implementation guide", "Production API"),
    ("S04", "MöbiiiOS × MCP Coherence Bridge (TSX)", "Triadic Fusion", "FractalCrystalCore, triadicFuse, 16 domains, modes", "Live UI + domain desire tools", "Bridge draft"),
    ("S05", "Engineering Cycles & Seasons (Adaptive Cycle)", "Lifecycle / Resilience", "Holling adaptive cycle, panarchy, disturbance, keystones", "Lifecycle management tools", "Design pattern"),
    ("S06", "Distributed Domain Infrastructure Audit", "Infra / Domains", "Monorepo, 8 domains, shared components, deploy workflows", "Deploy & registry tools", "Blueprint"),
    ("S07", "Skill-Integration Audit (Quad-Parse)", "Skill Pipeline", "mobius-vocabulary, skill-creator, mcp-builder, algorithmic-art", "Skill minting & governance tools", "Audit ready"),
    ("S08", "Skill Library Extension (13+1 snippets)", "Library / Snippets", "B0X bundle, SCUBAStream, everybuddy atlas, superdense core", "Snippet ingestion tools", "INTRA/INTER"),
    ("S09", "System Architecture + 90-Day Roadmap", "Kähler / Geometry", "Kähler weave, Hopf fibration, spiral indexer", "Coordinate & retrieval tools", "Research synth"),
]

for r, row in enumerate(sources, 9):
    for c, val in enumerate(row, 1):
        cell = ws.cell(row=r, column=c, value=val)
        cell.font = body_font
        cell.alignment = left_align
        cell.border = thin
        if r % 2 == 0:
            cell.fill = light_gray

ws["A19"] = "CONSTANTS (Möbii³us Canon)"
ws["A19"].font = section_font

const_headers = ["Symbol", "Value", "Role", "Source"]
for i, h in enumerate(const_headers, 1):
    ws.cell(row=20, column=i, value=h)
style_header(ws, 20, 4, teal_fill)

constants = [
    ("α (alpha)", 0.743, "Trust floor / Caputo weight / hysteresis", "Guardian / MOTIIV / Bridge"),
    ("φ (phi)", 1.618, "Golden ratio / spiral scaling", "Architecture roadmap"),
    ("TWIN", "8009 / 8011", "Twin-prime carriers / ports", "Bridge / skill ports"),
    ("HZ", 4.6, "Base cycle frequency", "Bridge live engine"),
    ("Coherence target", 0.987, "Locked package coherence", "MOTIIV manifest"),
    ("Chern targets", "±2, ±1, 0", "Topological sectors for Guardian Gate", "Fullerene QuantumBridge"),
    ("42+1 Canon", "42 faces + HOME", "Mesh + Min v1.0", "MOTIIV / Architecture"),
    ("Seven Gates", "Ethics layer", "ROUTE / BRAKE / FORBID decisions", "MOTIIV Guardian"),
]

for r, row in enumerate(constants, 21):
    for c, val in enumerate(row, 1):
        cell = ws.cell(row=r, column=c, value=val)
        cell.font = body_font
        cell.border = thin
        if c == 2:
            cell.alignment = center

ws["A31"] = "HOW TO USE THIS WORKBOOK"
ws["A31"].font = section_font
ws["A32"] = (
    "1. Review 02_Function_Catalog for the full inventory of native capabilities and their proposed MCP analog names.\n"
    "2. Use 03_MCP_Tool_Specs as the authoritative signature list when implementing a Server with @modelcontextprotocol/sdk.\n"
    "3. Consult 04_Domain_Crosswalk to bind the 16 Bridge domains to MCP tiers and operations.\n"
    "4. 05_Lifecycle_Analogs maps Holling adaptive-cycle phases onto system operations (build → harden → release → reorganize).\n"
    "5. 06_Implementation_Notes contains import paths, return shapes, and Guardian Gate binding guidance.\n"
    "6. All proposed tools remain under Evidence Clamp; never claim live production until TOFAR receipts and trust-floor checks pass."
)
ws["A32"].alignment = left_align
ws.merge_cells("A32:F32")
ws.row_dimensions[32].height = 100

auto_width(ws)
ws.column_dimensions["B"].width = 48
ws.column_dimensions["D"].width = 42
ws.column_dimensions["E"].width = 32

# ═══════════════════════════════════════════════════════════
# SHEET 2: Function Catalog
# ═══════════════════════════════════════════════════════════
ws2 = wb.create_sheet("02_Function_Catalog")

ws2["A1"] = "Native Function → MCP Analog Catalog"
ws2["A1"].font = title_font
ws2.merge_cells("A1:H1")

cat_headers = [
    "Source", "Native Function / Class", "Description", "Proposed MCP Tool",
    "Input Schema (summary)", "Output / Side-effect", "Guardian Gate", "Priority"
]
for i, h in enumerate(cat_headers, 1):
    ws2.cell(row=3, column=i, value=h)
style_header(ws2, 3, 8, blue_fill)

# Comprehensive function list
functions = [
    # Fullerene
    ("S01", "C60.MonolayerNetwork", "Icosahedral substrate with tunable band gap & coherence config", "fullerene_configure_substrate", "phase, temperature_K, buffer_gas", "substrate mesh + coherence_ms", "topological", "P1"),
    ("S01", "QuantumBridge.map_ising_frustration", "Map fullerene lattice Ising model to quantum annealer", "quantum_map_ising", "lattice, qubits, backend", "encoded Hamiltonian / qubit map", "topological", "P1"),
    ("S01", "QuantumBridge.tune_chern_number", "Tune Chern sector via strain for edge-state channels", "quantum_tune_chern", "target_chern, strain_pct", "chern_sector id + protection status", "topological", "P1"),
    ("S01", "C120Network (implied)", "Extended fullerene network for multi-scale mesh", "fullerene_extend_network", "base_mesh, scale_factor", "extended vertex/edge set", "topological", "P2"),
    # MOTIIV
    ("S02", "MotiivSynthesisSystem.process", "Ingest text/topic/role → full pipeline with Guardian stamp", "motiiv_process_event", "text, topic, role, identity", "MobiusEvent + ledger entry", "Seven Gates", "P0"),
    ("S02", "Guardian Stamp / ROUTE|BRAKE|FORBID", "Ethics gate decision on every event", "guardian_evaluate", "event, trust_floor=0.743", "decision + reason + narrowed scope", "Seven Gates", "P0"),
    ("S02", "system.get_status", "Return coherence, trust, lane health", "motiiv_get_status", "none / scope", "status object (coherence, floors)", "none", "P0"),
    ("S02", "system.export_ledger", "Append-only TOFAR-style ledger export", "motiiv_export_ledger", "path, since_ts?", "jsonl path or content", "provenance", "P1"),
    ("S02", "Tee+latch+unify auto-ingest", "No-loop sub-stream unification with provenance", "motiiv_ingest_stream", "stream_id, payload, latch", "unified event + receipt", "provenance", "P1"),
    ("S02", "Organic Hybrid Harmony Multicast", "Pub/Sub event bus", "motiiv_bus_publish / subscribe", "topic, event", "ack / callback", "none", "P2"),
    # MCP + Neo4j reference
    ("S03", "resolve_coordinate", "Resolve Kabbalistic / geometric coordinate in hypermetagraph", "resolve_coordinate", "coord_string | vector", "node set + confidence", "none", "P0"),
    ("S03", "find_intersections", "Find intersecting lineages or domains", "find_intersections", "set_a, set_b, depth", "intersection nodes + paths", "none", "P1"),
    ("S03", "traverse_lineage", "Walk ancestry / provenance graph", "traverse_lineage", "start_id, direction, max_hops", "path list + receipts", "provenance", "P1"),
    ("S03", "semantic_search", "Vector + graph hybrid search over Neo4j", "semantic_search", "query, topK, index_name", "ranked nodes + scores", "none", "P0"),
    # Coherence Bridge
    ("S04", "FractalCrystalCore.runCycle", "One fractal → crystalline constrain → learn cycle", "crystal_run_cycle", "core_id, observation", "validatedActions + confidence + novelty", "α-weight", "P0"),
    ("S04", "triadicFuse", "Fuse two cores + emergent third", "triadic_fuse", "coreA_id, coreB_id, inputA, inputB", "agreement, tension β, emergent", "α-weight", "P0"),
    ("S04", "setDesire / domain health", "Adjust domain desire field (1-5) and health", "domain_set_desire", "domain_id, desire_1to5", "updated α·w + health bar", "none", "P1"),
    ("S04", "forwardPacket (Dr.SHIFT)", "Emit coordinate packet to SHEFA/SHEMA lanes", "bridge_forward_packet", "mode, vertex, domains snapshot", "packet JSON + FAST receipt", "σ-return check", "P1"),
    ("S04", "Mode switch (ℛ𝒮ℐ𝒟)", "Reflection / Refraction / Inversion / Diffraction", "bridge_set_mode", "mode_symbol", "active mode + color + desc", "none", "P2"),
    ("S04", "σ-return trigger", "Coherence drop below threshold → return protocol", "bridge_sigma_return", "force? ", "σ status + corrective actions", "coherence floor", "P1"),
    # Adaptive cycle
    ("S05", "Adaptive cycle phase detect", "Classify current system state into growth/conservation/release/reorg", "lifecycle_detect_phase", "metrics snapshot", "phase + recommended action", "none", "P1"),
    ("S05", "Inject controlled disturbance", "Chaos-engineering / pulse harvest analog", "lifecycle_inject_disturbance", "target, intensity, bound", "release event + recovery plan", "Guardian", "P2"),
    ("S05", "Keystone monitor", "Watch critical nodes for cascade risk", "lifecycle_keystone_status", "node_id or auto", "centrality + redundancy score", "none", "P1"),
    ("S05", "Slow-variable monitor", "Track hidden stock variables (drift, O₂ analog)", "lifecycle_monitor_slow", "variable_id, window", "trend + alert if threshold", "none", "P1"),
    # Domain infra
    ("S06", "site-registry.json read", "Central domain metadata + affiliate IDs", "infra_list_domains", "none / filter", "domain list + hosting targets", "none", "P1"),
    ("S06", "deploy path-filtered workflow", "Trigger rebuild for changed site or shared/", "infra_trigger_deploy", "site_id or 'all'", "workflow run id + status", "none", "P2"),
    ("S06", "sync-shared components", "Propagate shared nav/footer/styles", "infra_sync_shared", "component_set", "diff summary + commit hash", "none", "P2"),
    # Skills
    ("S07", "skill-creator mint", "Create new skill with progressive disclosure", "skill_mint", "name, description, body, resources", "SKILL.md path + hash", "vocabulary gate", "P1"),
    ("S07", "mcp-builder QA pairs", "Generate 10 idempotent QA pairs for MCP server", "mcp_generate_qa", "server_spec, count=10", "XML QA set", "none", "P2"),
    ("S07", "mobius-vocabulary GOVERNs", "Authenticate / clamp vocabulary against 42-domain lattice", "vocab_authenticate", "term or phrase", "accepted / rewritten + lattice face", "vocabulary", "P0"),
    ("S07", "algorithmic-art RENDER", "Visualize under brand clamp (DoinBetter tokens override)", "art_render", "prompt, palette_override?", "SVG/PNG path + brand receipt", "brand gate", "P2"),
    # Library snippets
    ("S08", "B0X_bundle facets bootloader", "Pack CubeEngine + n8n MCP + Wheel HUD", "snippet_boot_b0x", "manifest path", "running ports + health", "none", "P2"),
    ("S08", "SCUBAStream runtime", "Flask + ethics clamp + ledger kernel", "snippet_scuba_start", "port, clamp_level", "server handle + ledger path", "ethics", "P2"),
    ("S08", "everybuddy-code-atlas harvest", "Classify + secret-scan + manifest code", "snippet_harvest_atlas", "root_path, classify_rules", "harvest_manifest.csv + sample.json", "secrets", "P2"),
    # Geometry
    ("S09", "Kähler / Hopf spiral index", "Index content onto Hopf fibers for permanent retrieval", "kahler_index_document", "doc_id, content, level_ℓ", "fiber coords (θ,φ,ψ) + receipt", "none", "P1"),
    ("S09", "spiral retrieval", "Retrieve by spiral phase or Hopf linking", "kahler_retrieve", "query_coords or text", "ranked docs + linking numbers", "none", "P1"),
]

for r, row in enumerate(functions, 4):
    for c, val in enumerate(row, 1):
        cell = ws2.cell(row=r, column=c, value=val)
        cell.font = body_font if c != 4 else Font(name="Consolas", size=9, bold=True)
        cell.alignment = left_align
        cell.border = thin
        if row[7] == "P0":
            cell.fill = PatternFill("solid", fgColor="D5F5E3")
        elif row[7] == "P1":
            cell.fill = light_blue
        else:
            cell.fill = light_gray

ws2["A42"] = "Priority legend: P0 = core runtime / ethics; P1 = primary operational; P2 = supporting / optional"
ws2["A42"].font = Font(name="Arial", size=9, italic=True)

auto_width(ws2)
ws2.column_dimensions["C"].width = 55
ws2.column_dimensions["D"].width = 28
ws2.column_dimensions["E"].width = 32
ws2.column_dimensions["F"].width = 36

# ═══════════════════════════════════════════════════════════
# SHEET 3: MCP Tool Specs
# ═══════════════════════════════════════════════════════════
ws3 = wb.create_sheet("03_MCP_Tool_Specs")

ws3["A1"] = "MCP Tool Signatures (for @modelcontextprotocol/sdk Server)"
ws3["A1"].font = title_font
ws3.merge_cells("A1:G1")

ws3["A2"] = "Return shape must be { content: [{ type: 'text', text: '...' }] } or structuredContent. Import paths require .js under Node16/NodeNext."
ws3["A2"].font = Font(name="Arial", size=9, italic=True)
ws3.merge_cells("A2:G2")

spec_headers = ["Tool Name", "Description", "Parameters (JSON Schema style)", "Required", "Returns", "Tier", "Example Call"]
for i, h in enumerate(spec_headers, 1):
    ws3.cell(row=4, column=i, value=h)
style_header(ws3, 4, 7, purple_fill)

tools = [
    ("motiiv_process_event", "Run full Motiiv synthesis pipeline with Guardian",
     '{"text":"string","topic":"string","role":"MEMBER|...","identity":"string"}', "text,topic,role,identity",
     "MobiusEvent JSON + decision", "CORE", 'process({text:"Hello Buddy",topic:"user.input",role:"MEMBER",identity:"User"})'),
    ("guardian_evaluate", "Apply Seven Gates ethics check",
     '{"event":"object","trust_floor":0.743}', "event",
     "ROUTE|BRAKE|FORBID + reason", "CORE", 'guardian_evaluate({event, trust_floor:0.743})'),
    ("motiiv_get_status", "System coherence & floor status",
     "{}", "", "status object", "CORE", "motiiv_get_status()"),
    ("motiiv_export_ledger", "Export append-only ledger",
     '{"path":"string","since_ts":"ISO?"}', "path",
     "file path or content", "CORE", 'export_ledger({path:"./ledger.jsonl"})'),
    ("crystal_run_cycle", "Single FractalCrystalCore cycle",
     '{"core_id":"string","observation":"object"}', "core_id",
     "validatedActions + confidence + novelty", "BRIDGE", 'crystal_run_cycle({core_id:"FormRecognizer",observation:{...}})'),
    ("triadic_fuse", "Fuse two cores into emergent",
     '{"coreA":"string","coreB":"string","inputA":{},"inputB":{}}', "coreA,coreB",
     "agreement, tension β, emergent", "BRIDGE", "triadic_fuse({...})"),
    ("domain_set_desire", "Set domain desire 1-5 and recompute α·w",
     '{"domain_id":"HYDRO|MET|...","desire":1-5}', "domain_id,desire",
     "updated domain vector", "BRIDGE", 'domain_set_desire({domain_id:"CODE",desire:5})'),
    ("bridge_forward_packet", "Emit Dr.SHIFT coordinate packet",
     '{"mode":"ℛ|𝒮|ℐ|𝒟","include_domains":true}', "mode",
     "packet JSON + FAST tag", "BRIDGE", "bridge_forward_packet({mode:'ℛ'})"),
    ("resolve_coordinate", "Resolve geometric / Kabbalistic coordinate",
     '{"coord":"string|array","space":"hopf|kahler?"}', "coord",
     "node set + confidence", "GRAPH", "resolve_coordinate({coord:'θ=0.3,φ=1.2,ψ=2.1'})"),
    ("semantic_search", "Hybrid vector + graph search",
     '{"query":"string","topK":10,"index":"string"}', "query",
     "ranked results + scores", "GRAPH", 'semantic_search({query:"fullerene Chern",topK:5})'),
    ("traverse_lineage", "Walk provenance / ancestry",
     '{"start_id":"string","direction":"in|out|both","max_hops":5}', "start_id",
     "paths + receipts", "GRAPH", "traverse_lineage({start_id:'evt-123',direction:'out'})"),
    ("fullerene_configure_substrate", "Configure C60 monolayer substrate",
     '{"phase":"qHP","temperature_K":150,"target_ms":0.25}', "phase",
     "mesh + coherence config", "QUANTUM", "fullerene_configure_substrate({phase:'qHP',temperature_K:150})"),
    ("quantum_tune_chern", "Tune Chern number sector",
     '{"target":2,"strain_pct":1.5}', "target",
     "chern_sector binding", "QUANTUM", "quantum_tune_chern({target:2,strain_pct:1.5})"),
    ("quantum_map_ising", "Map lattice to annealer Ising",
     '{"lattice":"C60.icosahedral","qubits":6,"backend":"dwave_advantage"}', "lattice",
     "encoded problem", "QUANTUM", "quantum_map_ising({lattice:'C60.icosahedral',qubits:6})"),
    ("lifecycle_detect_phase", "Detect adaptive-cycle phase",
     '{"metrics":"object"}', "metrics",
     "phase + action recommendation", "LIFECYCLE", "lifecycle_detect_phase({metrics:{...}})"),
    ("lifecycle_inject_disturbance", "Bounded chaos / pulse",
     '{"target":"string","intensity":0-1,"bound":true}', "target",
     "release event + plan", "LIFECYCLE", "lifecycle_inject_disturbance({target:'model-X',intensity:0.3})"),
    ("vocab_authenticate", "Clamp term to 42-domain lattice",
     '{"term":"string","context":"string?"}', "term",
     "accepted|rewritten + face id", "VOCAB", 'vocab_authenticate({term:"coherence flux"})'),
    ("skill_mint", "Mint new skill under progressive disclosure",
     '{"name":"string","description":"string","body":"string","resources":[]}', "name,description,body",
     "SKILL.md path + TOFAR hash", "SKILL", "skill_mint({name:'new-skill',...})"),
    ("kahler_index_document", "Index onto Hopf spiral fiber",
     '{"doc_id":"string","content":"string","level":0}', "doc_id,content",
     "fiber coords + receipt", "GEOMETRY", "kahler_index_document({doc_id:'d1',content:'...'})"),
    ("infra_list_domains", "List registered domains from site-registry",
     '{"filter":"string?"}', "",
     "domain metadata array", "INFRA", "infra_list_domains()"),
]

for r, row in enumerate(tools, 5):
    for c, val in enumerate(row, 1):
        cell = ws3.cell(row=r, column=c, value=val)
        cell.font = mono_font if c in (1, 3, 7) else body_font
        cell.alignment = left_align
        cell.border = thin
        if row[5] == "CORE":
            cell.fill = light_teal
        elif row[5] == "BRIDGE":
            cell.fill = light_purple
        elif row[5] == "QUANTUM":
            cell.fill = light_amber
        else:
            cell.fill = light_gray

auto_width(ws3)
ws3.column_dimensions["B"].width = 42
ws3.column_dimensions["C"].width = 55
ws3.column_dimensions["G"].width = 50

# ═══════════════════════════════════════════════════════════
# SHEET 4: Domain Crosswalk
# ═══════════════════════════════════════════════════════════
ws4 = wb.create_sheet("04_Domain_Crosswalk")

ws4["A1"] = "16 Bridge Domains × MCP Binding × Analog Operations"
ws4["A1"].font = title_font
ws4.merge_cells("A1:G1")

dom_headers = ["Domain ID", "Color", "Primary MCP (Bridge)", "Tier", "Analog Operations (from Catalog)", "Desire α·w formula", "Health Note"]
for i, h in enumerate(dom_headers, 1):
    ws4.cell(row=3, column=i, value=h)
style_header(ws4, 3, 7, teal_fill)

domains = [
    ("HYDRO", "#00d4ff", "web_search", "CORE", "semantic_search, kahler_retrieve", "desire/5 * 0.743", "Water / flow signals"),
    ("MET", "#44ddcc", "web_fetch", "CORE", "motiiv_process_event, traverse_lineage", "desire/5 * 0.743", "Metabolic / data fetch"),
    ("GEO", "#44cc88", "drive_search", "CORE", "infra_list_domains, resolve_coordinate", "desire/5 * 0.743", "Place / storage"),
    ("SPACE", "#9988ff", "pubmed", "MCP", "quantum_tune_chern, fullerene_configure", "desire/5 * 0.743", "Research / quantum"),
    ("VISION", "#ffaa00", "image_search / visualize", "CORE", "art_render, bridge modes", "desire/5 * 0.743", "Visual / render"),
    ("AUDIO", "#ff44cc", "play_sheet", "MCP", "motiiv bus, harmony multicast", "desire/5 * 0.743", "Sonic / sheet"),
    ("TEXT", "#00ff88", "artifacts", "CORE", "skill_mint, vocab_authenticate", "desire/5 * 0.743", "Text / artifacts"),
    ("TELEM", "#ff6699", "conv_search", "CORE", "semantic_search, lifecycle_monitor_slow", "desire/5 * 0.743", "Telemetry / conv"),
    ("ETHICS", "#bb88ff", "memory", "CORE", "guardian_evaluate, vocab_authenticate", "desire/5 * 0.743", "Guardian / memory"),
    ("INFRA", "#ffcc44", "godaddy", "MCP", "infra_list_domains, infra_trigger_deploy", "desire/5 * 0.743", "Domains / DNS"),
    ("CODE", "#ff8844", "github", "MCP", "snippet_harvest_atlas, skill_mint", "desire/5 * 0.743", "Repos / CI"),
    ("COMMS", "#ff6699", "slack", "MCP", "motiiv_bus_publish, forward_packet", "desire/5 * 0.743", "Messaging"),
    ("TRACK", "#bb88ff", "linear", "MCP", "lifecycle_detect_phase, keystone_status", "desire/5 * 0.743", "Issues / track"),
    ("HARVEST", "#00d4ff", "drive_fetch", "CORE", "snippet_harvest_atlas, export_ledger", "desire/5 * 0.743", "Ingest / harvest"),
    ("EMIT", "#ffaa00", "visualize", "CORE", "art_render, bridge_forward_packet", "desire/5 * 0.743", "Emit / viz"),
    ("PROP", "#00ff88", "drive_search", "CORE", "kahler_index_document, traverse_lineage", "desire/5 * 0.743", "Propagate / prop"),
]

for r, row in enumerate(domains, 4):
    for c, val in enumerate(row, 1):
        cell = ws4.cell(row=r, column=c, value=val)
        cell.font = body_font
        cell.alignment = left_align
        cell.border = thin
        if c == 2:
            cell.fill = PatternFill("solid", fgColor=val.replace("#", ""))
            cell.font = Font(name="Arial", size=9, color="FFFFFF")

ws4["A22"] = "Modes (ℛ Reflection, 𝒮 Refraction, ℐ Fractal Inversion, 𝒟 Diffraction) modulate how domain signals are processed in triadic_fuse and forward_packet."
ws4["A22"].font = Font(name="Arial", size=9, italic=True)
ws4.merge_cells("A22:G22")

auto_width(ws4)
ws4.column_dimensions["E"].width = 45

# ═══════════════════════════════════════════════════════════
# SHEET 5: Lifecycle Analogs
# ═══════════════════════════════════════════════════════════
ws5 = wb.create_sheet("05_Lifecycle_Analogs")

ws5["A1"] = "Holling Adaptive Cycle ↔ Möbii³us / MCP Operations"
ws5["A1"].font = title_font
ws5.merge_cells("A1:F1")

ws5["A2"] = "Panarchy nesting: fast biogeochemical clock → mid 'season' clock → slow successional clock. Engineering acts on fast/mid to steer slow."
ws5["A2"].font = Font(name="Arial", size=9, italic=True)
ws5.merge_cells("A2:F2")

life_headers = ["Phase", "Ecological Meaning", "Software / AI Analog", "Möbii³us Mapping", "Suggested MCP Tools", "Anti-pattern"]
for i, h in enumerate(life_headers, 1):
    ws5.cell(row=4, column=i, value=h)
style_header(ws5, 4, 6, amber_fill)

phases = [
    ("Growth (r)", "Exploitation, rapid colonization, high novelty", "Feature build-up, model training, data ingestion", "CrystalCore learn cycles, skill_mint, harvest_atlas", "crystal_run_cycle, skill_mint, motiiv_ingest_stream, snippet_harvest_atlas", "Unbounded growth without Guardian"),
    ("Conservation (K)", "Accumulation, rigidity, high connectedness", "Hardening, optimization, production freeze, high coherence", "Guardian floors, Chern protection, brand clamp, ledger sealing", "guardian_evaluate, quantum_tune_chern, motiiv_export_ledger, vocab_authenticate", "Climax ossification / no disturbance"),
    ("Release (Ω)", "Creative destruction, collapse of structure", "Chaos engineering, decommission, catastrophic forgetting recovery", "σ-return, inject_disturbance, FORBID → reorg path", "bridge_sigma_return, lifecycle_inject_disturbance, guardian_evaluate (FORBID)", "Uncontrolled cascade / keystone loss"),
    ("Reorganization (α)", "Renewal, innovation, pioneer states", "Refactor, retrain, new skill composition, domain re-wiring", "triadic_fuse emergent, new domain desire, monorepo restructure", "triadic_fuse, domain_set_desire, infra_sync_shared, skill_mint", "Premature lock-in before diversity restored"),
]

for r, row in enumerate(phases, 5):
    for c, val in enumerate(row, 1):
        cell = ws5.cell(row=r, column=c, value=val)
        cell.font = body_font
        cell.alignment = left_align
        cell.border = thin
        cell.fill = light_amber if r % 2 else PatternFill("solid", fgColor="FEF9E7")

ws5["A10"] = "Key engineering lessons transferred"
ws5["A10"].font = section_font
ws5["A11"] = (
    "• Closed systems fail at the slow, hidden variable (Biosphere 2 O₂) → lifecycle_monitor_slow + drift detection.\n"
    "• Resilience = diversity + redundancy + multifunctionality; avoid single critical nodes → keystone_status + eco-connectance analogs.\n"
    "• Stagnation at climax is prevented by deliberate bounded disturbance → inject_disturbance under Guardian.\n"
    "• Keystones and trophic cascades are coherence anchors → Guardian + ETHICS domain + α floor."
)
ws5["A11"].alignment = left_align
ws5.merge_cells("A11:F11")
ws5.row_dimensions[11].height = 70

auto_width(ws5)
ws5.column_dimensions["B"].width = 40
ws5.column_dimensions["C"].width = 42
ws5.column_dimensions["D"].width = 45
ws5.column_dimensions["E"].width = 50

# ═══════════════════════════════════════════════════════════
# SHEET 6: Implementation Notes
# ═══════════════════════════════════════════════════════════
ws6 = wb.create_sheet("06_Implementation_Notes")

ws6["A1"] = "Implementation Notes for MCP Server (TypeScript + optional Neo4j)"
ws6["A1"].font = title_font
ws6.merge_cells("A1:B1")

ws6["A3"] = "SDK & Runtime"
ws6["A3"].font = section_font
ws6["A4"] = "Package"
ws6["B4"] = "@modelcontextprotocol/sdk ^1.29.0 (v1.x production; v2 alpha Q1 2026)"
ws6["A5"] = "Server class"
ws6["B5"] = "Prefer low-level Server from server/index.js for fixed tool set; setRequestHandler(ListToolsRequestSchema / CallToolRequestSchema)"
ws6["A6"] = "Transport"
ws6["B6"] = "StdioServerTransport for Claude Desktop / local; keep absolute paths in config"
ws6["A7"] = "Import paths"
ws6["B7"] = "ESM + Node16/NodeNext REQUIRED; every subpath needs .js extension"
ws6["A8"] = "Tool return shape"
ws6["B8"] = "{ content: [{ type: 'text', text: '...' }] }  — old toolResult field removed"
ws6["A9"] = "Zod peer"
ws6["B9"] = "SDK imports zod/v4 internally; pin compatible zod ≥3.25; older SDK+Zod v4 breaks"

ws6["A11"] = "Neo4j (when used)"
ws6["A11"].font = section_font
ws6["A12"] = "Driver"
ws6["B12"] = "neo4j-driver v5; executeRead / executeWrite for auto-retry"
ws6["A13"] = "URI schemes"
ws6["B13"] = "neo4j+s:// (routing+TLS Aura) or bolt+s:// (direct+TLS)"
ws6["A14"] = "Vector index"
ws6["B14"] = "CREATE VECTOR INDEX ... OPTIONS {indexConfig: {vector.dimensions: N, vector.similarity_function: 'cosine'}} (GA since 5.13)"
ws6["A15"] = "Query"
ws6["B15"] = "db.index.vector.queryNodes for k-ANN"

ws6["A17"] = "Guardian / Evidence Clamp Binding"
ws6["A17"].font = section_font
ws6["A18"] = "Trust floor"
ws6["B18"] = "α = 0.743 — every guardian_evaluate and σ-return check must reference this constant"
ws6["A19"] = "Decision outcomes"
ws6["B19"] = "ROUTE (proceed) | BRAKE (pause + narrow + HOME) | FORBID (block)"
ws6["A20"] = "TOFAR / ledger"
ws6["B20"] = "Append-only; model as :TofarEntry nodes or jsonl; never mutate history"
ws6["A21"] = "σ-return"
ws6["B21"] = "If emergent coherence < ~0.3 trigger return protocol; expose as tool or resource"

ws6["A23"] = "Suggested Server Skeleton (pseudocode)"
ws6["A23"].font = section_font
ws6["A24"] = (
    "import { Server } from '@modelcontextprotocol/sdk/server/index.js';\n"
    "import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';\n"
    "// register ListTools + CallTool handlers\n"
    "// switch(name) { case 'motiiv_process_event': ... case 'guardian_evaluate': ... }\n"
    "// always return { content: [...] }\n"
    "// bind Guardian before any state-changing tool"
)
ws6["A24"].font = mono_font
ws6["A24"].alignment = left_align
ws6.merge_cells("A24:B24")
ws6.row_dimensions[24].height = 90

ws6["A26"] = "Evidence Clamp Notice"
ws6["A26"].font = Font(name="Arial", bold=True, size=11, color="C0392B")
ws6["A27"] = (
    "This workbook is a design-time synthesis under the Möbii³us Evidence Clamp. "
    "No tool is live until TOFAR receipts, trust-floor checks, and explicit deployment lock (see MOTIIV status: LOCKED) are satisfied. "
    "Treat all proposed MCP names as draft analogs, not production endpoints."
)
ws6["A27"].font = Font(name="Arial", size=10, italic=True)
ws6["A27"].alignment = left_align
ws6.merge_cells("A27:B27")
ws6.row_dimensions[27].height = 50

for row in range(4, 22):
    ws6.cell(row=row, column=1).font = Font(name="Arial", bold=True, size=10)
    ws6.cell(row=row, column=1).fill = light_gray
    ws6.cell(row=row, column=2).font = body_font
    ws6.cell(row=row, column=1).border = thin
    ws6.cell(row=row, column=2).border = thin

ws6.column_dimensions["A"].width = 28
ws6.column_dimensions["B"].width = 95

# ═══════════════════════════════════════════════════════════
# SHEET 7: Quick Reference Matrix
# ═══════════════════════════════════════════════════════════
ws7 = wb.create_sheet("07_Quick_Matrix")

ws7["A1"] = "Quick Cross-System Analog Matrix (selected)"
ws7["A1"].font = title_font
ws7.merge_cells("A1:F1")

mx_headers = ["Capability", "Fullerene / Quantum", "MOTIIV Event Kernel", "Coherence Bridge", "MCP Graph", "Lifecycle"]
for i, h in enumerate(mx_headers, 1):
    ws7.cell(row=3, column=i, value=h)
style_header(ws7, 3, 6, blue_fill)

matrix = [
    ("Ingest / Process", "configure_substrate", "process + Tee+latch+unify", "crystal_run_cycle", "semantic_search", "Growth phase detect"),
    ("Ethics / Gate", "Chern sector bind", "Guardian ROUTE/BRAKE/FORBID", "σ-return + α floor", "—", "Keystone + disturbance bound"),
    ("Coordinate / Locate", "icosahedral mesh", "MobiusEvent atom", "vertex_bin + Hopf-like", "resolve_coordinate", "Phase coordinate"),
    ("Fuse / Synthesize", "Ising map + HMO compact", "Organic Hybrid Multicast", "triadic_fuse", "find_intersections", "Reorganization"),
    ("Persist / Provenance", "coherence config", "export_ledger / TOFAR", "FART / FAST trail", "traverse_lineage", "Slow-variable log"),
    ("Visualize / Emit", "—", "status", "forward_packet + modes", "—", "Disturbance inject viz"),
    ("Skill / Extend", "—", "—", "domain desire", "—", "skill_mint + vocab"),
]

for r, row in enumerate(matrix, 4):
    for c, val in enumerate(row, 1):
        cell = ws7.cell(row=r, column=c, value=val)
        cell.font = body_font
        cell.alignment = left_align
        cell.border = thin
        if c == 1:
            cell.font = Font(name="Arial", bold=True, size=10)
            cell.fill = light_blue

auto_width(ws7)

# Footer on overview
ws["A34"] = "Möbii³us · DoinBetter · Evidence Clamp ACTIVE · Local / Draft Workbook · α=0.743"
ws["A34"].font = Font(name="Arial", size=8, color="888888")

# Save
out_path = "/home/workdir/artifacts/Möbii³us_MCP_Workbook_Analogs.xlsx"
wb.save(out_path)
print(f"Saved: {out_path}")
print(f"Sheets: {wb.sheetnames}")
print(f"Function catalog rows: {len(functions)}")
print(f"MCP tool specs: {len(tools)}")
