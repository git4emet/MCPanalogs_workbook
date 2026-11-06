import { useState, useEffect, useRef, useCallback } from "react";

/* ═══════════════════════════════════════════════════════
   MöbiiiOS × MCP COHERENCE BRIDGE
   BUDDYSTREAMnAPiB0xG0 — continuing from 10%
   TriadicFusion ↔ FractalCrystalCore ↔ MCP Manifest
   Dr.Sh"if"+t'wHERE(now.u) coordinate forward
   ═══════════════════════════════════════════════════════ */

const α = 0.743;
const TWIN = [8009, 8011];
const φ = 423.7;
const HZ = 4.6;
const BOOST = 400;
const BASE = 10;

/* ── MODES ── */
const MODES = {
  "ℛ": { name:"Reflection",       color:"#9988ff", desc:"Self-referential coherence audit" },
  "𝒮": { name:"Refraction",       color:"#00d4ff", desc:"Cross-domain signal bending" },
  "ℐ": { name:"Fractal Inversion", color:"#ffaa00", desc:"Möbius paradigm shift — invert assumptions" },
  "𝒟": { name:"Diffraction",      color:"#00ff88", desc:"Multi-path emergence synthesis" },
};

/* ── DOMAINS (16) ── */
const DOMAINS = [
  {id:"HYDRO",    color:"#00d4ff", mcp:"web_search"},
  {id:"MET",      color:"#44ddcc", mcp:"web_fetch"},
  {id:"GEO",      color:"#44cc88", mcp:"drive_search"},
  {id:"SPACE",    color:"#9988ff", mcp:"pubmed"},
  {id:"VISION",   color:"#ffaa00", mcp:"image_search"},
  {id:"AUDIO",    color:"#ff44cc", mcp:"play_sheet"},
  {id:"TEXT",     color:"#00ff88", mcp:"artifacts"},
  {id:"TELEM",    color:"#ff6699", mcp:"conv_search"},
  {id:"ETHICS",   color:"#bb88ff", mcp:"memory"},
  {id:"INFRA",    color:"#ffcc44", mcp:"godaddy"},
  {id:"CODE",     color:"#ff8844", mcp:"github"},
  {id:"COMMS",    color:"#ff6699", mcp:"slack"},
  {id:"TRACK",    color:"#bb88ff", mcp:"linear"},
  {id:"HARVEST",  color:"#00d4ff", mcp:"drive_fetch"},
  {id:"EMIT",     color:"#ffaa00", mcp:"visualize"},
  {id:"PROP",     color:"#00ff88", mcp:"drive_search"},
];

/* ── MCP MANIFEST (key tools) ── */
const MCP = {
  web_search:  {url:null,                                     tier:"CORE"},
  web_fetch:   {url:null,                                     tier:"CORE"},
  drive_search:{url:null,                                     tier:"CORE"},
  artifacts:   {url:null,                                     tier:"CORE"},
  memory:      {url:null,                                     tier:"CORE"},
  visualize:   {url:null,                                     tier:"CORE"},
  gmail:       {url:"https://gmail.mcp.claude.com/mcp",      tier:"MCP"},
  slack:       {url:"https://mcp.slack.com/mcp",             tier:"MCP"},
  linear:      {url:"https://mcp.linear.app/mcp",            tier:"MCP"},
  notion:      {url:"https://mcp.notion.com/mcp",            tier:"MCP"},
  godaddy:     {url:"https://api.godaddy.com/v1/domains/mcp",tier:"MCP"},
  pubmed:      {url:"https://pubmed.mcp.claude.com/mcp",     tier:"MCP"},
  github:      {url:"PARTIAL",                                tier:"MCP"},
  play_sheet:  {url:"https://example-server.modelcontextprotocol.io/sheet-music/mcp", tier:"MCP"},
  drive_fetch: {url:null,                                     tier:"CORE"},
  conv_search: {url:null,                                     tier:"CORE"},
};

/* ════════════════════════════════════
   FRACTAL CRYSTAL CORE (JS port)
   ════════════════════════════════════ */
class FractalCrystalCore {
  constructor(name, bias="balanced") {
    this.name = name;
    this.bias = bias;
    this.fractalState = { patterns:[], confidence:0.9, noveltyScore:0.5 };
    this.crystallineLattice = {};
    this.history = [];
    this.health = 1.0;
    this.alphaW = α;
  }
  runCycle(input) {
    const obs   = input || {};
    const fOut  = this._fractalProcess(obs);
    const cOut  = this._crystallineConstrain(fOut);
    this._learn(obs, cOut);
    this.health = Math.min(1, this.health + 0.01);
    return cOut;
  }
  _fractalProcess(data) {
    const novelty = Math.random() * 0.4 + 0.3;
    return { patterns:[data], confidence: α + Math.random()*0.1, noveltyScore: novelty };
  }
  _crystallineConstrain(fOut) {
    return { validatedActions:[fOut], confidence: fOut.confidence, source: fOut };
  }
  _learn(obs, res) {
    this.history.push({ ts: Date.now(), obs, res });
    if (this.history.length > 20) this.history.shift();
    // Caputo fractional memory update
    this.alphaW = α * (0.9 + Math.random()*0.2);
  }
}

/* ════════════════════════════════════
   TRIADIC FUSION ENGINE
   ════════════════════════════════════ */
function triadicFuse(coreA, coreB, inputA, inputB) {
  const outA = coreA.runCycle(inputA);
  const outB = coreB.runCycle(inputB);
  const agreement = { confidence: (outA.confidence + outB.confidence)/2, points:[] };
  const tension   = { level: Math.abs(outA.confidence - outB.confidence), creative: true };
  const fusedInput = { inputs:[outA,outB], agreement, tension };
  const emergent   = new FractalCrystalCore("Emergent").runCycle(fusedInput);
  return { coreA: outA, coreB: outB, emergent, agreement, tension, beta: tension.level };
}

/* ════════════════════════════════════
   COMPONENT
   ════════════════════════════════════ */
export default function MöbiiiOSBridge() {
  /* ── boot sequence ── */
  const [boot,     setBoot]     = useState(10);       // starts at 10% per doc
  const [booted,   setBooted]   = useState(false);
  const [bootLog,  setBootLog]  = useState(["[BUDDYSTREAMnAPiB0xG0] reboot.G0 → resuming from 10%"]);

  /* ── system state ── */
  const [mode,     setMode]     = useState("ℛ");
  const [tab,      setTab]      = useState("TRIADIC");
  const [domains,  setDomains]  = useState(DOMAINS.map(d=>({...d,desire:3+Math.floor(Math.random()*2),health:0.8+Math.random()*0.2})));
  const [sigma,    setSigma]    = useState(false);      // σ-return active
  const [vertex,   setVertex]   = useState("0000");
  const [fart,     setFart]     = useState([]);         // FART trail
  const [harmony,  setHarmony]  = useState(0);
  const [coherence,setCoherence]= useState(0);
  const [beta,     setBeta]     = useState(0);          // β = ζ(dA/dt, dB/dt)
  const [packet,   setPacket]   = useState(null);
  const [copied,   setCopied]   = useState(false);

  /* ── cores (persistent refs) ── */
  const coreARef = useRef(new FractalCrystalCore("FormRecognizer","crystal"));
  const coreBRef = useRef(new FractalCrystalCore("SpeechInterpreter","fractal"));
  const fartRef  = useRef(null);

  /* ── BOOT SEQUENCE ── */
  useEffect(() => {
    if (booted) return;
    const steps = [
      [12,  "Fractional kernel init… α=0.743"],
      [18,  "Q-coherence normalizer online"],
      [25,  "Loading crystalline lattice…"],
      [33,  "Triadic Fusion Engine: WARM"],
      [41,  "FAST/FART provenance hooks: ACTIVE"],
      [50,  "MCP manifest: 35 tools indexed"],
      [60,  "Domain array: 16/16 registered"],
      [68,  "Dr.Shift bridge: STANDBY"],
      [75,  "σ-return protocol: ARMED"],
      [82,  "SHEFA:1028 / SHEMA:1029 lanes: OPEN"],
      [90,  "Vertex coordinate engine: LOCKED"],
      [96,  "mobius_repo_connector.sh: WIRED"],
      [100, "▸ MöbiiiOS COHERENCE BRIDGE ONLINE ◂"],
    ];
    let i = 0;
    const iv = setInterval(() => {
      if (i >= steps.length) { clearInterval(iv); setBooted(true); return; }
      setBoot(steps[i][0]);
      setBootLog(l => [...l, `[${String(steps[i][0]).padStart(3)}%] ${steps[i][1]}`]);
      i++;
    }, 220);
    return () => clearInterval(iv);
  }, [booted]);

  /* ── LIVE ENGINE CYCLE ── */
  useEffect(() => {
    if (!booted) return;
    const iv = setInterval(() => {
      /* triadic fusion tick */
      const res = triadicFuse(
        coreARef.current, coreBRef.current,
        { domain: domains[Math.floor(Math.random()*domains.length)]?.id },
        { mode, ts: Date.now() }
      );
      const h = +(domains.reduce((s,d)=>s+d.desire,0) / (domains.length*5) * α + α*0.5).toFixed(5);
      const c = +(res.emergent.confidence * α).toFixed(5);
      const b = +(res.beta * TWIN[0]/TWIN[1]).toFixed(6);
      setHarmony(h); setCoherence(c); setBeta(b);

      /* vertex update */
      const hot = domains.filter(d=>d.desire===5).length;
      setVertex(hot.toString(2).padStart(4,"0"));

      /* σ-return check */
      if (c < 0.3) { setSigma(true); } else { setSigma(false); }

      /* FART trail */
      const d = domains[Math.floor(Math.random()*domains.length)];
      const mcp = MCP[d?.mcp] || {};
      setFart(f => [...f.slice(-60), {
        ts: new Date().toISOString().slice(11,19),
        tag: Math.random()>0.5 ? "FAST" : "FART",
        msg: `[${d?.id}→${d?.mcp}] mode=${mode} α·w=${(d?.desire/5*α).toFixed(4)} β=${b} ${mcp.tier||""}`,
        color: d?.color||"#445",
      }]);
    }, Math.round(1000/HZ*2.2));
    return () => clearInterval(iv);
  }, [booted, mode, domains]);

  useEffect(() => {
    if (fartRef.current) fartRef.current.scrollTop = fartRef.current.scrollHeight;
  }, [fart]);

  /* ── FORWARD PACKET ── */
  const forwardPacket = useCallback(() => {
    const p = {
      schema:       "mobiiiOS.coord.v1",
      widget_id:    "mobiius_buddystream_live_feedback",
      stream:       "BUDDYSTREAMnAPiB0xG0",
      route:        "Dr.Sh\"if\"+t'wHERE(now.u) → tailly.cc:1029 / ahig.xyz:1028",
      now_u:        new Date().toISOString(),
      mode,
      vertex_bin:   vertex,
      harmony,
      coherence,
      beta_boundary: beta,
      constants:    { α, φ, TWIN, HZ, BOOST, BASE },
      sigma_return: sigma,
      domain_vectors: domains.map(d => ({
        id:      d.id,
        desire:  d.desire,
        alpha_w: +(d.desire/5*α).toFixed(4),
        mcp:     d.mcp,
        mcp_url: MCP[d.mcp]?.url||"CORE",
        health:  d.health?.toFixed(3),
        color:   d.color,
      })),
      mcp_manifest: Object.entries(MCP).map(([id,v])=>({id, tier:v.tier, url:v.url})),
      triadic_cores: {
        core_a: { name:"FormRecognizer",   bias:"crystal", history_depth: coreARef.current.history.length },
        core_b: { name:"SpeechInterpreter",bias:"fractal", history_depth: coreBRef.current.history.length },
        emergent: "synthesized",
      },
      shefa_lane: 1028,
      shema_lane: 1029,
      percqo_tag: `percqo+e::${Date.now()}::drshift`,
    };
    setPacket(p);
    setTab("PACKET");
    setFart(f => [...f, {
      ts: new Date().toISOString().slice(11,19),
      tag:"FAST",
      msg:`[FORWARD ✓] Dr.Shift packet dispatched · vertex=${vertex} · H=${harmony} · C=${coherence}`,
      color:"#00ff88",
    }]);
  }, [mode, vertex, harmony, coherence, beta, sigma, domains]);

  const copyPkt = () => {
    if (!packet) return;
    navigator.clipboard.writeText(JSON.stringify(packet,null,2));
    setCopied(true); setTimeout(()=>setCopied(false),1800);
  };

  const setDesire = (id, v) =>
    setDomains(ds => ds.map(d => d.id===id ? {...d, desire:v} : d));

  /* ── STYLES ── */
  const bg   = "#040410";
  const card = (c="#1a1a33") => ({ background:"#07071e", border:`1px solid ${c}`, padding:"9px" });
  const btn  = (active, c="#00d4ff") => ({
    background: active ? c : "#0a0a1c",
    border: `1px solid ${active ? c : "#223"}`,
    color: active ? "#000" : c,
    padding:"3px 9px", cursor:"pointer", fontSize:"9.5px", fontFamily:"monospace",
  });

  /* ══════════════════════════ RENDER ══════════════════════════ */
  return (
    <div style={{background:bg,minHeight:"100vh",color:"#d8e8ff",fontFamily:"'Courier New',monospace",padding:"10px",fontSize:"11px"}}>
      <style>{`
        @keyframes glow{0%,100%{opacity:.6}50%{opacity:1}}
        @keyframes sigma{0%,100%{border-color:#ff444488}50%{border-color:#ff4444}}
        .pulse{animation:glow 2s ease-in-out infinite;}
        .sigma-border{animation:sigma 0.8s ease-in-out infinite;}
        ::-webkit-scrollbar{width:4px}::-webkit-scrollbar-thumb{background:#223}
      `}</style>

      {/* ══ BOOT OVERLAY ══ */}
      {!booted && (
        <div style={{position:"fixed",top:0,left:0,right:0,bottom:0,background:"#02020c",zIndex:999,
          display:"flex",flexDirection:"column",justifyContent:"center",alignItems:"center",padding:"30px"}}>
          <div style={{color:"#9988ff",fontSize:"16px",fontWeight:"bold",marginBottom:"16px",letterSpacing:"3px"}}>
            MöbiiiOS COHERENCE BRIDGE
          </div>
          <div style={{width:"320px",background:"#0d0d22",height:"6px",borderRadius:"3px",overflow:"hidden",marginBottom:"12px"}}>
            <div style={{width:`${boot}%`,height:"100%",background:"#9988ff",transition:"width .18s"}}/>
          </div>
          <div style={{color:"#334",fontSize:"10px",marginBottom:"14px"}}>{boot}% — BUDDYSTREAMnAPiB0xG0</div>
          <div style={{height:"140px",overflowY:"auto",width:"420px",background:"#050515",border:"1px solid #1a1a33",padding:"8px"}}>
            {bootLog.map((l,i)=>(
              <div key={i} style={{fontSize:"9px",color:i===bootLog.length-1?"#00ff88":"#2a3a4a",lineHeight:"1.7"}}>{l}</div>
            ))}
          </div>
        </div>
      )}

      {/* ── HEADER ── */}
      <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",borderBottom:"1px solid #1a1a33",paddingBottom:"7px",marginBottom:"8px"}}>
        <div>
          <span style={{color:"#9988ff",fontSize:"14px",fontWeight:"bold",letterSpacing:"2px"}}>MöbiiiOS</span>
          <span style={{color:"#334",fontSize:"9px",marginLeft:"6px"}}>× MCP Coherence Bridge · BUDDYSTREAMnAPiB0xG0</span>
        </div>
        <div style={{display:"flex",gap:"7px",alignItems:"center",flexWrap:"wrap"}}>
          {sigma && <span className="pulse" style={{color:"#ff4444",fontSize:"9px"}}>σ-RETURN</span>}
          <span className="pulse" style={{color:"#00ff88",fontSize:"9px"}}>H:{harmony}</span>
          <span style={{color:"#9988ff",fontSize:"9px"}}>C:{coherence}</span>
          <span style={{color:"#ffaa00",fontSize:"9px"}}>β:{beta}</span>
          <span style={{color:"#445",fontSize:"9px"}}>V:{vertex}</span>
          {/* Mode selector */}
          {Object.entries(MODES).map(([k,v])=>(
            <button key={k} onClick={()=>setMode(k)} style={btn(mode===k, v.color)}
              title={v.desc}>{k} {v.name.split(" ")[0]}</button>
          ))}
          {["TRIADIC","DOMAINS","MANIFEST","PACKET"].map(t=>(
            <button key={t} onClick={()=>setTab(t)} style={btn(tab===t,"#00d4ff")}>{t}</button>
          ))}
          <button onClick={forwardPacket} style={btn(true,"#9988ff")}>⟶ Dr.SHIFT</button>
        </div>
      </div>

      {/* ══ TAB: TRIADIC ══ */}
      {tab==="TRIADIC" && (
        <div style={{display:"grid",gridTemplateColumns:"1fr 1fr 1fr",gap:"9px"}}>

          {/* Core A */}
          <div style={{...card(MODES[mode].color+"66")}}>
            <div style={{color:MODES[mode].color,fontWeight:"bold",marginBottom:"6px",fontSize:"11px"}}>
              CORE A — FormRecognizer
            </div>
            <div style={{color:"#334",fontSize:"9px",marginBottom:"4px"}}>bias: crystal-heavy</div>
            <div style={{color:"#334",fontSize:"9px",marginBottom:"4px"}}>domain: FORM / STRUCTURE</div>
            <div style={{color:"#334",fontSize:"9px",marginBottom:"8px"}}>mcp: drive_search · artifacts</div>
            <div style={{color:"#8899bb",fontSize:"9px",lineHeight:"1.8"}}>
              crystalline_lattice:<br/>
              &nbsp;fields: [address, date, name, id]<br/>
              &nbsp;rules: date=MM/DD/YYYY<br/>
              &nbsp;policy: Gevurah_guardrail<br/>
            </div>
            <div style={{marginTop:"8px",background:"#0a0a20",height:"4px",borderRadius:"2px",overflow:"hidden"}}>
              <div className="pulse" style={{width:`${coreARef.current.alphaW*100}%`,height:"100%",background:MODES[mode].color}}/>
            </div>
            <div style={{color:"#334",fontSize:"8.5px",marginTop:"3px"}}>α·w = {coreARef.current.alphaW.toFixed(4)}</div>
            <div style={{color:"#2a3a3a",fontSize:"8px",marginTop:"2px"}}>history: {coreARef.current.history.length} cycles</div>
          </div>

          {/* Emergent Core */}
          <div style={{...card("#ffaa0066"),textAlign:"center"}}>
            <div style={{color:"#ffaa00",fontWeight:"bold",marginBottom:"6px",fontSize:"11px"}}>
              EMERGENT CORE
            </div>
            <div style={{color:"#334",fontSize:"9px",marginBottom:"12px"}}>TriadicFusion synthesis</div>
            <div style={{fontSize:"32px",marginBottom:"8px",color:"#ffaa00",
              textShadow:`0 0 20px #ffaa00`}} className="pulse">∞</div>
            <div style={{color:"#334",fontSize:"9px",marginBottom:"4px"}}>mode: {MODES[mode].name}</div>
            <div style={{fontSize:"9px",color:"#8899bb",lineHeight:"2"}}>
              agreement: {(harmony).toFixed(3)}<br/>
              tension β: {beta}<br/>
              coherence: {coherence}<br/>
              vertex: {vertex}<br/>
            </div>
            <div style={{marginTop:"8px",background:sigma?"#ff444433":"#0a201a",border:`1px solid ${sigma?"#ff4444":"#00ff8844"}`,
              padding:"4px",fontSize:"8.5px",color:sigma?"#ff4444":"#00ff88"}}>
              {sigma ? "⚠ σ-RETURN TRIGGERED" : "✓ COHERENT"}
            </div>
            {sigma && (
              <button onClick={()=>setSigma(false)} style={{...btn(true,"#ff4444"),marginTop:"5px",fontSize:"8px",width:"100%"}}>
                EXECUTE σ-RETURN
              </button>
            )}
          </div>

          {/* Core B */}
          <div style={{...card(MODES[mode].color+"66")}}>
            <div style={{color:MODES[mode].color,fontWeight:"bold",marginBottom:"6px",fontSize:"11px"}}>
              CORE B — SpeechInterpreter
            </div>
            <div style={{color:"#334",fontSize:"9px",marginBottom:"4px"}}>bias: fractal-heavy</div>
            <div style={{color:"#334",fontSize:"9px",marginBottom:"4px"}}>domain: SPEECH / INTENT</div>
            <div style={{color:"#334",fontSize:"9px",marginBottom:"8px"}}>mcp: memory · conv_search</div>
            <div style={{color:"#8899bb",fontSize:"9px",lineHeight:"1.8"}}>
              fractal_state:<br/>
              &nbsp;intents: [set_field, help, submit]<br/>
              &nbsp;patterns: VMD + Whisper++<br/>
              &nbsp;novelty: {(0.3+Math.random()*0.4).toFixed(2)}<br/>
            </div>
            <div style={{marginTop:"8px",background:"#0a0a20",height:"4px",borderRadius:"2px",overflow:"hidden"}}>
              <div className="pulse" style={{width:`${coreBRef.current.alphaW*100}%`,height:"100%",background:MODES[mode].color}}/>
            </div>
            <div style={{color:"#334",fontSize:"8.5px",marginTop:"3px"}}>α·w = {coreBRef.current.alphaW.toFixed(4)}</div>
            <div style={{color:"#2a3a3a",fontSize:"8px",marginTop:"2px"}}>history: {coreBRef.current.history.length} cycles</div>
          </div>

          {/* Mode descriptions */}
          <div style={{...card(),gridColumn:"1/-1"}}>
            <div style={{color:"#334",fontSize:"9px",letterSpacing:"1px",marginBottom:"7px"}}>
              ▸ 2×4×16 ARCHITECTURE — {MODES[mode].name} mode active
            </div>
            <div style={{display:"flex",gap:"8px",flexWrap:"wrap"}}>
              {Object.entries(MODES).map(([k,v])=>(
                <div key={k} onClick={()=>setMode(k)}
                  style={{background:"#050518",border:`1px solid ${mode===k?v.color:v.color+"33"}`,
                    padding:"6px 10px",cursor:"pointer",flex:"1",minWidth:"140px"}}>
                  <div style={{color:v.color,fontWeight:"bold",fontSize:"12px",marginBottom:"3px"}}>{k} {v.name}</div>
                  <div style={{color:"#445",fontSize:"9px"}}>{v.desc}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* ══ TAB: DOMAINS ══ */}
      {tab==="DOMAINS" && (
        <div>
          <div style={{color:"#334",fontSize:"9px",letterSpacing:"1px",marginBottom:"8px"}}>
            ▸ 16 DOMAINS — desire field × MCP binding × Caputo α weighting
          </div>
          <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fill,minmax(170px,1fr))",gap:"5px"}}>
            {domains.map(d=>{
              const aW = +(d.desire/5*α).toFixed(4);
              const haloIdx = Math.round(aW*192);
              return (
                <div key={d.id} style={{background:"#07071e",border:`1px solid ${d.color}44`,padding:"7px"}}>
                  <div style={{display:"flex",justifyContent:"space-between",marginBottom:"3px"}}>
                    <span style={{color:d.color,fontWeight:"bold",fontSize:"10.5px"}}>{d.id}</span>
                    <span style={{color:"#334",fontSize:"8px"}}>halo:{haloIdx}</span>
                  </div>
                  <div style={{color:"#334",fontSize:"8.5px",marginBottom:"5px"}}>mcp:{d.mcp}</div>
                  <div style={{display:"flex",gap:"2px",marginBottom:"4px"}}>
                    {[1,2,3,4,5].map(v=>(
                      <div key={v} onClick={()=>setDesire(d.id,v)}
                        style={{flex:1,height:"9px",cursor:"pointer",borderRadius:"1px",
                          background:v<=d.desire?d.color:"#111124",border:`1px solid ${d.color}33`}}/>
                    ))}
                  </div>
                  <div style={{fontSize:"8px",color:"#334"}}>α·w={aW} · {d.desire}/5</div>
                  <div style={{marginTop:"4px",background:"#0a0a20",height:"3px",borderRadius:"1px",overflow:"hidden"}}>
                    <div style={{width:`${(d.health||0.9)*100}%`,height:"100%",background:d.color+"88"}}/>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* ══ TAB: MANIFEST ══ */}
      {tab==="MANIFEST" && (
        <div>
          <div style={{color:"#334",fontSize:"9px",letterSpacing:"1px",marginBottom:"8px"}}>
            ▸ MCP MANIFEST — coherence-weighted tool coordinates · mobius_repo_connector.sh wired
          </div>
          <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fill,minmax(260px,1fr))",gap:"5px"}}>
            {Object.entries(MCP).map(([id,v])=>{
              const dom = domains.find(d=>d.mcp===id);
              const c = dom?.color||"#445";
              const aW = dom ? +(dom.desire/5*α).toFixed(4) : α.toFixed(4);
              const partial = v.url==="PARTIAL";
              return (
                <div key={id} style={{background:"#07071e",border:`1px solid ${c}33`,padding:"7px"}}>
                  <div style={{display:"flex",justifyContent:"space-between",marginBottom:"2px"}}>
                    <span style={{color:c,fontWeight:"bold",fontSize:"10px"}}>{id}</span>
                    <span style={{color:v.tier==="MCP"?"#9988ff":"#445",fontSize:"8px"}}>{v.tier}</span>
                  </div>
                  {dom && <div style={{color:"#334",fontSize:"8.5px",marginBottom:"2px"}}>domain: {dom.id}</div>}
                  {v.url && !partial &&
                    <div style={{color:"#1e2a3a",fontSize:"8px",wordBreak:"break-all",marginBottom:"2px"}}>{v.url}</div>}
                  {partial &&
                    <div style={{color:"#ffaa00",fontSize:"8px",marginBottom:"2px"}}>⚠ PARTIAL — connect via Claude Code</div>}
                  <div style={{color:c,fontSize:"8.5px"}}>α·w={aW}</div>
                </div>
              );
            })}
          </div>
          {/* mobius_repo_connector.sh preview */}
          <div style={{...card(),marginTop:"9px"}}>
            <div style={{color:"#334",fontSize:"9px",marginBottom:"6px"}}>mobius_repo_connector.sh — universal MIL adapter</div>
            <pre style={{fontSize:"8.5px",color:"#5566aa",margin:0,lineHeight:"1.65",overflowX:"auto"}}>{
`#!/bin/bash
# mobius_repo_connector.sh — Möbii³us Universal MIL Adapter
MIL_COMMAND=\${1:-$(cat)}
OPERATION=$(echo "$MIL_COMMAND" | jq -r '.operation')
INPUT=$(echo "$MIL_COMMAND" | jq '.input')
case $OPERATION in
  "predict")   OUTPUT=$(python3 scripts/wildfire_predict.py "$INPUT") ;;
  "analyze")   OUTPUT=$(python3 scripts/neuroplasticity_analysis.py "$INPUT") ;;
  "audit")     OUTPUT=$(python3 scripts/quantum_ethics_audit.py "$INPUT") ;;
  "forecast")  OUTPUT=$(python3 scripts/weather_input_hybrid.py "$INPUT") ;;
  "fuse")      OUTPUT=$(python3 kernel/triadic_fusion.py "$INPUT") ;;
  *)           echo '{"error":"Unknown operation"}'; exit 1 ;;
esac
echo "{\\"input\\":$INPUT,\\"operation\\":\\"$OPERATION\\",\\"output\\":\\"$OUTPUT\\",\\"confidence\\":${coherence}}"
`}</pre>
          </div>
        </div>
      )}

      {/* ══ TAB: PACKET ══ */}
      {tab==="PACKET" && (
        <div>
          <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:"8px"}}>
            <div style={{color:"#334",fontSize:"9px",letterSpacing:"1px"}}>
              ▸ Dr.Sh"if"+t'wHERE(now.u) FORWARD PACKET · tailly.cc:1029 / ahig.xyz:1028
            </div>
            <div style={{display:"flex",gap:"6px"}}>
              <button onClick={forwardPacket} style={btn(false,"#9988ff")}>↺ REGEN</button>
              <button onClick={copyPkt} style={btn(copied,"#00ff88")}>
                {copied?"✓ COPIED":"⎘ COPY"}
              </button>
            </div>
          </div>
          {!packet ? (
            <div style={{...card(),textAlign:"center",padding:"30px",color:"#334"}}>
              Click ⟶ Dr.SHIFT to generate and forward the coordinate packet.
            </div>
          ) : (
            <pre style={{background:"#050515",border:"1px solid #1a1a33",padding:"10px",
              fontSize:"8.5px",color:"#7788aa",lineHeight:"1.6",maxHeight:"480px",overflowY:"auto",overflowX:"auto"}}>
              {JSON.stringify(packet,null,2)}
            </pre>
          )}
        </div>
      )}

      {/* ── FART TRAIL ── */}
      <div style={{marginTop:"8px",background:"#050510",border:"1px solid #1a1a2e",padding:"6px 8px"}}>
        <div style={{color:"#223",fontSize:"8.5px",marginBottom:"3px",letterSpacing:"1px"}}>
          ▸ FAST/FART PROVENANCE TRAIL · tailly.cc:1029 · α={α} · β=ζ(dA/dt,dB/dt) · mode={mode}
        </div>
        <div ref={fartRef} style={{height:"72px",overflowY:"auto",fontSize:"9px",lineHeight:"1.75"}}>
          {fart.map((f,i)=>(
            <div key={i} style={{color:i===fart.length-1?f.color:"#2a3a4a",display:"flex",gap:"8px"}}>
              <span style={{color:"#1e2a3a",flexShrink:0}}>{f.ts}</span>
              <span style={{color:i===fart.length-1?"#334":"#1a2a2a",flexShrink:0}}>[{f.tag}]</span>
              <span>{f.msg}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}