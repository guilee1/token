"""List models available to a Buddy API key or summarize a sample ticket."""

import argparse
import getpass
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


BASE_URL = "https://buddy.santop.vip/v1"
TICKET = (
    "Summarize this support ticket in one sentence and suggest the next step. "
    "Ticket: My card shows two charges for the same order, but I received only "
    "one confirmation email."
)


def request_json(path, key, payload=None):
    body = json.dumps(payload).encode() if payload is not None else None
    request = Request(
        BASE_URL + path,
        data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    with urlopen(request, timeout=90) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", help="Send one billable chat request using this model ID")
    args = parser.parse_args()
    key = (os.environ.get("BUDDY_API_KEY") or getpass.getpass("Buddy API key: ")).strip()
    if not key:
        raise SystemExit("A Buddy API key is required.")
    if not args.model:
        result = request_json("/models", key)
        models = [entry["id"] for entry in result["data"]]
        print("\n".join(models) or "No models returned for this key's group.")
        return
    result = request_json(
        "/chat/completions", key,
        {"model": args.model, "messages": [{"role": "user", "content": TICKET}]},
    )
    message = result["choices"][0]["message"]
    print(message.get("content") or message.get("refusal") or "(No text returned)")
    if result.get("usage"):
        print("Token usage:", json.dumps(result["usage"], ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except HTTPError as exc:
        sys.exit(f"HTTP {exc.code} from Buddy. See the troubleshooting table in the README.")
    except (URLError, TimeoutError) as exc:
        sys.exit(f"Could not reach Buddy: {exc}")
    except (ValueError, KeyError, IndexError, TypeError):
        sys.exit("Unexpected API response. Check the model and its supported endpoint.")
