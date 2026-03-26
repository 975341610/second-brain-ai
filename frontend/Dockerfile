# 第一阶段：构建前端
FROM node:20-alpine AS build

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装依赖项
COPY package*.json ./
RUN npm install

# 复制项目代码并构建
COPY . .
RUN npm run build

# 第二阶段：服务静态文件
FROM nginx:alpine

# 从构建阶段复制打包后的文件
COPY --from=build /app/dist /usr/share/nginx/html

# 复制 Nginx 配置文件
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 暴露端口 80
EXPOSE 80

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]
