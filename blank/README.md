# blank 站点

仿 Hexo：文章以 GitHub 仓库里的 `articles/articles-data.js` 为唯一数据源。

## 异机同步（无存档码）

1. 后台 → **发布**
2. 仓库填 `catcoder-0/1`，路径 `blank/articles`
3. 填有 `repo` 权限的 GitHub Token → **保存并启用**
4. 之后在后台添加 / 修改 / 删除文章，会自动提交到 GitHub  
5. 另一台电脑打开页面会自动拉取，刷新即可看到

阅读端不需要 Token；只有要发文章的电脑需要填一次 Token。

## 本地预览

```bash
npx --yes serve -l 5173 blank
```
