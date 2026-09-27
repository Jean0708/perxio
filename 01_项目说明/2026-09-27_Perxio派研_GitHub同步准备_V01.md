# GitHub 同步准备 V01

日期：2026-09-27

## 文件整理结果

- 使用：2026-08-25 的 V05 HTML 与现有 QA、过程记录。
- 参考：V04 HTML 移至 `02_参考资料`。
- 过程：记录、截图和对比 HTML 移至 `03_过程文件`；对比页引用的图片仍在同目录。
- 最终原件：V05 HTML 移至 `04_最终输出`；正式 QA 对比图保存在 `03_过程文件`。
- 归档：重复 QA 文档与重复对比图移至 `05_归档文件`。
- 无主版本冲突，未删除或覆盖原始文件。

## 新增与修改

- 新增网站入口 `index.html`，基于 V05 原件；仅补充内嵌浏览器图标。
- 新增 `README.md`、`.gitignore`、`scripts/build.py`、GitHub Pages 发布目录 `docs` 及本说明。
- 初始化本地 Git，使用 `main` 分支。
- 构建目录 `_site` 不进入 Git；部署产物只包含网页和 `.nojekyll`。
- 后续更新以根目录 `index.html` 为准，V05 原件作为历史版本保留。

## 已执行验证

- `python3 scripts/build.py`：通过，检查完整页面标记与重复 ID，并生成发布产物。
- 使用 Playwright 和本机 Chrome 验证 `http://127.0.0.1:8080`。
- 网页加载、语言切换、新建活动必填验证与创建、H5 预览、同步、清洗、AI 对话、初版结论到报告：通过。
- 1280×720 与 390×844：文档无横向溢出。
- 初次检查发现缺少浏览器图标；补充内嵌图标后复测通过，控制台错误与 HTTP 失败均为零。
- 本地验证服务器已关闭。
- 源码、README、历史记录、截图和 `docs` 发布目录已成功上传至 `https://github.com/Jean0708/perxio`。
- 本地 `main` 已跟踪 `origin/main`；源码与两份预览产物内容一致。

## 待完成

- 已通过连接确认 GitHub 账号为 `Jean0708`。
- 用户已确认公开仓库 `Jean0708/perxio` 及上传、发布。
- 远端初始 README 已保留至 `05_归档文件`。
- 上传工作流因当前 OAuth 登录未包含 workflow 权限被 GitHub 拒绝；采用 `main` 的 `/docs` 分支发布，Actions 配置作为参考移至 `01_项目说明`。
- 需在目标仓库启用 GitHub Pages 的 Deploy from a branch，选择 main 和 /docs。
- 浏览器控制连续超时，无法代为修改 Pages 设置；已向用户提供设置页与具体选项。
- 待用户保存 Pages 设置后检查实际预览链接 `https://jean0708.github.io/perxio/`。
- 当前为演示原型，没有真实后端、AI 或数据持久化。
