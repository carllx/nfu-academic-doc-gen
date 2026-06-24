# How To: Index String Inference

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test index string inference

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign expected = Index(...)

```python
expected = Index(['a', 'b'], dtype=pd.StringDtype(na_value=np.nan))
```

### Step 2: Call tm.assert_index_equal()

```python
tm.assert_index_equal(ser, expected)
```

### Step 3: Assign expected = Index(...)

```python
expected = Index(['a', 1], dtype='object')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(ser, expected)
```

### Step 5: Assign ser = Index(...)

```python
ser = Index(['a', 'b'])
```

### Step 6: Assign ser = Index(...)

```python
ser = Index(['a', 1])
```


## Complete Example

```python
# Workflow
expected = Index(['a', 'b'], dtype=pd.StringDtype(na_value=np.nan))
with pd.option_context('future.infer_string', True):
    ser = Index(['a', 'b'])
tm.assert_index_equal(ser, expected)
expected = Index(['a', 1], dtype='object')
with pd.option_context('future.infer_string', True):
    ser = Index(['a', 1])
tm.assert_index_equal(ser, expected)
```

## Next Steps


---

*Source: test_constructors.py:48 | Complexity: Intermediate | Last updated: 2026-06-02*