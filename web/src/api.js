// Client API minimal — mêmes origines (FastAPI sert le build), token en localStorage.
const TOKEN_KEY = 'structai_token'

export function getToken() { return localStorage.getItem(TOKEN_KEY) || '' }
export function setToken(t) { t ? localStorage.setItem(TOKEN_KEY, t) : localStorage.removeItem(TOKEN_KEY) }

export class ApiError extends Error {
  constructor(status, detail) { super(typeof detail === 'string' ? detail : JSON.stringify(detail)); this.status = status; this.detail = detail }
}

export async function api(path, opts = {}) {
  const headers = {}
  const tok = getToken()
  if (tok) headers['X-StructAI-Token'] = tok
  let body = opts.body
  if (body !== undefined && !(body instanceof FormData)) {
    headers['Content-Type'] = 'application/json'
    body = JSON.stringify(body)
  }
  const r = await fetch('/api' + path, { method: opts.method || 'GET', headers, body })
  if (r.status === 401) { throw new ApiError(401, 'session') }
  if (!r.ok) {
    let detail = r.statusText
    try { const j = await r.json(); detail = j.detail ?? j } catch (e) { /* noop */ }
    throw new ApiError(r.status, detail)
  }
  const ct = r.headers.get('content-type') || ''
  return ct.includes('json') ? r.json() : r.blob()
}

export const fileUrl = (pid, rel) =>
  `/api/projects/${pid}/file?path=${encodeURIComponent(rel)}`

export async function pollJob(jid, onTick) {
  // retourne le job fini (ou lance Error)
  for (;;) {
    const j = await api('/jobs/' + jid)
    if (onTick) onTick(j)
    if (j.done) {
      if (j.error) throw new Error(j.error)
      return j
    }
    await new Promise(res => setTimeout(res, 900))
  }
}
