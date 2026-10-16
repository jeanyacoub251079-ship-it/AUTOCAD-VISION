import React, { useEffect, useRef, useState } from 'react'
import { api, pollJob } from '../api.js'

// Démarre un job backend (POST retourne {job}) puis suit sa progression.
export function useJob() {
  const [job, setJob] = useState(null)
  const [error, setError] = useState('')
  const [running, setRunning] = useState(false)
  const jidRef = useRef(null)

  const run = async (path, body) => {
    setError(''); setRunning(true); setJob(null)
    try {
      const r = await api(path, { method: 'POST', body })
      jidRef.current = r.job
      const done = await pollJob(r.job, j => setJob(j))
      setJob(done)
      setRunning(false)
      return done.result
    } catch (e) {
      setError(e.message || String(e)); setRunning(false); throw e
    }
  }
  const cancel = () => jidRef.current && api(`/jobs/${jidRef.current}/cancel`, { method: 'POST', body: {} })
  return { job, error, running, run, cancel }
}

export function JobProgress({ job, running, onCancel }) {
  if (!job && !running) return null
  const pct = job?.progress ?? 0
  return (
    <div className="col">
      <div className="row" style={{ justifyContent: 'space-between' }}>
        <span className="small muted">
          {job?.stage || 'démarrage…'} — {pct}% {job?.done ? (job.error ? '(erreur)' : '(terminé)') : ''}
        </span>
        {!job?.done && onCancel && <button className="ghost" onClick={onCancel}>Annuler</button>}
      </div>
      <div className="progress"><i style={{ width: pct + '%' }} /></div>
      {job?.log?.length > 0 && (
        <div className="joblog">
          {job.log.slice(-14).map((l, i) => <div key={i}>[{(l.t || '').slice(11, 19)}] {l.stage}: {l.msg}</div>)}
        </div>
      )}
    </div>
  )
}
