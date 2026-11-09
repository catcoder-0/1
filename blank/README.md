# blank 站点

独立站点目录。页面入口：`blank.html`

## 文章（只用 JS）

唯一数据源：`articles/articles-data.js`

```js
window.__BLANK_ARTICLES = [
  {
    "id": "a-opening",
    "category": "随笔",
    "date": "2026.10.04",
    "title": "开篇",
    "body": "正文…"
  }
];
```

页面启动会：
1. 读取本地 `articles-data.js`
2. 再尝试从 GitHub 同路径拉取覆盖

默认 GitHub 路径：`catcoder-0/1` → `blank/articles/articles-data.js`

### 后台自动改 JS

1. 「后台管理 → 存档」配置仓库 / 分支 / 路径
2. 填 GitHub Token（写权限）或「绑定本地 articles 文件夹」
3. 添加 / 修改 / 删除文章后，会自动改写 `articles-data.js`

没有 Token / 未绑定文件夹时，会下载更新后的 `articles-data.js`。

### 规范化（可选）

```bash
python crawl-articles.py
```

## 本地预览

```bash
npx --yes serve -l 5173 blank
```

访问：`http://localhost:5173/blank.html`
