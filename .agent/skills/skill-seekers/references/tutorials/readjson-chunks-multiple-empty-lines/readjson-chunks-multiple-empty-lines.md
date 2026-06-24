# How To: Readjson Chunks Multiple Empty Lines

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test readjson chunks multiple empty lines

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
# Fixtures: chunksize
```

## Step-by-Step Guide

### Step 1: Assign j = '\n\n    {"A":1,"B":4}\n\n\n\n    {"A":2,"B":5}\n\n\n\n\n\n\n\n    {"A":3,"B":6}\n    '

```python
j = '\n\n    {"A":1,"B":4}\n\n\n\n    {"A":2,"B":5}\n\n\n\n\n\n\n\n    {"A":3,"B":6}\n    '
```

### Step 2: Assign orig = DataFrame(...)

```python
orig = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
```

### Step 3: Assign test = read_json(...)

```python
test = read_json(StringIO(j), lines=True, chunksize=chunksize)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(orig, test, obj=f'chunksize: {chunksize}')
```

### Step 5: Assign test = pd.concat(...)

```python
test = pd.concat(test)
```


## Complete Example

```python
# Setup
# Fixtures: chunksize

# Workflow
j = '\n\n    {"A":1,"B":4}\n\n\n\n    {"A":2,"B":5}\n\n\n\n\n\n\n\n    {"A":3,"B":6}\n    '
orig = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
test = read_json(StringIO(j), lines=True, chunksize=chunksize)
if chunksize is not None:
    with test:
        test = pd.concat(test)
tm.assert_frame_equal(orig, test, obj=f'chunksize: {chunksize}')
```

## Next Steps


---

*Source: test_readlines.py:256 | Complexity: Intermediate | Last updated: 2026-06-02*