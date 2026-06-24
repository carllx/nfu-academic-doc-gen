# How To: To Json Append Output Consistent Columns

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to json append output consistent columns

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'col1': [3, 4], 'col2': ['c', 'd']})
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'col1': [1, 2, 3, 4], 'col2': ['a', 'b', 'c', 'd']})
```

### Step 4: Call df1.to_json()

```python
df1.to_json(path, lines=True, orient='records')
```

### Step 5: Call df2.to_json()

```python
df2.to_json(path, mode='a', lines=True, orient='records')
```

### Step 6: Assign result = read_json(...)

```python
result = read_json(path, lines=True)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
df2 = DataFrame({'col1': [3, 4], 'col2': ['c', 'd']})
expected = DataFrame({'col1': [1, 2, 3, 4], 'col2': ['a', 'b', 'c', 'd']})
with tm.ensure_clean('test.json') as path:
    df1.to_json(path, lines=True, orient='records')
    df2.to_json(path, mode='a', lines=True, orient='records')
    result = read_json(path, lines=True)
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_readlines.py:445 | Complexity: Intermediate | Last updated: 2026-06-02*