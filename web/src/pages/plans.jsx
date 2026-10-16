import React, { useEffect, useRef, useState } from 'react'
import { api, fileUrl } from '../api.js'

// Phase 3-4 : import DXF + parsing local + contrôle d'anonymisation à l'import.
export default function PlansPage({ pid, refresh }) {
  const [plans, setPlans] = useState([])
  const [sel, setSel] = useState(null)
  const [parseRes, setParseRes] = useState(null)
  const [excl, setExcl] = useState([])
  const [busy, setBusy] = useState(false)
  const [err, setErr] = useState('')
  const [okMsg, setOkMsg] = useState('')
  const [preview, setPreview] = useState(null)
  const fileRef = useRef(null)

  const load = () => api(`/projects/${pid}/plans`).then(r => setPlans(r.plans || [])).catch(e => setErr(e.message))
  useEffect(() => { load(); api(`/projects/${pid}/alerts`).then(a => setSel(s => s)).catch(() => {}) }, [pid])

  const upload = async f => {
    if (!f) return
    setBusy(true); setErr('')
    const fd = new FormData(); fd.append('file', f)
    try {
      await api(`/projects/${pid}/plans`, { method: 'POST', body: fd })
      await load()
      setOkMsg(`« ${f.name} » importé (copie horodatée + SHA-256 conservés).`)
    } catch (e) { setErr(e.message) } finally { setBusy(false) }
  }

  const doParse = async () => {
    setBusy(true); setErr('')
    try {
      const r = await api(`/projects/${pid}/plans/${sel}/parse`, { method: 'POST', body: { exclude_layers: excl } })
      setParseRes(r)
      setExcl(r.layers.filter(l => l.exclure).map(l => l.nom))
      load()
    } catch (e) { setErr(typeof e.detail === 'string' ? e.detail : e.message) } finally { setBusy(false) }
  }
  const rerender = async () => {
    setBusy(true)
    try { await api(`/projects/${pid}/plans/${sel}/render`, { method: 'POST', body: { exclude_layers: excl, clean: true } }); await load() }
    catch (e) { setErr(e.message) } finally { setBusy(false) }
  }
  const confirm = async decision => {
    try { await api(`/projects/${pid}/plans/${sel}/confirm-anonymization`, { method: 'POST', body: { decision } }); refresh && refresh(); load() }
    catch (e) { setErr(e.message) }
  }
  const previewPayload = async () => {
    try { setPreview(await api(`/projects/${pid}/plans/${sel}/preview-payload`)) }
    catch (e) { setErr(e.message) }
  }

  const alerts = parseRes?.alerts || []
  return (
    <div className="grid cols-2">
      <div className="col">
        <div className="card">
          <h2>Importer un plan (DXF)</h2>
          <div className="box-warn small">Rappel : l'anonymisation est faite AVANT import par vos soins — l'application ne fait qu'un contrôle de cohérence (filet de sécurité, non bloquant hors mode strict).</div>
          <div
            onDragOver={e => e.preventDefault()}
            onDrop={e => { e.preventDefault(); upload(e.dataTransfer.files[0]) }}
            onClick={() => fileRef.current.click()}
            style={{ border: '2px dashed var(--line)', borderRadius: 8, padding: 22, textAlign: 'center', cursor: 'pointer' }}>
            {busy ? 'traitement…' : 'Glissez ici un fichier .dxf (R12→R2018, ≤ 100 Mo) ou cliquez pour choisir.'}
            <input ref={fileRef} type="file" accept=".dxf" hidden onChange={e => upload(e.target.files[0])} />
          </div>
          {okMsg && <div className="box-ok small">{okMsg}</div>}
          <table>
            <thead><tr><th>Fichier</th><th>Taille</th><th>Version</th><th>Entités</th><th>Hash</th><th /></tr></thead>
            <tbody>
              {plans.map(p => (
                <tr key={p.id} className="clickable" onClick={() => { setSel(p.id); setParseRes(null) }}
                    style={{ background: sel === p.id ? '#eaf4fa' : undefined }}>
                  <td>{p.filename}<div className="muted small">{(p.imported_at || '').slice(0, 16)} · anonymisation {p.anonymization_ok ? 'confirmée' : 'à confirmer'}</div></td>
                  <td>{(p.size / 1e6).toFixed(1)} Mo</td><td>{p.dxf_version}</td>
                  <td>{p.entities_count || '—'}</td><td className="small muted">{(p.sha256 || '').slice(0, 10)}…</td>
                  <td>{p.png_clean ? <a href={fileUrl(pid, p.png_clean)} target="_blank" rel="noreferrer" onClick={e => e.stopPropagation()}>rendu</a> : '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {sel && (
          <div className="card">
            <h2>Parsing local</h2>
            <div className="row">
              <button onClick={doParse} disabled={busy}>Parser / re-parser</button>
              {parseRes && <button className="ghost" onClick={rerender} disabled={busy}>Re-rendre l’image nettoyée</button>}
              {parseRes && <button className="ghost" onClick={previewPayload}>Aperçu de ce qui sera envoyé à l’IA</button>}
            </div>
            {err && <div className="err">{err}</div>}
            {parseRes && (
              <>
                <div className="kpi small" style={{ marginTop: 8 }}>
                  <div><b>{parseRes.entities}</b>entités</div>
                  <div><b>{parseRes.units}</b>{parseRes.unites_note}</div>
                  <div><b>{parseRes.bbox ? `${(parseRes.bbox[1][0] - parseRes.bbox[0][0]).toFixed(1)}×${(parseRes.bbox[1][1] - parseRes.bbox[0][1]).toFixed(1)} m` : '—'}</b>emprise (unités dxf)</div>
                </div>
                {(parseRes.warnings || []).map((w, i) => <div key={i} className="box-warn small">{w}</div>)}
                <h3>Calques (décochez ce qui doit être exclu du rendu IA)</h3>
                <div className="row small">
                  {parseRes.layers.map(l => (
                    <label key={l.nom}>
                      <input type="checkbox" checked={excl.includes(l.nom)}
                             onChange={e => setExcl(x => e.target.checked ? [...x, l.nom] : x.filter(n => n !== l.nom))} />
                      {' '}{l.nom} ({l.nb})
                    </label>
                  ))}
                </div>
                {alerts.length > 0 ? (
                  <div className="box-bad">
                    <b>Contrôle d’anonymisation — {alerts.length} alerte(s) non bloquante(s)</b>
                    <ul className="small">{alerts.map((a, i) => <li key={i}>{a.type} : {a.message}</li>)}</ul>
                    <div className="row end">
                      <button className="ghost" onClick={() => confirm('ignoree')}>J’ai vérifié — ignorer</button>
                      <button onClick={() => confirm('corrigee')}>Corrections faites</button>
                    </div>
                  </div>
                ) : <div className="box-ok small">Aucun indice de données identifiantes détecté à l’import.</div>}
                {preview && (
                  <div className="box-warn small">
                    <b>Aperçu envoi IA</b> — image : {preview.image} ({preview.hash_image}), {preview.nb_textes} texte(s) encore lisible(s) : {preview.textes_detectes.slice(0, 5).join(' / ') || 'aucun'}<br />
                    Fournisseur {preview.provider} / {preview.model} — coût estimé {preview.estimation?.cout_estime_usd?.toFixed(3)} USD.
                    <div className="muted">{preview.avertissement}</div>
                  </div>
                )}
              </>
            )}
          </div>
        )}
      </div>
      <div className="card">
        <h2>Rendu</h2>
        {sel && parseRes ? (
          <>
            <img style={{ width: '100%', border: '1px solid var(--line)', borderRadius: 6 }}
                 src={fileUrl(pid, parseRes.png_clean)} alt="plan nettoyé" />
            <div className="muted small">Version NETTOYÉE envoyée à l’IA (annotations/cartouche exclus). L’original reste consultable :</div>
            <a className="small" href={fileUrl(pid, parseRes.png_original)} target="_blank" rel="noreferrer">voir l’original complet</a>
          </>
        ) : <div className="muted">Sélectionnez un plan puis relancez le parsing.</div>}
      </div>
    </div>
  )
}
