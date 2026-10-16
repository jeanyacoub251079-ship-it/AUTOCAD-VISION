import React, { useState } from 'react'
import { api, setToken } from '../api.js'

export default function Login({ onDone }) {
  const [pwd, setPwd] = useState('')
  const [err, setErr] = useState('')
  const [busy, setBusy] = useState(false)
  const submit = async (e) => {
    e.preventDefault(); setBusy(true); setErr('')
    try {
      const r = await api('/session/login', { method: 'POST', body: { password: pwd } })
      setToken(r.token || '')
      onDone()
    } catch (x) { setErr(x.message || 'échec') } finally { setBusy(false) }
  }
  return (
    <div className="login card">
      <h1>StructAI — accès local</h1>
      <p className="muted">Une session est ouverte pour 30 min d'inactivité.</p>
      <form onSubmit={submit} className="col">
        <input type="password" autoFocus placeholder="Mot de passe local"
               value={pwd} onChange={e => setPwd(e.target.value)} />
        <button disabled={busy}>{busy ? '…' : 'Entrer'}</button>
        {err && <div className="err">{err}</div>}
      </form>
    </div>
  )
}
