import React, { useEffect, useState } from 'react'
import { api } from '../api.js'
import { nav } from '../app.jsx'
import PlansPage from './plans.jsx'
import ValidatePage from './validate.jsx'
import GenPage from './gen.jsx'
import EditorPage from './editor.jsx'
import DelivPage from './deliv.jsx'
import LogsPage from './logs.jsx'
import NewProjectForm from './newproject.jsx'

const TABS = [
  ['etapes', '1 · Étapes'], ['plans', '2 · Import & parsing'], ['validate', '3 · Interprétation & validation'],
  ['generate', '4 · Génération & comparateur'], ['editor', '5 · Éditeur'], ['deliverables', '6 · Livrables'],
  ['logs', '7 · Journal']
]

export default function Project({ pid, tab, newProject, refresh }) {
  const [p, setP] = useState(null)
  const [oid, setOid] = useState('')
  useEffect(() => { if (pid) api('/projects/' + pid).then(setP).catch(e => setP({ error: e.message })) }, [pid, tab])
  if (newProject) return <NewProjectForm onDone={id => nav('project/' + id + '/plans')} />
  if (!p) return <div className="muted">chargement…</div>
  if (p.error) return <div className="err">{p.error}</div>
  const steps = p.steps || {}
  const order = ['import', 'parsing', 'interpretation', 'interpretation_validee', 'generation', 'option_retenue', 'livrables']
  return (
    <div className="col">
      <div className="card" style={{ paddingBottom: 8 }}>
        <div className="row" style={{ justifyContent: 'space-between' }}>
          <h1 style={{ margin: 0 }}>{p.name} <span className="pill mut">{p.status}</span>
            {!p.client_agreement && <span className="pill warn" title="Le document d'information client (modèle en Paramètres) doit être signé avant envoi de données à l'IA">accord client : non enregistré</span>}
          </h1>
          <div className="row small">
            <button className="ghost" onClick={() => nav('settings')}>Modèle d'accord client</button>
            <button className="ghost" onClick={async () => {
              if (window.confirm('Dupliquer ce projet (sans les livrables) ?')) {
                const r = await api(`/projects/${pid}/duplicate`, { method: 'POST', body: {} }); nav('project/' + r.id + '/plans')
              }
            }}>Dupliquer</button>
            <button className="danger" onClick={async () => {
              const n = window.prompt(`Suppression DÉFINITIVE — saisissez le nom exact du projet (« ${p.name} ») :`)
              if (!n) return
              try { await api('/projects/' + pid + '?confirm_name=' + encodeURIComponent(n), { method: 'DELETE' }); nav('') }
              catch (e) { alert(typeof e.detail === 'string' ? e.detail : e.message) }
            }}>Supprimer…</button>
          </div>
        </div>
        <div className="row small" style={{ marginTop: 4 }}>
          <span className="muted">{p.ref || 'sans réf.'} · maj {(p.updated_at || '').slice(0, 16)}</span>
          <span className="row" style={{ marginLeft: 'auto' }}>
            {order.map(k => <span key={k} className={steps[k] ? 'pill ok' : 'pill mut'} style={{ marginRight: 3 }}>{k}</span>)}
          </span>
        </div>
        <div className="tabs">
          {TABS.map(([k, l]) => (
            <button key={k} className={tab === k ? 'on' : ''} onClick={() => nav(`project/${pid}/${k}`)}>{l}</button>
          ))}
        </div>
      </div>

      {tab === 'etapes' && <Steps p={p} />}
      {tab === 'plans' && <PlansPage pid={pid} refresh={refresh} />}
      {tab === 'validate' && <ValidatePage pid={pid} refresh={refresh} />}
      {tab === 'generate' && <GenPage pid={pid} refresh={refresh} />}
      {tab === 'editor' && <EditorPage pid={pid} optionId={oid} setOptionId={setOid} />}
      {tab === 'deliverables' && <DelivPage pid={pid} />}
      {tab === 'logs' && <LogsPage pid={pid} />}
    </div>
  )
}

function Steps({ p }) {
  const [form, setForm] = useState({ comment: p.comment || '' })
  const [ok, setOk] = useState('')
  const rows = [
    ['Import d’un plan DXF (copie + hash)', 'plans', 'import'],
    ['Parsing & rendu local, contrôle d’anonymisation', 'plans', 'parsing'],
    ['Interprétation (IA de vision ou saisie manuelle)', 'validate', 'interpretation'],
    ['Correction puis VALIDATION humaine obligatoire', 'validate', 'interpretation_validee'],
    ['Génération de 3–5 options conformes (calculs complets)', 'generate', 'generation'],
    ['Comparateur puis « Retenir »', 'generate', 'option_retenue'],
    ['Éditions justifiées puis figeage (optionnel)', 'editor', null],
    ['Livrables DXF/PDF/CSV + traçabilité', 'deliverables', 'livrables'],
  ]
  return (
    <div className="grid cols-2">
      <div className="card">
        <h2>Avancement — pipeline à 10 phases (5 points de contrôle humains)</h2>
        {rows.map(([l, t, k], i) => (
          <div key={i} className="row" style={{ padding: '4px 0', borderBottom: '1px solid var(--line)' }}>
            <span className={k ? (p.steps?.[k] ? 'pill ok' : 'pill warn') : 'pill mut'}>{k ? (p.steps[k] ? 'fait' : 'à faire') : 'libre'}</span>
            <a href={`#/project/${p.id}/${t}`} style={{ flex: 1 }}>{i + 1}. {l}</a>
          </div>
        ))}
      </div>
      <div className="card">
        <h2>Identité & notes</h2>
        <div className="small muted">
          <b>Projet :</b> {p.name}<br />
          <b>Typologie :</b> {p.params?.type_batiment || '—'} · niveaux {p.params?.niveaux || '—'} · h={p.params?.hauteur_etage || '—'} m · usage {p.params?.usage || '—'}<br />
          <b>Localisation :</b> {p.params?.commune || '—'} (jamais transmise à l'IA) · sismicité zone {p.params?.zone_sismique ?? '—'} · neige {p.params?.zone_neige || '—'} · vent {p.params?.zone_vent ?? '—'} · alt. {p.params?.altitude ?? '—'} m<br />
          <b>Normes :</b> {Object.entries(p.params?.normes || { EC0: 1, EC1: 1, EC2: 1, EC8: 1 }).filter(([, v]) => v).map(([k]) => k).join(' · ') || 'EC2/EC8 par défaut'}<br />
          <b>Matériaux :</b> {(p.params?.materiaux || ['béton armé']).join(', ')} · {p.params?.classe_exposition || 'XC1'} · {p.params?.duree_utilisation || 50} ans · importance {p.params?.categorie_importance || 'II'}
        </div>
        <label className="f">Commentaire interne
          <textarea rows={3} value={form.comment} onChange={e => setForm({ ...form, comment: e.target.value })} /></label>
        <div className="row end">
          <button className="ghost" onClick={() => setForm({ comment: '' })}>Annuler</button>
          <button onClick={async () => { await api('/projects/' + p.id, { method: 'PUT', body: { comment: form.comment } }); setOk('enregistré') }}>Enregistrer</button>
        </div>
        {ok && <div className="small box-ok">{ok}</div>}
        <label className="small" style={{ marginTop: 8 }}>
          <input type="checkbox" checked={!!p.client_agreement} onChange={async e => {
            await api('/projects/' + p.id, { method: 'PUT', body: { client_agreement: e.target.checked ? 1 : 0 } })
            const np = await api('/projects/' + p.id); location.hash = location.hash
          }} /> Accord client concernant l’usage de l’IA enregistré (case à cocher après signature du modèle — §5.7.2)
        </label>
      </div>
    </div>
  )
}
