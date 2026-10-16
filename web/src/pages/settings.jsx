import React, { useEffect, useState } from 'react'
import { api } from '../api.js'

// §5.9 / §2.6 : fournisseurs (Anthropic & OpenAI uniquement), clés via
// trousseau, plafonds, mode paranoïaque, ZDR, prompts, mot de passe local,
// documents RGPD/registre.
export default function SettingsPage({ status, refresh }) {
  const [s, setS] = useState(null)
  const [msg, setMsg] = useState('')
  const [err, setErr] = useState('')
  const [prompt, setPrompt] = useState(null)
  const [keys, setKeys] = useState({ anthropic: '', openai: '' })
  const [pwd, setPwd] = useState('')

  useEffect(() => { api('/settings').then(setS).catch(e => setErr(e.message)) }, [])
  const save = async patch => {
    setMsg(''); setErr('')
    try { setS(await api('/settings', { method: 'PUT', body: patch })); setMsg('Enregistré. (Les engagements ZDR/no-training relèvent de vos contrats fournisseurs — vérifiez-les.)'); refresh && refresh() }
    catch (e) { setErr(typeof e.detail === 'string' ? e.detail : e.message) }
  }
  const setKey = async p => {
    if (!keys[p]) return
    try {
      const r = await api('/keys', { method: 'POST', body: { provider: p, api_key: keys[p] } })
      setMsg(`Clé ${p} stockée dans ${r.stockee_dans}${r.avertissement ? ' — ' + r.avertissement : ''}`)
      setKeys(k => ({ ...k, [p]: '' })); refresh && refresh()
    } catch (e) { setErr(e.message) }
  }

  if (!s) return err ? <div className="err">{err}</div> : <div className="muted">chargement…</div>
  const ia = s.ia || {}
  const b = status?.budget || {}
  return (
    <div className="grid cols-2">
      <div className="col">
        <div className="card">
          <h2>Fournisseurs IA — périmètre contractuel</h2>
          <div className="box-warn small">Seuls <b>Claude Opus (Anthropic)</b> et <b>ChatGPT (OpenAI)</b> sont activés par le cahier des charges. Aucun autre fournisseur ne peut être ajouté.</div>
          {['anthropic', 'openai'].map(p => (
            <div key={p} className="row" style={{ marginTop: 8 }}>
              <span className={'light ' + (status?.providers?.[p]?.cle_presente ? 'ok' : 'bad')} />
              <b style={{ width: 90 }}>{p}</b>
              <input type="password" placeholder={status?.providers?.[p]?.cle_presente ? 'clé présente — saisir pour remplacer' : 'coller la clé API (sk-…)'}
                     value={keys[p]} onChange={e => setKeys(k => ({ ...k, [p]: e.target.value }))} style={{ flex: 1 }} />
              <button onClick={() => setKey(p)}>Enregistrer</button>
              <button className="ghost" onClick={() => api(`/keys/${p}`, { method: 'DELETE' }).then(refresh)}>Retirer</button>
            </div>
          ))}
          <div className="muted small">Clés : trousseau système (keyring) — jamais dans le code ni les journaux. Fournisseur absent → mode dégradé 100 % local.</div>
        </div>

        <div className="card">
          <h2>Règles d’appel</h2>
          <div className="row">
            {[['fournisseur_vision', 'Vision'], ['fournisseur_raisonnement', 'Raisonnement'], ['fournisseur_texte', 'Texte']].map(([k, l]) => (
              <label className="f" key={k}>{l}
                <select value={ia[k]} onChange={e => save({ ia: { [k]: e.target.value } })}>
                  <option value="anthropic">Anthropic</option><option value="openai">OpenAI</option>
                </select>
              </label>
            ))}
            <label className="f">Timeout (s)
              <input type="number" value={ia.timeout_s} onChange={e => setS({ ...s, ia: { ...ia, timeout_s: +e.target.value } })} onBlur={() => save({ ia: { timeout_s: ia.timeout_s } })} style={{ width: 80 }} /></label>
          </div>
          <div className="row" style={{ marginTop: 6 }}>
            <label className="f">Plafond jour (USD)<input type="number" step="0.5" value={ia.plafond_usd_jour} onChange={e => setS({ ...s, ia: { ...ia, plafond_usd_jour: +e.target.value } })} onBlur={() => save({ ia: { plafond_usd_jour: ia.plafond_usd_jour } })} style={{ width: 90 }} /></label>
            <label className="f">Plafond / projet (USD)<input type="number" step="0.5" value={ia.plafond_usd_projet} onChange={e => setS({ ...s, ia: { ...ia, plafond_usd_projet: +e.target.value } })} onBlur={() => save({ ia: { plafond_usd_projet: ia.plafond_usd_projet } })} style={{ width: 90 }} /></label>
            <span className="muted small" style={{ marginTop: 18 }}>Déjà dépensé : {b.jour?.usd ?? 0} $ aujourd'hui{b.projet ? ` · ${b.projet.usd} $ pour le projet courant` : ''}</span>
          </div>
          <div className="col small" style={{ marginTop: 8 }}>
            <label><input type="checkbox" checked={!!ia.mode_paranoiaque} onChange={e => save({ ia: { mode_paranoiaque: e.target.checked } })} /> Mode paranoïaque — bloquer TOUT envoi tant qu'aucune confirmation explicite n'a été cochée</label>
            <label><input type="checkbox" checked={!!ia.fallback_fournisseur} onChange={e => save({ ia: { fallback_fournisseur: e.target.checked } })} /> Bascule automatique Anthropic ↔ OpenAI en cas d'échec</label>
            <label><input type="checkbox" checked={!!ia.exiger_zero_retention} onChange={e => save({ ia: { exiger_zero_retention: e.target.checked } })} /> Exiger ZDR + non-training déclarés pour appeler (sinon blocage config)</label>
          </div>
          <div className="row" style={{ marginTop: 6 }}>
            {['anthropic', 'openai'].map(p => (
              <label key={p} className="small">ZDR {p}<input type="checkbox" checked={!!(ia.zero_data_retention || {})[p]}
                onChange={e => save({ ia: { zero_data_retention: { ...(ia.zero_data_retention || {}), [p]: e.target.checked }, no_training: { ...(ia.no_training || {}), [p]: e.target.checked } } })} /></label>
            ))}
          </div>
        </div>
        {msg && <div className="box-ok small">{msg}</div>}
        {err && <div className="box-bad small">{err}</div>}
      </div>

      <div className="col">
        <div className="card">
          <h2>Sécurité locale</h2>
          <div className="row">
            <label className="f" style={{ flex: 1 }}>Mot de passe d'application {status && '(actuel : ' + (s.securite.mot_de_passe_actif ? 'défini' : 'aucun') + ')'}
              <input type="password" placeholder="nouveau mot de passe (vide = retirer)" value={pwd} onChange={e => setPwd(e.target.value)} /></label>
            <button style={{ marginTop: 18 }} onClick={async () => { await api('/settings', { method: 'PUT', body: { securite: { mot_de_passe_nouveau: pwd } } }); setPwd(''); refresh && refresh() }}>Appliquer</button>
          </div>
          <label className="small"><input type="checkbox" checked={!!s.securite.journal_acces_local} onChange={e => save({ securite: { journal_acces_local: e.target.checked } })} /> Journaliser les accès locaux (sessions, exports, lectures sensibles)</label>
          <div className="muted small">Session : expiration après {s.securite.session_expiration_min} min d'inactivité. L'app n'écoute que localhost hors démo.</div>
        </div>
        <div className="card">
          <h2>Prompts (YAML éditables à chaud)</h2>
          <div className="row">{(status?.prompts || []).map(p => (
            <button key={p} className="ghost" onClick={async () => setPrompt(await api('/settings/prompts/' + p.replace(/\.ya?ml$/, '').replace(/^.*\//, '')))}>{p}</button>))}</div>
          {prompt && <><textarea readOnly rows={14} value={prompt.content || JSON.stringify(prompt, null, 1)} /></>}
        </div>
        <div className="card">
          <h2>Documents de conformité</h2>
          <div className="col small">
            <a href="/api/documents/client-consent" download>▸ Modèle d'accord client (anonymisation / DPA résumés)</a>
            <a href="/api/documents/registre" download>▸ Registre simplifié des traitements</a>
            <div className="muted">Procédure incident : onglet Journal → incidents (détection → qualification → mesure corrective → information client si données concernées → clôture datée). L'application ne conserve AUCUNE donnée identifiante en clair (hashs uniquement).</div>
          </div>
        </div>
      </div>
    </div>
  )
}
