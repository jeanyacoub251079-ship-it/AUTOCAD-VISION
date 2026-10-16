import React, { useState } from 'react'
import { api } from '../api.js'

// Étape 2 du cahier des charges : formulaire d'identité du projet (sections A–G).
// Adresse/commune restent LOCALES — jamais envoyées à l'IA.
export default function NewProjectForm({ onDone }) {
  const [f, setF] = useState({
    name: '', ref: '',
    commune: '', adresse: '', altitude: 50,
    zone_sismique: 3, zone_neige: 'C1', zone_vent: 3, classe_sol: 'AB', qsol: 250,
    type_batiment: 'R+2', niveaux: 3, hauteur_etage: 2.8, usage: 'habitation', sous_sol: false,
    materiaux: ['beton_arme'],
    normes: { EC0: true, EC1: true, EC2: true, EC8: true, AN_FR: true, EC3: false, EC6: false, EC7: false },
    classe_exposition: 'XC1', duree_utilisation: 50, categorie_importance: 'II', q_comportement: 3.0,
    nb_options: 5, critere_classement: 'simplicite_mise_en_oeuvre', seed: Math.floor(Math.random() * 1e6),
    notes: ''
  })
  const [err, setErr] = useState('')
  const set = (k, v) => setF(x => ({ ...x, [k]: v }))
  const submit = async () => {
    setErr('')
    if (!f.name.trim()) { setErr('Le nom du projet est obligatoire.'); return }
    try {
      const r = await api('/projects', { method: 'POST', body: { name: f.name, ref: f.ref, params: f } })
      onDone(r.id)
    } catch (e) { setErr(e.message) }
  }
  return (
    <div className="card" style={{ maxWidth: 980, margin: '0 auto' }}>
      <h1>Nouveau projet</h1>
      <div className="grid cols-2">
        <div className="col">
          <div className="row">
            <label className="f" style={{ flex: 1 }}>A · Nom du projet *<input value={f.name} onChange={e => set('name', e.target.value)} placeholder="ex: Maison Durand R+2" /></label>
            <label className="f" style={{ flex: 1 }}>Référence interne<input value={f.ref} onChange={e => set('ref', e.target.value)} /></label>
          </div>
          <div className="box-warn small">B · Localisation — ces champs restent 100 % locaux : l’adresse ne sera JAMAIS transmise à l’IA (seules les zones normatives en sont déduites).</div>
          <div className="row">
            <label className="f" style={{ flex: 1 }}>Commune<input value={f.commune} onChange={e => set('commune', e.target.value)} /></label>
            <label className="f" style={{ flex: 1 }}>Adresse (locale, non envoyée)<input value={f.adresse} onChange={e => set('adresse', e.target.value)} /></label>
            <label className="f">Altitude (m)<input type="number" value={f.altitude} onChange={e => set('altitude', +e.target.value)} style={{ width: 90 }} /></label>
          </div>
          <div className="row">
            <label className="f">Zone sismique (1–5)<select value={f.zone_sismique} onChange={e => set('zone_sismique', +e.target.value)}>{[1, 2, 3, 4, 5].map(z => <option key={z}>{z}</option>)}</select></label>
            <label className="f">Zone de neige<select value={f.zone_neige} onChange={e => set('zone_neige', e.target.value)}>{['A1', 'A2', 'B', 'C1', 'C2', 'D', 'E'].map(z => <option key={z}>{z}</option>)}</select></label>
            <label className="f">Zone de vent (1–5)<select value={f.zone_vent} onChange={e => set('zone_vent', +e.target.value)}>{[1, 2, 3, 4, 5].map(z => <option key={z}>{z}</option>)}</select></label>
            <label className="f">Classe de sol<select value={f.classe_sol} onChange={e => set('classe_sol', e.target.value)}>{['A', 'B', 'AB', 'C', 'D', 'E'].map(z => <option key={z}>{z}</option>)}</select></label>
            <label className="f">q_sol (kPa)<input type="number" value={f.qsol} onChange={e => set('qsol', +e.target.value)} style={{ width: 80 }} /></label>
          </div>
          <div className="row">
            <label className="f">C · Typologie<select value={f.type_batiment} onChange={e => set('type_batiment', e.target.value)}>{['RDC', 'R+1', 'R+2', 'R+3', 'R+4', 'R+5'].map(t => <option key={t}>{t}</option>)}</select></label>
            <label className="f">Niveaux<input type="number" min="1" max="8" value={f.niveaux} onChange={e => set('niveaux', +e.target.value)} style={{ width: 70 }} /></label>
            <label className="f">Hauteur d’étage (m)<input type="number" step="0.05" value={f.hauteur_etage} onChange={e => set('hauteur_etage', +e.target.value)} style={{ width: 80 }} /></label>
            <label className="f">Usage<select value={f.usage} onChange={e => set('usage', e.target.value)}>{['habitation', 'bureau', 'commercial', 'parking', 'stockage'].map(u => <option key={u}>{u}</option>)}</select></label>
            <label className="small" style={{ marginTop: 20 }}><input type="checkbox" checked={f.sous_sol} onChange={e => set('sous_sol', e.target.checked)} /> Sous-sol</label>
          </div>
          <div className="row">
            <label className="small"><input type="checkbox" checked={f.materiaux.includes('beton_arme')} onChange={e => set('materiaux', e.target.checked ? [...f.materiaux, 'beton_arme'] : f.materiaux.filter(m => m !== 'beton_arme'))} /> Béton armé</label>
            <span className="muted small">(Lot 1 : BA uniquement — charpente métallique/batis bois : non disponible)</span>
          </div>
        </div>
        <div className="col">
          <h3>D · Normes applicables</h3>
          <div className="row small">
            {Object.keys(f.normes).map(k => (
              <label key={k}><input type="checkbox" checked={f.normes[k]} onChange={e => set('normes', { ...f.normes, [k]: e.target.checked })} /> Eurocode {k.replace('AN_FR', 'FR (Annexes Nat. FR)').replace('EC', '')}{k === 'AN_FR' ? 'Annexes FR' : ''}</label>
            ))}
          </div>
          <h3>E · Paramètres de calcul</h3>
          <div className="row">
            <label className="f">Classe d’exposition<select value={f.classe_exposition} onChange={e => set('classe_exposition', e.target.value)}>{['XC1', 'XC2', 'XC3', 'XC4', 'XD1', 'XS1'].map(c => <option key={c}>{c}</option>)}</select></label>
            <label className="f">Durée de service (ans)<input type="number" value={f.duree_utilisation} onChange={e => set('duree_utilisation', +e.target.value)} style={{ width: 70 }} /></label>
            <label className="f">Cat. importance<select value={f.categorie_importance} onChange={e => set('categorie_importance', e.target.value)}>{['I', 'II', 'III', 'IV'].map(c => <option key={c}>{c}</option>)}</select></label>
            <label className="f">Facteur de comportement q<input type="number" step="0.1" value={f.q_comportement} onChange={e => set('q_comportement', +e.target.value)} style={{ width: 70 }} /></label>
          </div>
          <h3>F–G · Génération</h3>
          <div className="row">
            <label className="f">Nombre d’options visé<select value={f.nb_options} onChange={e => set('nb_options', +e.target.value)}>{[3, 4, 5].map(n => <option key={n}>{n}</option>)}</select></label>
            <label className="f">Critère de classement
              <select value={f.critere_classement} onChange={e => set('critere_classement', e.target.value)}>
                <option value="simplicite_mise_en_oeuvre">Simplicité de mise en œuvre</option>
                <option value="masse_acier">Économie d’acier</option>
                <option value="volume_beton">Économie de béton</option>
                <option value="performance_sismique">Performance sismique</option>
                <option value="marge_structurelle">Marge structurelle</option>
              </select></label>
            <label className="f">Seed<input type="number" value={f.seed} onChange={e => set('seed', +e.target.value)} style={{ width: 110 }} /></label>
          </div>
          <label className="f">Notes internes<input value={f.notes} onChange={e => set('notes', e.target.value)} /></label>
        </div>
      </div>
      <div className="row end" style={{ marginTop: 12 }}>
        <button className="ghost">Annuler</button>
        <button onClick={submit}>Créer le projet</button>
      </div>
      {err && <div className="err">{err}</div>}
    </div>
  )
}
