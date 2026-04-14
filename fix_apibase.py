import re

with open("nova_repo/nova-block/src/lib/api.ts", "r") as f:
    content = f.read()

# add aime-app.bytedance.net to the proxy check
old_base = """export const getApiBase = () => {
  if (import.meta.env.VITE_API_BASE_URL) return import.meta.env.VITE_API_BASE_URL;
  if (typeof window !== 'undefined' && window.location.hostname.includes('strato-https-proxy')) {
    // 将前端 vite 预览的端口替换为后端 8765 端口
    return `https://${window.location.hostname.replace(/^[0-9]+-/, '8765-')}/api`;
  }
  return 'http://127.0.0.1:8765/api';
};"""

new_base = """export const getApiBase = () => {
  if (import.meta.env.VITE_API_BASE_URL) return import.meta.env.VITE_API_BASE_URL;
  if (typeof window !== 'undefined') {
    if (window.location.hostname.includes('strato-https-proxy')) {
      return `https://${window.location.hostname.replace(/^[0-9]+-/, '8765-')}/api`;
    }
    if (window.location.hostname.includes('aime-app.bytedance.net')) {
      // 代理 AIME App 端口 (假设前端挂在 8bfdd3c16844 这个 app_id 上，后端通过 /api 分发，或者前端请求当前域名)
      // 如果前后端挂在同一个域名下，则使用当前 host
      return `https://${window.location.hostname}/api`;
    }
  }
  
  // 对于生产构建出来的 static HTML (file:// 或 localhost)，或者开发模式，通常使用当前 host 即可
  if (typeof window !== 'undefined' && window.location.protocol === 'http:' && !window.location.hostname.includes('localhost') && window.location.hostname !== '127.0.0.1') {
      return `http://${window.location.hostname}:8765/api`;
  }
  
  // 最终 fallback，如果前端是 SPA，并且没有走 Vite dev server，最好就是当前域名 + 端口或者同源的 /api
  // 因为现在把静态文件打包放在后端 8765 上起了，所以直接走 /api 最保险
  return '/api';
};"""

content = content.replace(old_base, new_base)

with open("nova_repo/nova-block/src/lib/api.ts", "w") as f:
    f.write(content)
