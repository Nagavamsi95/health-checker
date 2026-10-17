import time
import requests
import yaml


def load_config(path="config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)["endpoints"]


def check_endpoint(endpoint, timeout=5):
    name = endpoint["name"]
    url = endpoint["url"]
    start = time.time()

    try:
        response = requests.get(url, timeout=timeout)
        elapsed_ms = round((time.time() - start) * 1000)
        healthy = response.status_code < 400
        return {
            "name": name,
            "url": url,
            "status": "UP" if healthy else "DOWN",
            "code": response.status_code,
            "response_ms": elapsed_ms,
        }
    except requests.RequestException as e:
        return {
            "name": name,
            "url": url,
            "status": "DOWN",
            "code": None,
            "response_ms": None,
            "error": str(e),
        }


def run_checks(path="config.yaml"):
    return [check_endpoint(e) for e in load_config(path)]


if __name__ == "__main__":
    for r in run_checks():
        if r["code"] is None:
            print(f"[DOWN] {r['name']}: {r['error']}")
        else:
            print(f"[{r['status']}] {r['name']}: HTTP {r['code']} in {r['response_ms']} ms")