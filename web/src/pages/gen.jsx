import React, { useEffect, useState } from 'react'
import { api, fileUrl } from '../api.js'
import { JobProgress, useJob } from '../components/job.jsx'
import { nav } from '../app.jsx'

// Phase 7-8 : génération des options (exploration locale ± IA créative) + comparateur.
export default function GenPage({ pid, refresh }) {
  const [cfg, setCfg] = useState(null)
  const [opts, setOpts] = useState([])
  const [nb, setNb] = useState(5)
  const [crit, setCrit] = useState('simplicite_mise_en_oeuvre')
  const [seed, setSeed] = useState(() => Math.floor(Math.random() * 1e6))
  const [useAi, setUseAi] = useState(false)
  const [thumbs, setThumbs] = useState({})
  const job = useJob()
  const [err, setErr] = useState('')

  const load = () => api(`/projects/${pid}/options`).then(r => setOpts(r.options || [])).catch(e => setErr(e.message))
  useEffect(() => {
    api(`/projects/${pid}/generation/config`).then(c => { setCfg(c); setSeed(c.params.seed || seed); setCrit(c.params.critere_classement || crit) }).catch(e => setErr(e.message))
    load()
  }, [pid])

  const run = async () => {
    setErr('')
    try {
      await job.run(`/projects/${pid}/generate`, { nb_options: nb, critere_classement: crit, seed, use_ai: useAi })
      await load()
      opts.forEach(render)
      refresh && refresh()
    } catch (e) { setErr(e.message) }
  }
  const render = async o => {
    try { const r = await api(`/projects/${pid}/options/${o.id}/render`, { method: 'POST', body: {} }); setThumbs(t => ({ ...t, [o.id]: r.png })) } catch (e) { }
  }
  useEffect(() => { opts.forEach(render) }, [opts.map(o => o.id).join()])

  const [sort, setSort] = useState({ k: 'rank', dir: 1 })
  const sorted = [...opts].sort((a, b) => {
    const get = o => sort.k === 'rank' ? (o.rank || 99)
      : sort.k === 'desc' ? o.short_desc
        : (o.indicators?.[sort.k] ?? 9e9)
    const x = get(a), y = get(b)
    return (typeof x === 'string' ? String(x).localeCompare(y) : x - y) * sort.dir
  })
  const select = async o => {
    if (o.status === 'figee' || o.status === 'retenue') { nav(`project/${pid}/editor`); return }
    await api(`/projects/${pid}/options/${o.id}/select`, { method: 'POST', body: { raison: 'sélection comparateur' } })
    await load(); nav(`project/${pid}/editor`)
  }

  return (
    <div className="col">
      <div className="card">
        <h2>Génération d’options structurelles</h2>
        <div className="row">
          <label className="f">Nombre visé (3–5)<input type="number" min="3" max="5" value={nb} onChange={e => setNb(+e.target.value)} style={{ width: 70 }} /></label>
          <label className="f">Critère de classement
            <select value={crit} onChange={e => setCrit(e.target.value)}>
              <option value="simplicite_mise_en_oeuvre">Simplicité de mise en œuvre</option>
              <option value="masse_acier">Économie d’acier</option>
              <option value="volume_beton">Économie de béton</option>
              <option value="performance_sismique">Performance sismique</option>
              <option value="marge_structurelle">Marge structurelle</option>
            </select>
          </label>
          <label className="f">Seed (reproductibilité)<input type="number" value={seed} onChange={e => setSeed(+e.target.value)} style={{ width: 110 }} /></label>
          <label className="small" style={{ marginTop: 18 }}>
            <input type="checkbox" checked={useAi} onChange={e => setUseAi(e.target.checked)} /> Activer l’IA créative
            (pistes envoyées au modèle de raisonnement — JSON abstrait uniquement, jamais le plan)
            {cfg?.estimation_ia && <span className="muted"> · est. {cfg.estimation_ia.cout_estime_usd?.toFixed(3)} $</span>}
          </label>
          <button onClick={run} disabled={job.running}>{job.running ? 'calcul…' : 'Générer'}</button>
        </div>
        {cfg && <div className="muted small">Exploration : {cfg.generation.max_options_calculees} options max en calcul complet ·
          {' '}portées {cfg.generation.portee_min_m}–{cfg.generation.portee_max_m} m · épaisseurs dalles {cfg.generation.epaisseurs_dalle_m.join('/')} m ·
          {' '}filtre : seules les options 100 % conformes sont présentées.</div>}
        <JobProgress job={job.job} running={job.running} onCancel={job.cancel} />
        {job.job?.result?.diagnostic && <div className="box-warn small">{job.job.result.diagnostic}</div>}
        {err && <div className="box-bad small">{err}</div>}
      </div>

      <div className="card">
        <h2>Comparateur <span className="muted small">({opts.length} option(s))</span></h2>
        <table>
          <thead>
            <tr>
              {[['rank', '#'], ['desc', 'Description'], ['volume_beton_m3', 'Béton m³'], ['masse_acier_kg', 'Acier kg'],
                ['taux_travail_max', 'Taux max'], ['fleche_max_mm', 'Flèche mm'], ['derrive_max_mm', 'Dérive mm'],
                ['cost_index', 'Coût ind.'], ['conformite', 'Conformité'], ['status', 'Statut'], ['', '']]
                .map(([k, l]) => (
                  <th key={l} onClick={() => k && setSort(s => ({ k, dir: s.k === k ? -s.dir : 1 }))}>{l} {sort.k === k ? (sort.dir > 0 ? '↑' : '↓') : ''}</th>
                ))}
            </tr>
          </thead>
          <tbody>
            {sorted.map(o => {
              const i = o.indicators || {}
              return (
                <tr key={o.id}>
                  <td>{o.rank}</td>
                  <td><a href="#" onClick={e => { e.preventDefault(); nav(`project/${pid}/editor/${o.id}`) }}>{o.short_desc}</a>
                    <div className="muted small">{o.method} · seed {o.seed}{o.n_edits ? ` · ${o.n_edits} édits` : ''}</div></td>
                  <td>{i.volume_beton_m3}</td><td>{i.masse_acier_kg}</td>
                  <td>{i.taux_travail_max} {i.taux_travail_max > 1 && <span className="pill bad">!</span>}</td>
                  <td>{i.fleche_max_mm}</td><td>{i.derive_max_mm}</td><td>{i.cost_index ?? '—'}</td>
                  <td>{Object.entries(o.conformity || {}).map(([k, v]) => <span key={k} className={v === 'non_conforme' ? 'pill bad' : 'pill ok'} style={{ marginRight: 3 }}>{k}</span>)}</td>
                  <td><span className={o.status === 'retenue' || o.status === 'figee' ? 'pill ok' : o.status === 'rejetee' ? 'pill bad' : 'pill mut'}>{o.status}</span></td>
                  <td className="row">
                    {o.status !== 'retenue' && o.status !== 'figee' && <button onClick={() => select(o)}>Retenir</button>}
                    {(o.status === 'retenue' || o.status === 'figee') && <button className="ghost" onClick={() => select(o)}>Éditer</button>}
                    <button className="ghost" onClick={() => api(`/projects/${pid}/options/${o.id}/reject`, { method: 'POST', body: {} }).then(load)}>Rejeter</button>
                  </td>
                </tr>
              )
            })}
            {!opts.length && <tr><td colSpan="10" className="muted">Aucune option — lancez la génération (étape 7).</td></tr>}
          </tbody>
        </table>
        <h3>Vignettes</h3>
        <div className="grid cols-3 thumbs">
          {sorted.slice(0, 6).map(o => (
            <div key={o.id} className="card" style={{ padding: 6 }}>
              {thumbs[o.id] ? <img src={fileUrl(pid, thumbs[o.id])} alt={o.id} /> : <div className="muted small">rendu…</div>}
              <div className="small"><b>{o.rank}. {o.short_desc}</b></div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
