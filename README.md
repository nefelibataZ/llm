# LLM · EduAgent 学习项目

面向大模型应用开发的渐进式实践仓库，从可复现的教育问答闭环开始。

## 快速开始

需要 Python 3.11 或更新版本。在仓库根目录运行：

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS / Linux: source .venv/bin/activate
python -m pip install -e .
python -m eduagent "RAG 是什么？"
python -m unittest discover -s tests -v
```

首次安装需要从软件源获取构建工具 setuptools。无网络时可跳过安装，从仓库根目录直接运行（PowerShell）：

```powershell
$env:PYTHONPATH = (Join-Path (Get-Location) "src")
python -m eduagent "RAG 是什么？"
python -m unittest discover -s tests -v
```

macOS / Linux 对应使用 `PYTHONPATH=src python -m eduagent "RAG 是什么？"`。

也可安装后运行：`eduagent "如何学习 Agent？"`。

默认使用离线 extractive 模式：从示例课程数据检索并摘录原文，不调用真实大模型，也不需要密钥。输出明确标记模式并给出来源；无命中时拒绝编造答案。它验证的是检索、上下文组织、回答与引用的工程闭环，不代表真实 LLM 或完整自治 Agent。

示例输出：
```text
模式：offline-extractive
回答：RAG（检索增强生成）先检索课程知识，再将相关上下文交给大模型生成回答。回答应附来源，证据不足时应说明无法回答。
来源：rag-intro | RAG 入门
```

## 目录与文件用途

| 文件 | 当前用途 | 后续扩展 |
| --- | --- | --- |
| README.md | 安装、运行、边界和导航 | 增加实际演示与部署说明 |
| pyproject.toml | 包元数据、Python 版本、安装及 CLI 入口；运行时零第三方依赖 | 接入真实模型时增加可选依赖及锁文件 |
| .gitignore | 排除密钥、缓存、虚拟环境和本地数据 | 增加模型缓存规则 |
| src/eduagent/__init__.py | 包入口与版本 | 公共接口 |
| src/eduagent/__main__.py | 命令行参数与错误提示 | 服务入口、批量提问 |
| src/eduagent/qa.py | 离线检索、答案和来源结构 | 向量检索、重排、模型适配器 |
| src/eduagent/data/lessons.json | 随包分发的虚构课程知识 | 经授权的课程语料与版本管理 |
| examples/README.md | 示例命令及预期行为 | 批改、简历与面试示例 |
| tests/test_qa.py | 命中、拒答、空输入和 CLI 回归 | 检索评估、模型契约测试 |
| docs/roadmap.md | 分阶段学习路线及验收标准 | 迭代记录与架构决策 |

## 开发约定

- 业务逻辑放在 src/eduagent，演示说明放 examples，学习设计放 docs。
- 仅提交可公开的合成数据；不提交学生资料、简历、考试原卷或密钥。
- 真实模型接入时从环境变量读取凭据，并补齐超时、失败处理、费用观测和离线测试替身。
- 每次迭代保持上述运行与测试命令通过。

详见 [学习路线](docs/roadmap.md) 和 [示例](examples/README.md)。
