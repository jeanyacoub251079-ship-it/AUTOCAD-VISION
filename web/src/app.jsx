import React, { useEffect, useState } from 'react'
import { api } from './api.js'
import Dashboard from './pages/dashboard.jsx'
import Project from './pages/project.jsx'
import Settings from './pages/settings.jsx'
import Login from './pages/login.jsx'

export function nav(path) { window.location.hash = '#/' + path }

function useRoute() {
  const parse = () => (window.location.hash || '#/').slice(2)
  const [route, setRoute] = useState(parse)
  useEffect(() => {
    const f = () => setRoute(parse())
    window.addEventListener('hashchange', f)
    return () => window.removeEventListener('hashchange', f)
  }, [])
  return route.split('/')
}

export default function App() {
  const [status, setStatus] = useState(null)
  const [auth, setAuth] = useState({ required: false, ok: true })
  const parts = useRoute()

  const refresh = async () => {
    try {
      const s = await api('/status')
      setStatus(s)
      setAuth(a => ({ ...a, ok: true }))
    } catch (e) {
      if (e.status === 401) setAuth({ required: true, ok: false })
    }
  }
  useEffect(() => { refresh(); const t = setInterval(refresh, 30000); return () => clearInterval(t) }, [])

  if (!auth.ok) return <Login onDone={() => { setAuth({ required: false, ok: true }); refresh() }} />

  let page = <Dashboard status={status} />
  if (parts[0] === 'settings') page = <Settings status={status} refresh={refresh} />
  else if (parts[0] === 'new') page = <Project newProject refresh={refresh} />
  else if (parts[0] === 'project' && parts[1]) page = <Project pid={parts[1]} tab={parts[2] || 'etapes'} refresh={refresh} />

  return (
    <>
      <header className="topbar">
        <span className="brand">StructAI</span>
        <nav>
          <a href="#/" className={parts[0] === 'project' || parts[0] === 'new' ? '' : 'on'}>Projets</a>
          <a href="#/settings" className={parts[0] === 'settings' ? 'on' : ''}>Paramètres</a>
          <a href="https://localhost:8000/api/docs" target="_blank" rel="noreferrer">API</a>
        </nav>
        <div className="lights">
          {status && ['anthropic', 'openai'].map(p => (
            <span key={p} title={status.providers[p]?.label + (status.providers[p]?.cle_presente ? ' — clé présente' : ' — clé absente (mode dégradé local)')}>
              <i className={'light ' + (status.providers[p]?.cle_presente ? 'ok' : 'bad')} /> {p}
            </span>
          ))}
          <span title="hors-ligne sauf appels IA">● local</span>
          {status?.mode_paranoiaque && <span className="pill warn" style={{ color: '#ffd98a', borderColor: '#ffd98a' }}>parano</span>}
        </div>
      </header>
      <main>{page}</main>
    </>
  )
}
