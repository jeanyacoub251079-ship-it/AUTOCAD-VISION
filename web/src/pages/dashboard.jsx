import React, { useEffect, useState } from 'react'
import { api } from '../api.js'
import { nav } from '../app.jsx'

export default function Dashboard({ status }) {
  const [projects, setProjects] = useState([])
  const [alerts, setAlerts] = useState([])
  const [err, setErr] = useState('')
  const load = () => {
    api('/projects').then(r => setProjects(r.projects || [])).catch(e => setErr(e.message))
    api('/projects/-/alerts').catch(() => api('/status'))
  }
  useEffect(load, [])
  const b = status?.budget || {}
  return (
    <div className="grid cols-2">
      <div className="card">
        <div className="row" style={{ justifyContent: 'space-between' }}>
          <h2>Projets récents</h2>
          <button onClick={() => nav('new')}>Nouveau projet</button>
        </div>
        <table>
          <thead><tr><th>Nom</th><th>Réf.</th><th>Statut</th><th>Plans</th><th>Options</th><th>MAJ</th></tr></thead>
          <tbody>
            {projects.map(p => (
              <tr key={p.id} className="clickable" onClick={() => nav('project/' + p.id)}>
                <td>{p.name}</td><td>{p.ref || '—'}</td>
                <td><span className="pill mut">{p.status}</span></td>
                <td>{p.n_plans}</td><td>{p.n_options}</td>
                <td className="muted small">{(p.updated_at || '').slice(0, 16)}</td>
              </tr>
            ))}
            {!projects.length && <tr><td colSpan="6" className="muted">Aucun projet — créez-en un pour commencer.</td></tr>}
          </tbody>
        </table>
        {err && <div className="err">{err}</div>}
      </div>
      <div className="col">
        <div className="card">
          <h2>État du système</h2>
          {status ? (
            <div className="col small">
              <div className="kpi">
                <div><b>{status.ia_disponible ? 'en ligne' : 'dégradé'}</b>IA (Anthropic/OpenAI)</div>
                <div><b>{(b.jour?.usd || 0).toFixed(2)} / {b.plafond_jour_usd ?? '—'} $</b>dépensés aujourd'hui</div>
                <div><b>{status.prompts?.length || 0}</b>prompts chargés</div>
                <div><b>{status.db?.integrity ? 'ok' : 'KO'}</b>base SQLite</div>
              </div>
              <div className={status.ia_disponible ? 'box-ok' : 'box-warn'}>
                {status.ia_disponible
                  ? 'Fournisseurs configurés. Seuls Claude Opus (Anthropic) et ChatGPT (OpenAI) sont activés — choix contractuel du projet.'
                  : 'Mode dégradé : aucune clé API. Tout le pipeline fonctionne en local (saisie manuelle de l’interprétation, génération algorithmique).'}
              </div>
              <div className="muted">Données : {status.data_dir} — hors-ligne, aucun serveur distant hormis les appels IA.</div>
            </div>
          ) : <div className="muted">chargement…</div>}
        </div>
        <div className="card">
          <h2>Avertissements récents</h2>
          <AlertList alerts={alerts} setAlerts={setAlerts} />
        </div>
      </div>
    </div>
  )
}

function AlertList({ alerts, setAlerts }) {
  useEffect(() => { api('/projects').then(async r => {
    const list = []
    for (const p of (r.projects || []).slice(0, 5)) {
      const a = await api(`/projects/${p.id}/alerts`).catch(() => ({ alerts: [] }))
      a.alerts?.filter(x => x.decision === 'en_attente').forEach(x => list.push({ ...x, project: p.name }))
    }
    setAlerts(list)
  }).catch(() => {}) }, [])
  if (!alerts.length) return <div className="muted small">Aucune alerte en attente.</div>
  return (
    <div className="col small">
      {alerts.map(a => (
        <div key={a.id} className="box-warn">
          <b>{a.project}</b> — {a.kind} : {a.detail}
          <div className="row end">
            <button className="ghost" onClick={async () => { await api(`/projects/${a.project_id}/alerts/${a.id}`, { method: 'POST', body: { decision: 'ignoree' } }); setAlerts(x => x.filter(y => y.id !== a.id)) }}>Ignorer</button>
          </div>
        </div>
      ))}
    </div>
  )
}
