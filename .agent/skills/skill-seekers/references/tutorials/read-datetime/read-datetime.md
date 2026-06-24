# How To: Read Datetime

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read datetime

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([([1, 2], ['2020-03-05', '2020-04-08T09:58:49+00:00'], 'hector')], columns=['accounts', 'date', 'name'])
```

### Step 2: Assign json_line = df.to_json(...)

```python
json_line = df.to_json(lines=True, orient='records')
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, '2020-03-05', 'hector'], [2, '2020-04-08T09:58:49+00:00', 'hector']], columns=['accounts', 'date', 'name'])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign reason = 'Pyarrow only supports a file path as an input and line delimited json'

```python
reason = 'Pyarrow only supports a file path as an input and line delimited json'
```

### Step 6: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason=reason, raises=ValueError))
```

### Step 7: Assign result = read_json(...)

```python
result = read_json(StringIO(json_line), engine=engine)
```

### Step 8: Assign result = read_json(...)

```python
result = read_json(StringIO(json_line), engine=engine)
```


## Complete Example

```python
# Setup
# Fixtures: request, engine

# Workflow
if engine == 'pyarrow':
    reason = 'Pyarrow only supports a file path as an input and line delimited json'
    request.applymarker(pytest.mark.xfail(reason=reason, raises=ValueError))
df = DataFrame([([1, 2], ['2020-03-05', '2020-04-08T09:58:49+00:00'], 'hector')], columns=['accounts', 'date', 'name'])
json_line = df.to_json(lines=True, orient='records')
if engine == 'pyarrow':
    result = read_json(StringIO(json_line), engine=engine)
else:
    result = read_json(StringIO(json_line), engine=engine)
expected = DataFrame([[1, '2020-03-05', 'hector'], [2, '2020-04-08T09:58:49+00:00', 'hector']], columns=['accounts', 'date', 'name'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_readlines.py:52 | Complexity: Advanced | Last updated: 2026-06-02*