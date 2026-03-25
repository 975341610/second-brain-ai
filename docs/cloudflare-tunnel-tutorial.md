# Cloudflare Tunnel 白嫖与配置保姆级教程

本教程将教你如何使用 Cloudflare Tunnel（以前叫 Argo Tunnel）将本地运行的服务（如 Second Brain AI）安全地发布到公网，无需公网 IP，无需配置路由器端口映射，且完全免费。

## 1. 准备工作
- 一个 Cloudflare 账号。
- 一个已托管在 Cloudflare 上的域名（如果没有，可以去买个便宜的或者用免费域名）。
- 本地正在运行的服务（例如：`http://localhost:8000`）。

## 2. 安装 cloudflared
`cloudflared` 是 Cloudflare Tunnel 的客户端工具。

- **Windows:** 使用 `brew install cloudflared` (如果装了 Homebrew) 或直接从 [GitHub Releases](https://github.com/cloudflare/cloudflared/releases) 下载 exe。
- **macOS:** `brew install cloudflared`
- **Linux:** `curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared && chmod +x cloudflared`

## 3. 身份验证
在终端执行：
```bash
cloudflared tunnel login
```
这会打开浏览器，请选择你要使用的域名进行授权。

## 4. 创建隧道
创建一个名为 `my-brain` 的隧道：
```bash
cloudflared tunnel create my-brain
```
创建成功后，会生成一个 UUID 和一个对应的 `.json` 凭证文件。请记住这个 UUID。

## 5. 配置隧道
在 `cloudflared` 配置文件目录（通常是 `~/.cloudflared/` 或 `%USERPROFILE%\.cloudflared\`）创建 `config.yml`：

```yaml
tunnel: <你的隧道UUID>
credentials-file: /path/to/your/<UUID>.json

ingress:
  - hostname: brain.yourdomain.com
    service: http://localhost:8000
  - service: http_status:404
```

## 6. 配置 DNS 记录
将你的域名指向隧道：
```bash
cloudflared tunnel route dns my-brain brain.yourdomain.com
```
这会在你的 Cloudflare DNS 中创建一个 CNAME 记录。

## 7. 启动隧道
```bash
cloudflared tunnel run my-brain
```
现在，你就可以通过 `https://brain.yourdomain.com` 访问你的本地服务了！

## 8. 进阶：配置为系统服务
为了让隧道在后台常驻：
```bash
# Windows (管理员权限)
cloudflared service install
# Linux
sudo cloudflared service install
```

## 9. 配合 Access Token 认证
由于服务暴露在公网，**强烈建议**开启本项目集成的 Access Token 认证功能：
1. 在 `.env` 中设置 `ACCESS_TOKEN=你的强密码`。
2. 重启后端服务。
3. 访问网页时输入该密码。

这样即使别人知道了你的域名，没有密钥也无法访问你的数据。
