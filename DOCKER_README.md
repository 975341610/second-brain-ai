# SecondBrainAI Docker 部署指南

本项目已支持 Docker 化一键部署。通过 Docker，您可以快速在本地或服务器上运行完整的 SecondBrainAI 环境。

## 前置要求

- 已安装 [Docker](https://www.docker.com/products/docker-desktop)
- 已安装 [Docker Compose](https://docs.docker.com/compose/install/)

## 快速启动

1. **进入项目根目录**：
   ```bash
   cd second-brain-ai
   ```

2. **一键启动服务**：
   使用 Docker Compose 构建并启动前端和后端容器。
   ```bash
   docker-compose up -d --build
   ```

3. **访问应用**：
   - **前端界面**：打开浏览器访问 [http://localhost](http://localhost)
   - **后端 API 文档**：访问 [http://localhost:8000/docs](http://localhost:8000/docs)

## 架构说明

- **Frontend**：使用 Nginx 提供 React 静态资源服务，并作为反向代理将 API 请求转发至后端容器。
- **Backend**：FastAPI 后端服务。
- **持久化**：
  - 数据库文件存储在宿主机的 `./data/second_brain.db`。
  - 向量库文件存储在宿主机的 `./data/chroma_store`。
  - 静态资源映射自 `./backend/assets`。

## 常用命令

- **查看日志**：
  ```bash
  docker-compose logs -f
  ```

- **停止并移除容器**：
  ```bash
  docker-compose down
  ```

- **重启服务**：
  ```bash
  docker-compose restart
  ```

- **更新依赖后重新构建**：
  ```bash
  docker-compose up -d --build
  ```
