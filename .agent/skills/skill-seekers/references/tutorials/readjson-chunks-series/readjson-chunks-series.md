# How To: Readjson Chunks Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test readjson chunks series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections.abc`
- `io`
- `pathlib`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.json._json`

**Setup Required:**
```python
# Fixtures: request, engine
```

## Step-by-Step Guide

### Step 1: Assign s = pd.Series(...)

```python
s = pd.Series({'A': 1, 'B': 2})
```

### Step 2: Assign strio = StringIO(...)

```python
strio = StringIO(s.to_json(lines=True, orient='records'))
```

### Step 3: Assign unchunked = read_json(...)

```python
unchunked = read_json(strio, lines=True, typ='Series', engine=engine)
```

### Step 4: Assign strio = StringIO(...)

```python
strio = StringIO(s.to_json(lines=True, orient='records'))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(chunked, unchunked)
```

### Step 6: Assign reason = "Pyarrow only supports a file path as an input and line delimited jsonand doesn't support chunksize parameter."

```python
reason = "Pyarrow only supports a file path as an input and line delimited jsonand doesn't support chunksize parameter."
```

### Step 7: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason=reason))
```

### Step 8: Assign chunked = pd.concat(...)

```python
chunked = pd.concat(reader)
```


## Complete Example

```python
# Setup
# Fixtures: request, engine

# Workflow
if engine == 'pyarrow':
    reason = "Pyarrow only supports a file path as an input and line delimited jsonand doesn't support chunksize parameter."
    request.applymarker(pytest.mark.xfail(reason=reason))
s = pd.Series({'A': 1, 'B': 2})
strio = StringIO(s.to_json(lines=True, orient='records'))
unchunked = read_json(strio, lines=True, typ='Series', engine=engine)
strio = StringIO(s.to_json(lines=True, orient='records'))
with read_json(strio, lines=True, typ='Series', chunksize=1, engine=engine) as reader:
    chunked = pd.concat(reader)
tm.assert_series_equal(chunked, unchunked)
```

## Next Steps


---

*Source: test_readlines.py:155 | Complexity: Advanced | Last updated: 2026-06-02*