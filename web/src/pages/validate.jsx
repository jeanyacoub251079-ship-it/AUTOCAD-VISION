import React, { useEffect, useMemo, useState } from 'react'
import { api, fileUrl } from '../api.js'
import { JobProgress, useJob } from '../components/job.jsx'
import Plan2D from '../components/plan2d.jsx'

// Phases 5-6 : interprétation IA (ou saisie manuelle) + écran de validation/correction OBLIGATOIRE.
export default function ValidatePage({ pid, status, refresh }) {
  const [plans, setPlans] = useState([])
  const [planId, setPlanId] = useState('')
  const [items, setItems] = useState([])
  const [cur, setCur] = useState(null)
  const [jsonText, setJsonText] = useState('')
  const [validation, setValidation] = useState({ statut: '', corrections: [], incertitudes_traitees: [] })
  const [err, setErr] = useState('')
  const [msg, setMsg] = useState('')
  const [confirmed, setConfirmed] = useState(false)
  const [provider, setProvider] = useState('anthropic')
  const job = useJob()

  useEffect(() => {
    api(`/projects/${pid}/plans`).then(r => { const p = (r.plans || []).find(x => x.png_clean) || (r.plans || [])[0]; p && setPlanId(p.id); setPlans(r.plans || []) }).catch(() => {})
    loadItems()
  }, [pid])

  const loadItems = () => api(`/projects/${pid}/interpretations`).then(r => setItems(r.interpretations || [])).catch(() => {})
  const open = async iid => {
    const d = await api(`/projects/${pid}/interpretations/${iid}`)
    setCur(d); setJsonText(JSON.stringify(d.json, null, 1))
    setValidation(d.validation || { statut: '', corrections: [], incertitudes_traitees: [] })
  }
  useEffect(() => { if (items.length && !cur) open(items[0].id) }, [items])

  const parsed = useMemo(() => { try { return { ok: true, data: JSON.parse(jsonText) } } catch (e) { return { ok: false, err: e.message } } }, [jsonText])
  const plan = plans.find(p => p.id === planId)

  const runAI = async () => {
    setErr('')
    try { await job.run(`/projects/${pid}/interpretations/run`, { plan_id: planId, provider, confirmed }) ; await loadItems(); const l = await api(`/projects/${pid}/interpretations`); if (l.interpretations[0]) open(l.interpretations[0].id) }
    catch (e) { setErr(e.message) }
  }
  const saveManual = async () => {
    if (!parsed.ok) { setErr('JSON invalide : ' + parsed.err); return }
    try {
      const r = await api(`/projects/${pid}/interpretations/manual`, { method: 'POST', body: { plan_id: planId || null, json: parsed.data } })
      await loadItems(); await open(r.interpretation_id); setMsg('Interprétation manuelle enregistrée.')
    } catch (e) { setErr(typeof e.detail === 'string' ? e.detail : e.message) }
  }
  const save = async (valider) => {
    if (!cur) return
    if (!parsed.ok) { setErr('JSON invalide — corrigez avant d’enregistrer.'); return }
    const v = valider
      ? { statut: 'validee', corrections: validation.corrections || [], incertitudes_traitees: validation.incertitudes_traitees || [] }
      : null
    setErr(''); setMsg('')
    try {
      const r = await api(`/projects/${pid}/interpretations/${cur.id}`, {
        method: 'PUT',
        body: { json: parsed.data, ...(v ? { validation: v, force: force } : {}) }
      })
      await loadItems(); await open(cur.id)
      setMsg(r.validated ? 'Interprétation validée — la génération est débloquée.' : 'Enregistré (non validé).')
      refresh && refresh()
    } catch (e) {
      let d = e.detail
      try { d = typeof d === 'string' ? JSON.parse(d) : d } catch (_) { }
      setErr(d?.message ? JSON.stringify(d.message) + ' — ' + (d.pending || []).map(x => x.id).join(', ') : (typeof d === 'string' ? d : e.message))
    }
  }
  const [force, setForce] = useState(false)

  const addCorrection = () => {
    const champ = window.prompt('Champ corrigé (ex: epaisseur, fin) ?') || ''
    const el = window.prompt('Élément concerné (id du mur/ouverture) ?') || ''
    const raison = window.prompt('RAISON de la correction (obligatoire) ?') || ''
    if (!raison) { setErr('Une raison est obligatoire pour chaque correction.'); return }
    setValidation(v => ({ ...v, corrections: [...(v.corrections || []), { type: 'champ', element: el, champ, avant: '', apres: '', raison }] }))
  }

  const murs = parsed.ok ? (parsed.data.murs_porteurs || []) : []
  return (
    <div className="grid cols-2">
      <div className="col">
        <div className="card">
          <h2>Interprétation</h2>
          <div className="row small">
            <label className="f">Plan source
              <select value={planId} onChange={e => setPlanId(e.target.value)}>
                {plans.map(p => <option key={p.id} value={p.id}>{p.filename}{p.png_clean ? '' : ' (non parsé)'}</option>)}
              </select>
            </label>
            <label className="f">Fournisseur
              <select value={provider} onChange={e => setProvider(e.target.value)}>
                <option value="anthropic">Anthropic Claude Opus</option>
                <option value="openai">OpenAI ChatGPT</option>
              </select>
            </label>
          </div>
          <label className="small"><input type="checkbox" checked={confirmed} onChange={e => setConfirmed(e.target.checked)} />
            {' '}Je confirme l’envoi de l’image <b>nettoyée</b> du plan au fournisseur (données identifiantes retirées par mes soins en amont).</label>
          <div className="row">
            <button onClick={runAI} disabled={!confirmed || !planId || job.running}>Lancer l’interprétation IA</button>
            <span className="muted small">Coût et détail de l’envoi : vérifier l’aperçu en page « Import ».</span>
          </div>
          <JobProgress job={job.job} running={job.running} onCancel={job.cancel} />
          {msg && <div className="box-ok small">{msg}</div>}
          {err && <div className="box-bad small">{err}</div>}
          <h3>ou saisie manuelle (mode dégradé)</h3>
          <div className="row"><button className="ghost" onClick={saveManual}>Enregistrer le JSON ci-contre comme interprétation</button></div>
          <div className="muted small">Historique : {items.map(i => <a key={i.id} href="#" style={{ marginRight: 8 }} onClick={e => { e.preventDefault(); open(i.id) }}>{i.id} ({i.source}{i.validated ? ', validée' : ''})</a>)}</div>
        </div>

        {cur && (
          <div className="card">
            <h2>Correction / validation — {cur.id} <span className={cur.validated ? 'pill ok' : 'pill warn'}>{cur.validated ? 'validée' : 'en attente'}</span></h2>
            <div className="row small">
              <button className="ghost" onClick={addCorrection}>+ correction (raison obligatoire)</button>
              <span className="muted">{(validation.corrections || []).length} correction(s) journalisée(s)</span>
            </div>
            {(validation.corrections || []).map((c, i) => (
              <div key={i} className="small box-warn">{c.element} · {c.champ} → <b>{c.apres || '(à préciser dans le JSON)'}</b> — {c.raison}</div>
            ))}
            <h3>Incertitudes signalées — décision requise pour chacune</h3>
            {murs.length === 0 && !parsed.ok ? null : (parsed.ok ? (parsed.data.incertitudes || []) : []).map(u => {
              const done = (validation.incertitudes_traitees || []).find(t => t.id === u.id)
              return (
                <div key={u.id} className="row small" style={{ marginBottom: 4 }}>
                  <span style={{ flex: 1 }}><b>{u.id}</b> {u.description} <span className="muted">({u.impact})</span></span>
                  <select value={done?.decision || ''} onChange={e => {
                    const v = e.target.value
                    setValidation(x => {
                      const list = (x.incertitudes_traitees || []).filter(t => t.id !== u.id)
                      if (v) list.push({ id: u.id, decision: v, raison: v === 'corrige' ? 'corrigé dans le JSON' : 'acceptée en l’état' })
                      return { ...x, incertitudes_traitees: list }
                    })
                  }}>
                    <option value="">— décider —</option><option value="corrige">Corrigée</option><option value="accepte">Acceptée</option>
                  </select>
                </div>
              )
            })}
            <label className="small"><input type="checkbox" checked={force} onChange={e => setForce(e.target.checked)} /> Forcer la validation malgré incertitudes non traitées (déconseillé)</label>
            <div className="row">
              <button onClick={() => save(true)}>Valider cette interprétation</button>
              <button className="ghost" onClick={() => save(false)}>Enregistrer sans valider</button>
            </div>
            <div className="muted small">Sans validation, la génération d’options reste bloquée (point de contrôle humain n°2).</div>
          </div>
        )}
      </div>

      <div className="col">
        <div className="card">
          <h2>Superposition (détections sur plan)</h2>
          <Plan2D height={300} pngBg={plan ? fileUrl(pid, plan.png_clean) : null}
                 structure={{}}
                 overlays={{ murs, ouvertures: parsed.ok ? (parsed.data.ouvertures || []).filter(o => o.position) : [] }} />
        </div>
        <div className="card">
          <h2>JSON d’interprétation (éditable)</h2>
          <textarea rows={16} value={jsonText} onChange={e => setJsonText(e.target.value)} />
          {!parsed.ok && <div className="err">{parsed.err}</div>}
        </div>
      </div>
    </div>
  )
}
