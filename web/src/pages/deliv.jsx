import React, { useEffect, useState } from 'react'
import { api } from '../api.js'
import { JobProgress, useJob } from '../components/job.jsx'

// Phase 10 : aperçu avant export puis génération des livrables.
export default function DelivPage({ pid }) {
  const [opts, setOpts] = useState([])
  const [oid, setOid] = useState('')
  const [inc, setInc] = useState({ plans: true, note: true, quantitatifs: true, traacabilite: true })
  const [useAi, setUseAi] = useState(true)
  const [dels, setDels] = useState([])
  const [preview, setPreview] = useState(null)
  const [dest, setDest] = useState('')
  const [msg, setMsg] = useState('')
  const job = useJob()

  useEffect(() => {
    api(`/projects/${pid}/options`).then(r => {
      const o = r.options || []
      setOpts(o)
      setOid((o.find(x => x.status === 'retenue' || x.status === 'figee') || o[0])?.id || '')
    }).catch(() => {})
    loadDels()
  }, [pid])
  const loadDels = () => api(`/projects/${pid}/deliverables`).then(r => setDels(r.deliverables || [])).catch(() => {})

  const previewNow = async () => {
    try {
      const o = await api(`/projects/${pid}/options/${oid}`)
      const r = await api(`/projects/${pid}/options/${oid}/render`, { method: 'POST', body: {} })
      setPreview({ opt: o.option, png: r.png })
    } catch (e) { setMsg('Aperçu indisponible : ' + e.message) }
  }

  const generate = async () => {
    setMsg('')
    try {
      await job.run(`/projects/${pid}/deliverables`, {
        option_id: oid,
        include: Object.entries(inc).filter(([, v]) => v).map(([k]) => k),
        use_ai_drafting: useAi
      })
      await loadDels()
      setMsg('Livrables produits et journalisés (hash SHA-256 par fichier).')
    } catch (e) { setMsg('Échec : ' + e.message) }
  }
  const copyOut = async () => {
    try {
      const ids = dels.map(d => d.id)
      const r = await api(`/projects/${pid}/deliverables/export`, { method: 'POST', body: { dest_dir: dest, ids } })
      setMsg(`${r.copied.length} fichier(s) copiés vers ${dest}`)
    } catch (e) { setMsg(e.message) }
  }

  const i = preview?.opt?.indicateurs || {}
  return (
    <div className="grid cols-2">
      <div className="card">
        <h2>Composer les livrables</h2>
        <label className="f">Option
          <select value={oid} onChange={e => setOid(e.target.value)}>
            {opts.map(o => <option key={o.id} value={o.id}>{o.rank}. {o.short_desc} [{o.status}]</option>)}
          </select>
        </label>
        <div className="col small" style={{ margin: '8px 0' }}>
          {[['plans', 'Plans DXF (fondations, coffrage, ferraillage) — AC2013, unités mm, calques figés'],
            ['note', 'Note de calcul PDF (11 sections, vérifications EC2/EC8 chiffrées)'],
            ['quantitatifs', 'Quantitatif estimatif CSV + XLSX (béton m³ / acier kg / coffrage m²)'],
            ['traacabilite', 'Rapport de traçabilité complet (normatif + IA +éditions)']].map(([k, l]) => (
            <label key={k}><input type="checkbox" checked={inc[k]} onChange={e => setInc(v => ({ ...v, [k]: e.target.checked }))} /> {l}</label>
          ))}
          <label><input type="checkbox" checked={useAi} onChange={e => setUseAi(e.target.checked)} /> Rédaction assistée des sections narratives par l’IA (marquée « assistance IA », 100 % local si décoché)</label>
        </div>
        <div className="row">
          <button className="ghost" onClick={previewNow}>Aperçu avant export</button>
          <button onClick={generate} disabled={job.running || !oid}>{job.running ? 'production…' : 'Générer les livrables'}</button>
        </div>
        <JobProgress job={job.job} running={job.running} onCancel={job.cancel} />
        {msg && <div className="box-ok small">{msg}</div>}
        <div className="box-warn small" style={{ marginTop: 8 }}>Ces documents sont des <b>propositions</b> : aucune signature d’ingénieur, aucune garantie réglementaire — la vérification finale vous incombe (ou à votre ingénieur référent).</div>
      </div>
      <div className="card">
        <h2>Aperçu</h2>
        {preview ? (<>
          <img src={`/api/projects/${pid}/file?path=${encodeURIComponent(preview.png)}`} style={{ width: '100%', border: '1px solid var(--line)', borderRadius: 6 }} alt="aperçu" />
          <div className="kpi small" style={{ marginTop: 8 }}>
            <div><b>{i.taux_travail_max}</b>taux max</div>
            <div><b>{i.volume_beton_m3}</b>conso béton m³</div>
            <div><b>{i.masse_acier_kg}</b>acier kg</div>
            <div><b>{i.fleche_max_mm}</b>flèche max mm</div>
          </div>
        </>) : <div className="muted small">Aperçu du plan de coffrage + indicateurs avant production.</div>}
      </div>

      <div className="card" style={{ gridColumn: '1 / -1' }}>
        <h2>Livrables produits</h2>
        <table><thead><tr><th>Date</th><th>Type</th><th>Fichier</th><th>Taille</th><th>SHA-256</th><th /></tr></thead>
          <tbody>{dels.map(d => (
            <tr key={d.id}>
              <td className="small">{(d.created_at || '').slice(0, 16)}</td><td>{d.type}</td>
              <td className="small">{d.path}</td><td>{((d.meta && 0) || 0) || ''}</td>
              <td className="small muted">{(d.sha256 || '').slice(0, 16)}…</td>
              <td><a href={`/api/projects/${pid}/deliverables/${d.id}/file`} download>Télécharger</a></td>
            </tr>))}</tbody></table>
        <div className="row small" style={{ marginTop: 8 }}>
          <input placeholder="répertoire de copie (ex: /home/user/livrables)" value={dest} onChange={e => setDest(e.target.value)} style={{ width: 320 }} />
          <button className="ghost" onClick={copyOut} disabled={!dels.length}>Copier tout vers ce dossier</button>
        </div>
      </div>
    </div>
  )
}
