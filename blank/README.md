# blank 站点

独立站点目录。页面入口：`blank.html`

## 文章怎么存

| 位置 | 作用 |
|------|------|
| 本机浏览器 `localStorage` | **增删改实际生效的地方** |
| `articles/articles-data.js` | 首次打开时的种子；也可导出后上传到 GitHub |

GitHub Pages 是静态站，浏览器**不能直接改仓库里的 JS**。所以：

1. 后台添加 / 修改 / 删除 → 立刻保存在本机，刷新也还在  
2. 若要更新线上种子文件：存档页点「导出 articles-data.js」，再上传到仓库  
   或填写有写权限的 GitHub Token 后点「推送到 GitHub JS」  
   或「绑定本地 articles 文件夹」后保存会自动写本机文件

「用 GitHub JS 覆盖本机」会用仓库文件盖掉当前浏览器里的文章，请慎用。

## 本地预览

```bash
npx --yes serve -l 5173 blank
```

访问：`http://localhost:5173/blank.html`
