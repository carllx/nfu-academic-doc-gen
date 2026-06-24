# How To: Readjson Nrows Chunks

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test readjson nrows chunks

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
# Fixtures: request, nrows, chunksize, engine
```

## Step-by-Step Guide

### Step 1: Assign jsonl = '{"a": 1, "b": 2}\n        {"a": 3, "b": 4}\n        {"a": 5, "b": 6}\n        {"a": 7, "b": 8}'

```python
jsonl = '{"a": 1, "b": 2}\n        {"a": 3, "b": 4}\n        {"a": 5, "b": 6}\n        {"a": 7, "b": 8}'
```

### Step 2: Assign expected = value

```python
expected = DataFrame({'a': [1, 3, 5, 7], 'b': [2, 4, 6, 8]}).iloc[:nrows]
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(chunked, expected)
```

### Step 4: Assign reason = "Pyarrow only supports a file path as an input and line delimited jsonand doesn't support chunksize parameter."

```python
reason = "Pyarrow only supports a file path as an input and line delimited jsonand doesn't support chunksize parameter."
```

### Step 5: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason=reason, raises=ValueError))
```

### Step 6: Assign chunked = pd.concat(...)

```python
chunked = pd.concat(reader)
```

### Step 7: Assign chunked = pd.concat(...)

```python
chunked = pd.concat(reader)
```


## Complete Example

```python
# Setup
# Fixtures: request, nrows, chunksize, engine

# Workflow
if engine == 'pyarrow':
    reason = "Pyarrow only supports a file path as an input and line delimited jsonand doesn't support chunksize parameter."
    request.applymarker(pytest.mark.xfail(reason=reason, raises=ValueError))
jsonl = '{"a": 1, "b": 2}\n        {"a": 3, "b": 4}\n        {"a": 5, "b": 6}\n        {"a": 7, "b": 8}'
if engine != 'pyarrow':
    with read_json(StringIO(jsonl), lines=True, nrows=nrows, chunksize=chunksize, engine=engine) as reader:
        chunked = pd.concat(reader)
else:
    with read_json(jsonl, lines=True, nrows=nrows, chunksize=chunksize, engine=engine) as reader:
        chunked = pd.concat(reader)
expected = DataFrame({'a': [1, 3, 5, 7], 'b': [2, 4, 6, 8]}).iloc[:nrows]
tm.assert_frame_equal(chunked, expected)
```

## Next Steps


---

*Source: test_readlines.py:314 | Complexity: Intermediate | Last updated: 2026-06-02*