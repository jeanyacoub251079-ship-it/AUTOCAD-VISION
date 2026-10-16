import React, { useEffect, useMemo, useState } from 'react'
import { api } from '../api.js'
import Plan2D from '../components/plan2d.jsx'

// Phase 9 : éditeur structurel 2D + iso, modifications justifiées, recalcul,
// Ctrl+Z, figeage en snapshot immuable.
export default function EditorPage({ pid, optionId, setOptionId }) {
  const [opts, setOpts] = useState([])
  const [data, setData] = useState(null)       // {option, status, rank, iso_svg}
  const [selected, setSelected] = useState(null)
  const [view, setView] = useState('2d')
  const [dirty, setDirty] = useState(false)
  const [banner, setBanner] = useState('')
  const [hist, setHist] = useState([])
  const [reasonFor, setReasonFor] = useState(null) // {run: fn, label}
  const [reasonText, setReasonText] = useState('')

  useEffect(() => { api(`/projects/${pid}/options`).then(r => {
    const o = r.options || []
    setOpts(o)
    if (!optionId && o.length) setOptionId((o.find(x => x.status === 'retenue' || x.status === 'figee') || o[0]).id)
  }).catch(() => {}) }, [pid])
  useEffect(() => { if (optionId) refreshOption() }, [optionId])

  const refreshOption = async () => {
    const d = await api(`/projects/${pid}/options/${optionId}`)
    setData(d); setDirty(false)
  }
  const loadEdits = () => api(`/projects/${pid}/options/${optionId}/edits`).then(r => setHist(r.edits || [])).catch(() => {})
  useEffect(loadEdits, [optionId, dirty])

  const st = data?.option?.structure
  const conf = data?.option?.conformite || {}
  const nonConf = Object.values(conf).some(v => v === 'non_conforme')
  const ind = data?.option?.indicateurs || {}

  // ---- opérations avec raison obligatoire ---------------------------------
  const askReason = (label, run) => { setReasonFor({ label, run }); setReasonText('') }
  const commitReason = async () => {
    if (!reasonText.trim()) return
    try {
      const r = await api(`/projects/${pid}/options/${optionId}/edit`, { method: 'POST', body: { ...reasonFor.run, reason: reasonText.trim() } })
      setData(d => ({ ...d, option: { ...d.option, structure: r.structure, indicateurs: r.indicateurs, conformite: r.conformite }, }))
      setDirty(true)
      if ((r.conformite && Object.values(r.conformite).some(v => v === 'non_conforme')))
        setBanner('ALERTE : cette modification rend l’option NON CONFORME — voyant rouge.')
      else setBanner('')
      setReasonFor(null)
    } catch (e) { setBanner('Recalcul refusé : ' + (typeof e.detail === 'string' ? e.detail : e.message)) }
  }

  const moveEl = id => {
    if (!st) return
    const el = st.poteaux?.find(p => p.id === id)
    if (!el) return
    setReasonFor({ label: `Déplacer ${id}`, run: { op: 'move_poteau', element: id, position: el._pending || el.position } })
  }
  const onMove = (id, pos) => {
    const el = st?.poteaux?.find(p => p.id === id)
    if (!el) return
    el.position = pos
    setData({ ...data })
    setReasonFor({ label: `Déplacer le poteau ${id} en (${pos[0]} ; ${pos[1]}) m`, run: { op: 'move_poteau', element: id, position: pos } })
  }
  useEffect(() => {
    const f = e => { if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'z') { e.preventDefault(); undo() } }
    window.addEventListener('keydown', f)
    return () => window.removeEventListener('keydown', f)
  }, [optionId])
  const undo = async () => {
    try {
      const r = await api(`/projects/${pid}/options/${optionId}/undo`, { method: 'POST', body: {} })
      await refreshOption(); setBanner('Dernière édition annulée.')
    } catch (e) { setBanner('Rien à annuler.') }
  }

  const freeze = async () => {
    await api(`/projects/${pid}/options/${optionId}/freeze`, { method: 'POST', body: {} })
    await refreshOption(); setBanner('Version figée : snapshot ZIP immuable créé — toute nouvelle édition devra être justifiée.')
  }
  const recalc = async () => {
    const r = await api(`/projects/${pid}/options/${optionId}/recalc`, { method: 'POST', body: {} })
    await refreshOption(); setBanner('Recalculé.')
  }

  const props = useMemo(() => {
    if (!st || !selected) return null
    for (const k of ['poteaux', 'poutres', 'voiles', 'dalles', 'fondations']) {
      const el = (st[k] || []).find(x => x.id === selected)
      if (el) return { kind: k, el }
    }
    return { kind: '?', el: { id: selected } }
  }, [st, selected])

  if (!opts.length) return <div className="card">Aucune option à éditer — générez d’abord (étape 7).</div>

  return (
    <div className="col">
      {nonConf && <div className="box-bad"><b>⚠ ALERTE ROUGE — NON-CONFORMITÉ</b> : des vérifications dépassent le taux de 1,0. Corrigez ou annulez avant tout usage des livrables.</div>}
      {banner && <div className={nonConf ? 'box-bad' : 'box-ok'}>{banner}</div>}
      <div className="card">
        <div className="row">
          <label className="f">Option
            <select value={optionId || ''} onChange={e => setOptionId(e.target.value)}>
              {opts.map(o => <option key={o.id} value={o.id}>{o.rank}. {o.short_desc} [{o.status}]</option>)}
            </select>
          </label>
          <div className="row" style={{ marginTop: 16 }}>
            <button className={view === '2d' ? '' : 'ghost'} onClick={() => setView('2d')}>2D</button>
            <button className={view === 'iso' ? '' : 'ghost'} onClick={() => setView('iso')}>Iso 3D</button>
            <button className="ghost" onClick={recalc}>Recalculer</button>
            <button className="ghost" onClick={undo}>Annuler la dernière édition (Ctrl+Z)</button>
            <button onClick={freeze}>Figer cette version</button>
          </div>
          <span className="muted small" style={{ marginTop: 18 }}>taux max {ind.taux_travail_max} · béton {ind.volume_beton_m3} m³ · acier {ind.masse_acier_kg} kg · {data?.status === 'figee' ? 'FIGÉE' : dirty ? 'modifications non figées' : 'à jour'}</span>
        </div>
        <Plan2D height={540} structure={st} mode={data?.status === 'figee' ? 'view' : 'edit'}
                selected={selected} onSelect={setSelected}
                onMoveElement={data?.status === 'figee' ? undefined : onMove}
                onAddPoteau={p => setReasonFor({ label: 'Ajouter un poteau', run: { op: 'add_poteau', position: p } })}
                onAddPoutre={(a, b) => setReasonFor({ label: 'Ajouter une poutre', run: { op: 'add_poutre', debut: a, fin: b, section: [0.25, 0.5], niveau: 1 } })}
                onAddVoile={(a, b) => setReasonFor({ label: 'Ajouter un voile', run: { op: 'add_poutre', debut: a, fin: b, section: [0.2, 0.2], niveau: 1, voile: true } })}
                isoSvg={data?.iso_svg} />
        {props && (
          <div className="prop-panel" style={{ position: 'static', width: '100%', marginTop: 8 }}>
            <b>{props.kind} · {props.el.id}</b>
            <pre className="small" style={{ margin: 4, maxHeight: 120, overflow: 'auto' }}>{JSON.stringify(props.el, null, 1)}</pre>
            {['poteaux', 'poutres'].includes(props.kind) && (
              <button className="ghost" onClick={() => {
                const v = window.prompt(`Nouvelle section b×h (m) pour ${props.el.id} :`, (props.el.section || []).join('×'))
                if (v) { const [b, h] = v.split('×').map(parseFloat); if (b && h) setReasonFor({ label: `Section de ${props.el.id} → ${b}×${h}`, run: { op: props.kind === 'poteaux' ? 'set_poteau_section' : 'set_poutre_section', element: props.el.id, section: [b, h] } }) }
              }}>Changer la section</button>
            )}
            <button className="danger" style={{ marginLeft: 8 }} onClick={() =>
              setReasonFor({ label: `Supprimer ${props.el.id}`, run: { op: 'delete_element', element: props.el.id } })}>Supprimer l’élément</button>
          </div>
        )}
      </div>

      <div className="grid cols-2">
        <div className="card">
          <h3>Journal des éditions (justification obligatoire)</h3>
          <table><thead><tr><th>Date</th><th>Type</th><th>Élément</th><th>Raison</th></tr></thead>
            <tbody>{hist.map(h => <tr key={h.id}><td className="small">{(h.date || '').slice(0, 16)}</td><td>{h.type}</td><td>{h.element}</td><td>{h.reason}</td></tr>)}</tbody></table>
        </div>
        <div className="card">
          <h3>Derniers résultats de vérification</h3>
          <VerifMini resultats={data?.option?.resultats_calcul} />
        </div>
      </div>

      {reasonFor && (
        <div className="modal-bg" onClick={e => e.target === e.currentTarget && setReasonFor(null)}>
          <div className="modal">
            <h2>Justifier la modification</h2>
            <p>{reasonFor.label}</p>
            <textarea rows={3} autoFocus placeholder="Raison (obligatoire, journalisée au rapport de traçabilité)…"
                      value={reasonText} onChange={e => setReasonText(e.target.value)} />
            <div className="row end" style={{ marginTop: 8 }}>
              <button className="ghost" onClick={() => setReasonFor(null)}>Annuler</button>
              <button disabled={!reasonText.trim()} onClick={commitReason}>Appliquer &amp; recalculer</button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

function VerifMini({ resultats }) {
  const [filter, setFilter] = useState('')
  if (!resultats) return <div className="muted small">pas de résultats</div>
  const all = resultats.verifications || []
  const shown = all.filter(v => !filter || v.verification === filter).sort((a, b) => (b.taux_travail || 0) - (a.taux_travail || 0)).slice(0, 40)
  return (
    <>
      <div className="row small" style={{ marginBottom: 6 }}>
        {['', 'flexion', 'effort_tranchant', 'fleche', 'flambement', 'fissuration', 'sismique', 'constructif'].map(k => (
          <button key={k || 'all'} className={filter === k ? '' : 'ghost'} onClick={() => setFilter(k)}>{k || 'tous'}</button>
        ))}
        <span className="muted">{all.length} vérifications</span>
      </div>
      <table><thead><tr><th>Élément</th><th>Vérif.</th><th>Comb.</th><th>Sollicit.</th><th>Capacité</th><th>Taux</th><th /></tr></thead>
        <tbody>{shown.map((v, i) => (
          <tr key={i}>
            <td>{v.element}</td><td>{v.verification}</td><td className="small">{v.combinaison}</td>
            <td>{v.sollicitation_kN ?? v.valeur_mm ?? '—'}</td><td>{v.resistance_kN ?? v.limite_mm ?? '—'}</td>
            <td>{v.taux_travail}</td><td><span className={v.statut === 'conforme' ? 'pill ok' : 'pill bad'}>{v.statut}</span></td>
          </tr>))}</tbody></table>
    </>
  )
}
