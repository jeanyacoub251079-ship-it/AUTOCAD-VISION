import React, { useEffect, useState } from 'react'
import { api } from '../api.js'

// Traçabilité locale : journal des appels IA, budget, alertes, snapshots, incidents.
export default function LogsPage({ pid }) {
  const [ai, setAi] = useState({ calls: [], budget: {} })
  const [alerts, setAlerts] = useState([])
  const [snaps, setSnaps] = useState([])
  const [inc, setInc] = useState([])
  useEffect(() => {
    api(`/projects/${pid}/ai-calls`).then(setAi).catch(() => {})
    api(`/projects/${pid}/alerts`).then(r => setAlerts(r.alerts || [])).catch(() => {})
    api(`/projects/${pid}/snapshots`).then(r => setSnaps(r.snapshots || [])).catch(() => {})
    api('/incidents').then(r => setInc(r.incidents || [])).catch(() => {})
  }, [pid])
  const total = ai.calls.reduce((s, c) => s + (c.cost_usd || 0), 0)
  return (
    <div className="col">
      <div className="card">
        <h2>Journal des appels IA — projet</h2>
        <div className="muted small">Aucun contenu n’est stocké en clair : uniquement les empreintes (16 premiers hex) de la requête et de la réponse. Coût cumulé projet : {total.toFixed(4)} USD {ai.budget?.plafond_projet_usd ? ` / plafond ${ai.budget.plafond_projet_usd} $` : ''}.</div>
        <table><thead><tr><th>Date</th><th>Fournisseur</th><th>Modèle</th><th>Finalité</th><th>Tokens</th><th>Coût $</th><th>Req→</th><th>←Resp</th><th>Statut</th><th>s (lat.)</th></tr></thead>
          <tbody>{ai.calls.map(c => (
            <tr key={c.id}>
              <td className="small">{(c.datetime || '').slice(0, 19)}</td><td>{c.provider}</td><td>{c.model}</td>
              <td>{c.purpose}</td><td>{c.tokens_in}/{c.tokens_out}</td><td>{(c.cost_usd || 0).toFixed(4)}</td>
              <td className="muted">{(c.hash_req || '').slice(0, 8)}</td><td className="muted">{(c.hash_resp || '').slice(0, 8)}</td>
              <td><span className={c.status === 'succes' ? 'pill ok' : c.status === 'bloque' ? 'pill warn' : 'pill bad'}>{c.status}</span></td>
              <td>{c.latency_s}</td>
            </tr>))}
            {!ai.calls.length && <tr><td colSpan="10" className="muted">Aucun appel — l’application a fonctionné en mode dégradé local.</td></tr>}
          </tbody></table>
        <a className="small" href="/api/ai-calls/export?fmt=csv">Exporter tout le journal (CSV)</a>
      </div>
      <div className="grid cols-2">
        <div className="card">
          <h2>Alertes du contrôle d’anonymisation</h2>
          <table><thead><tr><th>Date</th><th>Type</th><th>Détail</th><th>Décision</th></tr></thead>
            <tbody>{alerts.slice(0, 30).map(a => (
              <tr key={a.id}><td className="small">{(a.datetime || '').slice(0, 16)}</td><td>{a.kind}</td>
                <td className="small">{a.detail}</td><td><span className={a.decision === 'en_attente' ? 'pill warn' : 'pill mut'}>{a.decision}</span></td></tr>))}
              {!alerts.length && <tr><td colSpan="4" className="muted">RAS</td></tr>}
            </tbody></table>
        </div>
        <div className="card">
          <h2>Snapshots (rétention {90} j, sauf figeages conservés)</h2>
          <table><thead><tr><th>Date</th><th>Type</th><th>Libellé</th><th /></tr></thead>
            <tbody>{snaps.map(s => (
              <tr key={s.id}><td className="small">{(s.created_at || '').slice(0, 16)}</td><td>{s.kind}</td><td className="small">{s.label}</td>
                <td><button className="ghost" onClick={() => api(`/projects/${pid}/snapshots/${s.id}/restore`, { method: 'POST', body: {} }).then(() => alert('snapshot restauré')).catch(e => alert(e.message))}>Restaurer</button></td></tr>))}
              {!snaps.length && <tr><td colSpan="4" className="muted">—</td></tr>}
            </tbody></table>
          <h3>Incidents</h3>
          {inc.map(x => <div key={x.id} className="small">{(x.datetime || '').slice(0, 16)} — <b>{x.title}</b> {x.detail} {x.closed ? '' : <button className="ghost" onClick={() => api(`/incidents/${x.id}/close`, { method: 'POST', body: {} }).then(() => { })}>clôturer</button>}</div>)}
          {!inc.length && <div className="muted small">Aucun incident enregistré.</div>}
        </div>
      </div>
    </div>
  )
}
