# 执行计划

1. 创建 `.opencode/skills/` 子目录结构
2. 复制/创建 5 个本地 skill 文件
3. 更新 `SKILL.md` 前置条件 + skill 引用路径
4. 更新 `README.md` 安装说明
5. 更新 `components/01-SVG 流程图.md` skill 引用
6. 验证：SKILL.md 中不再引用外部 GitHub skill 路径

验证命令：无旧路径残留 `grep -rn "github.com.*skills" --include="*.md" SKILL.md components/ README.md`
