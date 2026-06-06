# 公开仓库同步检查清单

每次将私有开发仓库的内容同步到公开发布仓库前，请逐项检查：

## 内容检查

- [ ] 已删除所有个人本地路径配置
- [ ] 已删除所有调试代码、测试数据和临时文件
- [ ] 已删除所有个人研究笔记和决策记录
- [ ] 所有新功能均经过至少一个完整研究项目验证
- [ ] 所有文档已更新，与当前功能一致

## 版本检查

- [ ] 已更新公开发布仓库的 README 版本说明
- [ ] 已更新 CHANGELOG.md（如有）
- [ ] 已准备好新版本的 tag（语义化版本：vX.Y.Z）

## 同步操作

```bash
# 1. 在私有开发仓库 main 分支提交所有修改
git checkout main
git add -A
git commit -m "..."
git push origin main

# 2. 切换到 public-release 分支并合并 main 的改动
git checkout public-release
git merge main

# 3. 清理个人内容（按需执行）
# 编辑 AGENTS.md、README.md 等文件，移除个人信息

# 4. 提交清理后的内容
git add -A
git commit -m "chore: 同步公开发布版本 vX.Y.Z"

# 5. 推送到公开发布仓库
git push public main --force

# 6. 打标签并推送
git tag vX.Y.Z
git push public vX.Y.Z

# 7. 切回 main 继续开发
git checkout main
```

## 远程仓库配置

| 远程名 | 仓库 | 用途 |
|--------|------|------|
| `origin` | `wongzt/workflow-for-economists-dev` (Private) | 日常开发 |
| `public` | `wongzt/workflow-for-economists` (Public) | 稳定发布 |
