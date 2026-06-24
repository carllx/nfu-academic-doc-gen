# How To: Missing Nested Meta

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test missing nested meta

## Prerequisites

**Required Modules:**
- `json`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.io.json._normalize`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = {'meta': 'foo', 'nested_meta': None, 'value': [{'rec': 1}, {'rec': 2}]}
```

### Step 2: Assign result = json_normalize(...)

```python
result = json_normalize(data, record_path='value', meta=['meta', ['nested_meta', 'leaf']], errors='ignore')
```

### Step 3: Assign ex_data = value

```python
ex_data = [[1, 'foo', np.nan], [2, 'foo', np.nan]]
```

### Step 4: Assign columns = value

```python
columns = ['rec', 'meta', 'nested_meta.leaf']
```

### Step 5: Assign expected = DataFrame.astype(...)

```python
expected = DataFrame(ex_data, columns=columns).astype({'nested_meta.leaf': object})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Call json_normalize()

```python
json_normalize(data, record_path='value', meta=['meta', ['nested_meta', 'leaf']], errors='raise')
```


## Complete Example

```python
# Workflow
data = {'meta': 'foo', 'nested_meta': None, 'value': [{'rec': 1}, {'rec': 2}]}
result = json_normalize(data, record_path='value', meta=['meta', ['nested_meta', 'leaf']], errors='ignore')
ex_data = [[1, 'foo', np.nan], [2, 'foo', np.nan]]
columns = ['rec', 'meta', 'nested_meta.leaf']
expected = DataFrame(ex_data, columns=columns).astype({'nested_meta.leaf': object})
tm.assert_frame_equal(result, expected)
with pytest.raises(KeyError, match="'leaf' not found"):
    json_normalize(data, record_path='value', meta=['meta', ['nested_meta', 'leaf']], errors='raise')
```

## Next Steps


---

*Source: test_normalize.py:652 | Complexity: Intermediate | Last updated: 2026-06-02*