# How To: Frozenlist

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frozenlist

## Prerequisites

**Required Modules:**
- `collections`
- `functools`
- `string`
- `subprocess`
- `sys`
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.common`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = {'col1': [1, 2], 'col2': [3, 4]}
```

**Verification:**
```python
assert not com.is_bool_indexer(frozen)
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(data=data)
```

### Step 3: Assign frozen = value

```python
frozen = df.index.names[1:]
```

**Verification:**
```python
assert not com.is_bool_indexer(frozen)
```

### Step 4: Assign result = value

```python
result = df[frozen]
```

### Step 5: Assign expected = value

```python
expected = df[[]]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=data)
frozen = df.index.names[1:]
assert not com.is_bool_indexer(frozen)
result = df[frozen]
expected = df[[]]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_common.py:208 | Complexity: Intermediate | Last updated: 2026-06-02*