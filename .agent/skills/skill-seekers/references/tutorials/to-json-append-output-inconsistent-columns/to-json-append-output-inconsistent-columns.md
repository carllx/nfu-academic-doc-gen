# How To: To Json Append Output Inconsistent Columns

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to json append output inconsistent columns

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

### Step 2: Assign df3 = DataFrame(...)

```python
df3 = DataFrame({'col2': ['e', 'f'], 'col3': ['!', '#']})
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'col1': [1, 2, None, None], 'col2': ['a', 'b', 'e', 'f'], 'col3': [np.nan, np.nan, '!', '#']})
```

### Step 4: Call df1.to_json()

```python
df1.to_json(path, mode='a', lines=True, orient='records')
```

### Step 5: Call df3.to_json()

```python
df3.to_json(path, mode='a', lines=True, orient='records')
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
df3 = DataFrame({'col2': ['e', 'f'], 'col3': ['!', '#']})
expected = DataFrame({'col1': [1, 2, None, None], 'col2': ['a', 'b', 'e', 'f'], 'col3': [np.nan, np.nan, '!', '#']})
with tm.ensure_clean('test.json') as path:
    df1.to_json(path, mode='a', lines=True, orient='records')
    df3.to_json(path, mode='a', lines=True, orient='records')
    result = read_json(path, lines=True)
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_readlines.py:463 | Complexity: Intermediate | Last updated: 2026-06-02*