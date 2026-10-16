import React, { useEffect, useMemo, useRef, useState } from 'react'

// Visionneuse / éditeur structurel 2D SVG — zoom molette, pan glisser,
// sélection, déplacement de poteaux, ajout poteau/poutre (mode édition).
export default function Plan2D({
  structure, pngBg, mode = 'view', grid = true,
  selected, onSelect, onMoveElement, onAddPoteau, onAddPoutre, onAddVoile,
  overlays, isoSvg, height = 560
}) {
  const st = structure || { poteaux: [], poutres: [], voiles: [], dalles: [], fondations: [] }
  const wrapRef = useRef(null)
  const [view, setView] = useState({ x: 0, y: 0, k: 40 })
  const [drag, setDrag] = useState(null)
  const [draft, setDraft] = useState(null)   // 2e clic pour poutre/voile
  const edit = mode === 'edit'
  const [add, setAdd] = useState('none')

  const extents = useMemo(() => {
    const pts = []
    st.poteaux?.forEach(c => pts.push(c.position))
    st.poutres?.forEach(b => { pts.push(b.debut); pts.push(b.fin) })
    st.voiles?.forEach(w => { pts.push(w.debut); pts.push(w.fin) })
    st.dalles?.forEach(d => d.polygone?.forEach(p => pts.push(p)))
    if (!pts.length) pts.push([0, 0], [12, 9])
    const xs = pts.map(p => p[0]), ys = pts.map(p => p[1])
    let x0 = Math.min(...xs) - 1.5, x1 = Math.max(...xs) + 1.5
    let y0 = Math.min(...ys) - 1.5, y1 = Math.max(...ys) + 1.5
    if (x1 - x0 < 2) { x0 -= 3; x1 += 3 }
    if (y1 - y0 < 2) { y0 -= 3; y1 += 3 }
    return { x0, y0, x1, y1 }
  }, [structure])

  const fit = () => {
    const el = wrapRef.current?.firstChild
    const w = el?.clientWidth || 900, h = height
    const k = Math.min(w / (extents.x1 - extents.x0), h / (extents.y1 - extents.y0)) * 0.95
    setView({ x: 0, y: 0, k })
  }
  useEffect(fit, [extents, height])

  const X = x => (x - extents.x0) * view.k + view.x + 10
  const Y = y => (extents.y1 - y) * view.k + view.y + 10
  const toWorld = (cx, cy) => {
    const r = wrapRef.current.firstChild.getBoundingClientRect()
    return [((cx - r.left) - view.x - 10) / view.k + extents.x0,
            extents.y1 - ((cy - r.top) - view.y - 10) / view.k]
  }

  const onWheel = e => {
    const f = e.deltaY < 0 ? 1.15 : 1 / 1.15
    setView(v => ({ ...v, k: Math.min(600, Math.max(4, v.k * f)) }))
  }
  const onDown = e => {
    if (e.target.dataset && e.target.dataset.elid && edit) {
      const [wx, wy] = toWorld(e.clientX, e.clientY)
      setDrag({ kind: 'move', id: e.target.dataset.elid, dx: wx, dy: wy, moved: false })
      onSelect && onSelect(e.target.dataset.elid)
      e.stopPropagation()
      return
    }
    setDrag({ kind: 'pan', sx: e.clientX, sy: e.clientY, vx: view.x, vy: view.y })
  }
  const onMove = e => {
    if (!drag) return
    if (drag.kind === 'pan') setView(v => ({ ...v, x: drag.vx + e.clientX - drag.sx, y: drag.vy + e.clientY - drag.sy }))
  }
  const onUp = e => {
    if (drag?.kind === 'move' && drag.moved) {
      const [wx, wy] = toWorld(e.clientX, e.clientY)
      onMoveElement && onMoveElement(drag.id, [Math.round(wx * 50) / 50, Math.round(wy * 50) / 50])
    }
    setDrag(null)
  }
  const onClick = e => {
    if (!edit) { if (e.target.dataset?.elid) onSelect && onSelect(e.target.dataset.elid); return }
    const [wx, wy] = toWorld(e.clientX, e.clientY)
    const p = [Math.round(wx * 50) / 50, Math.round(wy * 50) / 50]
    if (add === 'poteau') { onAddPoteau && onAddPoteau(p); return }
    if (add === 'poutre' || add === 'voile') {
      if (!draft) setDraft(p)
      else {
        const fn = add === 'poutre' ? onAddPoutre : onAddVoile
        fn && fn(draft, p)
        setDraft(null)
      }
      return
    }
    if (!e.target.dataset?.elid) onSelect && onSelect(null)
  }

  const gsz = 1
  const gridlines = []
  if (grid) {
    const step = view.k > 25 ? 1 : view.k > 10 ? 5 : 10
    for (let x = Math.ceil(extents.x0 / step) * step; x <= extents.x1; x += step)
      gridlines.push(<line key={'gx' + x} x1={X(x)} y1={0} x2={X(x)} y2={height} stroke="#eef3f6" />)
    for (let y = Math.ceil(extents.y0 / step) * step; y <= extents.y1; y += step)
      gridlines.push(<line key={'gy' + y} x1={0} y1={Y(y)} x2={9999} y2={Y(y)} stroke="#eef3f6" />)
  }

  return (
    <div className="plan-wrap" style={{ height }}
         ref={wrapRef} onWheel={onWheel} onMouseDown={onDown} onMouseMove={onMove}
         onMouseUp={onUp} onMouseLeave={onUp} onClick={onClick}>
      {pngBg && mode !== 'edit' && <img className="pngbg" src={pngBg} alt="plan" />}
      <svg>
        {gridlines}
        {/* dalles */}
        {(st.dalles || []).map(d => (
          <polygon key={d.id} data-elid={d.id}
                   points={(d.polygone || []).map(p => X(p[0]) + ',' + Y(p[1])).join(' ')}
                   fill="rgba(149,165,166,.14)" stroke="#95a5a6" strokeWidth="1"
                   style={{ cursor: edit ? 'pointer' : 'default' }} />
        ))}
        {/* fondations */}
        {(st.fondations || []).map(f => {
          const c = (st.poteaux || []).find(p => p.id === f.poteau)
          if (!c || f.type === 'radier') return f.type === 'radier' ? (
            <rect key={f.id} data-elid={f.id} x={X(extents.x0 + 1)} y={Y(extents.y1 - 1)}
                  width={(extents.x1 - extents.x0 - 2) * view.k} height={(extents.y1 - extents.y0 - 2) * view.k}
                  fill="none" stroke="#8e44ad" strokeDasharray="6 4" />
          ) : null
          const [B, L] = f.dimensions || [1.5, 1.5]
          return (
            <g key={f.id}>
              <rect data-elid={f.id} x={X(c.position[0] - B / 2)} y={Y(c.position[1] + L / 2)}
                    width={B * view.k} height={L * view.k} fill="rgba(142,68,173,.09)"
                    stroke="#8e44ad" strokeDasharray="5 3" strokeWidth="1.2" />
            </g>
          )
        })}
        {/* voiles */}
        {(st.voiles || []).map(w => (
          <g key={w.id}>
            <line data-elid={w.id} x1={X(w.debut[0])} y1={Y(w.debut[1])} x2={X(w.fin[0])} y2={Y(w.fin[1])}
                  stroke="#16a085" strokeWidth={Math.max(2, (w.epaisseur || .2) * view.k)} strokeLinecap="butt"
                  style={{ cursor: edit ? 'pointer' : 'default' }} />
            <text x={X((w.debut[0] + w.fin[0]) / 2)} y={Y((w.debut[1] + w.fin[1]) / 2) - 6}
                  fontSize="10" fill="#0e6655">{w.id}</text>
          </g>
        ))}
        {/* poutres */}
        {(st.poutres || []).map(b => (
          <g key={b.id}>
            <line data-elid={b.id} x1={X(b.debut[0])} y1={Y(b.debut[1])} x2={X(b.fin[0])} y2={Y(b.fin[1])}
                  stroke="#2471a3" strokeWidth={Math.max(1.5, (b.section[0]) * view.k * .5)}
                  opacity=".85" style={{ cursor: edit ? 'pointer' : 'default' }} />
            <text x={X((b.debut[0] + b.fin[0]) / 2)} y={Y((b.debut[1] + b.fin[1]) / 2)}
                  fontSize="8.5" fill="#21618c">{b.id} {Math.round(b.section[0] * 100)}×{Math.round(b.section[1] * 100)}</text>
          </g>
        ))}
        {/* poteaux */}
        {(st.poteaux || []).map(c => {
          const [w, h] = c.section || [.3, .3]
          const sel = selected === c.id
          return (
            <g key={c.id}>
              <rect data-elid={c.id} x={X(c.position[0] - w / 2)} y={Y(c.position[1] + h / 2)}
                    width={Math.max(4, w * view.k)} height={Math.max(4, h * view.k)}
                    fill={sel ? '#e74c3c' : '#c0392b'} stroke={sel ? '#641e16' : 'none'} strokeWidth="2"
                    style={{ cursor: edit ? 'grab' : 'pointer' }} />
              <text x={X(c.position[0]) + 8} y={Y(c.position[1]) - 6} fontSize="9" fill="#333">{c.id}</text>
            </g>
          )
        })}
        {/* overlays d'interprétation (murs détectés par l'IA, ouvertures) */}
        {overlays?.murs?.map(m => (
          <line key={'ov' + m.id} x1={X(m.debut[0])} y1={Y(m.debut[1])} x2={X(m.fin[0])} y2={Y(m.fin[1])}
                stroke={m.selected ? '#e67e22' : '#27ae60'} strokeWidth="2" strokeDasharray="8 4" />
        ))}
        {overlays?.ouvertures?.map(o => o.position && (
          <circle key={'oo' + o.id} cx={X(o.position[0])} cy={Y(o.position[1])} r="5"
                  fill="none" stroke="#f39c12" strokeWidth="2" />
        ))}
        {draft && <circle cx={X(draft[0])} cy={Y(draft[1])} r="4" fill="#e67e22" />}
      </svg>
      {edit && (
        <div className="row" style={{ position: 'absolute', left: 8, bottom: 8, background: 'rgba(255,255,255,.9)', padding: 4, borderRadius: 6, border: '1px solid var(--line)' }}>
          {[['none', 'Sélection'], ['poteau', '+ Poteau (clic)'], ['poutre', '+ Poutre (2 clics)'], ['voile', '+ Voile (2 clics)']].map(([k, l]) => (
            <button key={k} className={add === k ? '' : 'ghost'} onClick={e => { e.stopPropagation(); setAdd(k); setDraft(null) }}>{l}</button>
          ))}
          <button className="ghost" onClick={e => { e.stopPropagation(); fit() }}>Recadrer</button>
        </div>
      )}
      {mode === 'iso' && (
        <div style={{ position: 'absolute', inset: 0, background: '#fff', overflow: 'auto', padding: 10 }}
             dangerouslySetInnerHTML={{ __html: isoSvg || '<i>aperçu 3D indisponible</i>' }} />
      )}
    </div>
  )
}
