# Perxio 派研

增长活动调研助手的前端交互原型。当前网站基于 2026-08-25 的 V05，包含工作台、活动项目、问卷与投放、数据处理、洞察报告、竞品基准和组织设置。

## 本地预览

不需要安装 npm 依赖。运行：

```sh
python3 scripts/build.py
python3 -m http.server 8080 --directory _site
```

打开 <http://localhost:8080>。

## 在线预览

源码仓库：[Jean0708/perxio](https://github.com/Jean0708/perxio)。

在 GitHub 的 **Settings → Pages → Source** 选择 **Deploy from a branch**，
分支选择 **main**，目录选择 **/docs**，点击 **Save**。
设置成功后，`main` 分支中的 `docs` 每次推送更新会自动重新部署。
预览地址：<https://jean0708.github.io/perxio/>（首次部署成功后可用）。

GitHub Free 的 Pages 适用于公开仓库；私有仓库需要支持 Pages 的付费套餐。Pages 网站默认公开，即使源仓库是私有的。

## 更新与同步

`index.html` 是后续修改的唯一网站入口；`04_最终输出` 中的 V05 是保留的历史原件。

完成修改后：

```sh
python3 scripts/build.py
git add index.html docs
git commit -m "Update Perxio prototype"
git push origin main
```

Git 跟踪版本；本地修改需要提交和推送后才会更新在线预览。

## 文件结构

- `index.html`：当前网站源码。
- `docs/`：GitHub Pages 发布目录，由构建脚本生成。
- `scripts/build.py`：检查 HTML 并生成预览发布目录。
- `01_项目说明`：整理及同步说明。
- `02_参考资料`：V04 历史参考。
- `03_过程文件`：过程记录、QA 截图与对比页。
- `04_最终输出`：V05 HTML 原件。
- `05_归档文件`：重复的 QA 文档和对比图。

`docs` 发布目录只包含 `index.html` 和 `.nojekyll`，文档、截图和历史版本保存在源码仓库中。
GitHub Actions 配置参考保存在 `01_项目说明`，当前采用分支发布，无需自定义 workflow 权限。

## 原型范围

页面使用演示数据，交互不包含真实后端、数据持久化、文件上传、AI 服务或报告导出。问卷发布与复制链接等操作为演示反馈。
