# Buddy API Quickstart for GPT Sol and Token Usage

[buddy.santop.vip](https://buddy.santop.vip/?utm_source=github&utm_medium=readme&utm_campaign=api_quickstart) · [中文指南](README.zh-CN.md)

List the models available to your Buddy API key, then use one to summarize a sample support ticket. The Python example runs with the standard library and sends requests to `https://buddy.santop.vip/v1`.

## List available models

1. Sign in to Buddy, check the prices for your group in the [model marketplace](https://buddy.santop.vip/available-channels), and create a [Buddy API key](https://buddy.santop.vip/keys).
2. Download the files from this repository and open a terminal in the folder containing `buddy.py`.
3. With Python 3.9 or later, run the following command. The script prompts for your key without displaying it. For automation, you can supply the `BUDDY_API_KEY` environment variable instead.

```console
python buddy.py
```

This prints one model ID per line. To try a GPT Sol model, look for an ID such as `gpt-6.1-sol` in the output. If your key lists it, use that exact ID in the next step. Otherwise choose another listed text model that supports Chat Completions.

## Summarize a support ticket

Replace `YOUR_MODEL_ID` with the ID you copied. This step sends one model request and can incur a charge at your group's rate.

```console
python buddy.py --model YOUR_MODEL_ID
```

The example asks the model to summarize a fictional customer's duplicate charge in one sentence and suggest a next step. It prints the model's reply and any token counts returned by the API. Compare these with the same request in the [usage dashboard](https://buddy.santop.vip/usage).

## Troubleshooting

| Result | What to check |
| --- | --- |
| HTTP 401 | Use a key issued by Buddy. A GitHub token or an upstream provider's key will not authenticate here. |
| Model list is empty, or the model is unavailable | Check your key's group in the dashboard, then list the models again. |
| HTTP 429 | Check your group's concurrency limit and retry after the current request completes. |
| HTML instead of JSON in another API client | Set the client's base URL to `https://buddy.santop.vip/v1`. The full models endpoint is `https://buddy.santop.vip/v1/models`. |

Buddy operates the gateway and maintains this guide. Model availability and billing depend on the group you select.
