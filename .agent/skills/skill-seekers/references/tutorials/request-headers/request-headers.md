# How To: Request Headers

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test request headers

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `gzip`
- `io`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `fsspec`

**Setup Required:**
```python
# Fixtures: responder, read_method, httpserver, storage_options
```

## Step-by-Step Guide

### Step 1: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': ['b']})
```

**Verification:**
```python
assert exp == storage_options[header]
```

### Step 2: Assign default_headers = value

```python
default_headers = ['Accept-Encoding', 'Host', 'Connection', 'User-Agent']
```

**Verification:**
```python
assert not request_headers
```

### Step 3: Assign expected_headers = set.union(...)

```python
expected_headers = set(default_headers).union(storage_options.keys() if storage_options else [])
```

### Step 4: Call httpserver.serve_content()

```python
httpserver.serve_content(content=responder(expected), headers=extra)
```

### Step 5: Assign result = read_method(...)

```python
result = read_method(httpserver.url, storage_options=storage_options)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign request_headers = dict(...)

```python
request_headers = dict(httpserver.requests[0].headers)
```

**Verification:**
```python
assert not request_headers
```

### Step 8: Assign extra = value

```python
extra = {'Content-Encoding': 'gzip'}
```

### Step 9: Assign extra = None

```python
extra = None
```

### Step 10: Assign exp = request_headers.pop(...)

```python
exp = request_headers.pop(header)
```

### Step 11: Assign storage_options = extra

```python
storage_options = extra
```

**Verification:**
```python
assert exp == storage_options[header]
```


## Complete Example

```python
# Setup
# Fixtures: responder, read_method, httpserver, storage_options

# Workflow
expected = pd.DataFrame({'a': ['b']})
default_headers = ['Accept-Encoding', 'Host', 'Connection', 'User-Agent']
if 'gz' in responder.__name__:
    extra = {'Content-Encoding': 'gzip'}
    if storage_options is None:
        storage_options = extra
    else:
        storage_options |= extra
else:
    extra = None
expected_headers = set(default_headers).union(storage_options.keys() if storage_options else [])
httpserver.serve_content(content=responder(expected), headers=extra)
result = read_method(httpserver.url, storage_options=storage_options)
tm.assert_frame_equal(result, expected)
request_headers = dict(httpserver.requests[0].headers)
for header in expected_headers:
    exp = request_headers.pop(header)
    if storage_options and header in storage_options:
        assert exp == storage_options[header]
assert not request_headers
```

## Next Steps


---

*Source: test_http_headers.py:127 | Complexity: Advanced | Last updated: 2026-06-02*