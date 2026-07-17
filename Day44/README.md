# Day 44, Smart API Explorer

Today the code made its first real network request.

It's not reading a file, not processing local data but actually going out to the internet, hitting an endpoint and getting live data back. That gap between local programs and networked ones felt big before today. It feels smaller now.

---

## What this does

This program connects to a public REST API (jsonplaceholder.typicode.com/posts), fetches 100 posts, then lets you browse them, search by ID, save the full response as a .json file, and view a log of every request made during the session.

There are six menu options. All of it was built using only Python's standard library, no requests, no third-party packages.

---

## The fetch function

```python
with urlopen(API_URL) as response:
    status_code = response.status
    data = json.loads(response.read().decode("utf-8"))
```

`urllib.request.urlopen()` opens the URL like a file. `.read()` gets the raw bytes. `.decode("utf-8")` turns it into a string. `json.loads()` parses that string into a Python list of dictionaries.

---

## Error handling on network calls

```python
except HTTPError as error:
    log_request(f"HTTP Error: {error.code}")

except URLError:
    log_request("Network connection failed.")
```

I used two separate exceptions, one for HTTP-level errors (404, 500 etc.) and one for connection-level failures (no internet, wrong URL) Handling both separately matters because they mean different things and need different responses.

---

## Request logging

Every action gets logged to a .txt file with a timestamp:

```python
with LOG_FILE.open("a", encoding="utf-8") as file:
    file.write(f"[{timestamp}] {message}\n")
```

Opens in append mode (`"a"`) so previous logs aren't overwritten. This is the same pattern real applications uses for audit trails and debugging logs. It's just a small detail but my real-world habit.

---

## Saving responses

```python
file_path.write_text(
    json.dumps(posts, indent=4),
    encoding="utf-8"
)
```

`json.dumps()` with indent=4, formats the JSON cleanly. Every saved response gets a timestamped filename so nothing overwrites anything else.

---

## Folder structure

```
Day44/
├── api_logs/
│   └── request_history.txt
├── saved_responses/
│   └── response_YYYY-MM-DD_HH-MM-SS.json
└── day44_smart_api_explorer.py
```

---

## What shifted today

Every previous project in this challenge has been self-contained — data goes in, data comes out, everything stays local. But today's project depends on something external. The program can fail for reasons that have nothing to do with the code — no internet, API is down, rate limited.

That changes how I think about writing functions. You stop assuming things will work and start planning for when they don't.

---

*Day 44, first live API call done. urllib, JSON parsing, logging.*