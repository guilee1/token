# Buddy API 快速入门：调用 GPT Sol，查看 Token 用量

[Buddy 算力平台 · buddy.santop.vip](https://buddy.santop.vip/?utm_source=github&utm_medium=readme_zh&utm_campaign=api_quickstart) · [English guide](README.md)

用一个 Python 脚本查出你的 Key 可以调用哪些模型，再选一个模型总结客服工单。示例只用 Python 标准库，请求发往 `https://buddy.santop.vip/v1`。

## 查可用模型

1. 登录 Buddy，在[模型广场](https://buddy.santop.vip/available-channels)查看所选分组的价格，然后在[密钥管理](https://buddy.santop.vip/keys)为该分组创建 Buddy API Key。
2. 下载本仓库文件，在 `buddy.py` 所在目录打开终端。
3. 使用 Python 3.9 或更高版本执行下面的命令。脚本会提示输入 Key，输入时不会回显。自动化运行时也可以用环境变量 `BUDDY_API_KEY` 传入。

```console
python buddy.py
```

每行输出一个模型 ID。想试 GPT Sol 时，先看结果里有没有 `gpt-6.1-sol`。如果有，就复制这个 ID 用于下一步。如果没有，选择列表里另一个支持 Chat Completions 的文本模型。

## 总结一张客服工单

把下面的 `YOUR_MODEL_ID` 换成你复制的 ID。此步骤会发送一次模型请求，可能按你的分组价格计费。

```console
python buddy.py --model YOUR_MODEL_ID
```

示例内置一张虚构的重复扣款工单，要求模型用一句话总结问题并建议下一步。脚本会打印答复以及接口返回的 Token 用量，你可以在[使用记录](https://buddy.santop.vip/usage)核对这次调用。

## 常见问题

| 遇到的情况 | 检查方法 |
| --- | --- |
| HTTP 401 | 使用 Buddy 站内创建的 Key。GitHub Token 或其他厂商的 Key 无法在这里认证。 |
| 模型列表为空或模型不可用 | 到控制台检查 Key 绑定的分组，再重新列出模型。 |
| HTTP 429 | 查看分组的并发限制，等正在运行的请求完成后再重试。 |
| 其他客户端收到 HTML | Base URL 填 `https://buddy.santop.vip/v1`，获取模型的完整地址应为 `https://buddy.santop.vip/v1/models`。 |

本指南由 Buddy 算力平台维护。可用模型和实际计费以所选分组为准。
