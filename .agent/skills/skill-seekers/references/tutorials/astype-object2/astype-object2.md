# How To: Astype Object2

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype object2

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = period_range(...)

```python
idx = period_range(start='2013-01-01', periods=4, freq='M', name='idx')
```

**Verification:**
```python
assert isinstance(result, Index)
```

### Step 2: Assign expected_list = value

```python
expected_list = [Period('2013-01-31', freq='M'), Period('2013-02-28', freq='M'), Period('2013-03-31', freq='M'), Period('2013-04-30', freq='M')]
```

**Verification:**
```python
assert result.dtype == object
```

### Step 3: Assign expected = Index(...)

```python
expected = Index(expected_list, dtype=object, name='idx')
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 4: Assign result = idx.astype(...)

```python
result = idx.astype(object)
```

**Verification:**
```python
assert idx.tolist() == expected_list
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert isinstance(result, Index)
```

### Step 6: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2013-01-01', '2013-01-02', 'NaT', '2013-01-04'], freq='D', name='idx')
```

**Verification:**
```python
assert result.dtype == object
```

### Step 7: Assign expected_list = value

```python
expected_list = [Period('2013-01-01', freq='D'), Period('2013-01-02', freq='D'), Period('NaT', freq='D'), Period('2013-01-04', freq='D')]
```

**Verification:**
```python
assert result[i] == expected[i]
```

### Step 8: Assign expected = Index(...)

```python
expected = Index(expected_list, dtype=object, name='idx')
```

**Verification:**
```python
assert result[2] is NaT
```

### Step 9: Assign result = idx.astype(...)

```python
result = idx.astype(object)
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert result_list[i] == expected_list[i]
```

### Step 11: Assign result_list = idx.tolist(...)

```python
result_list = idx.tolist()
```

**Verification:**
```python
assert result_list[2] is NaT
```


## Complete Example

```python
# Workflow
idx = period_range(start='2013-01-01', periods=4, freq='M', name='idx')
expected_list = [Period('2013-01-31', freq='M'), Period('2013-02-28', freq='M'), Period('2013-03-31', freq='M'), Period('2013-04-30', freq='M')]
expected = Index(expected_list, dtype=object, name='idx')
result = idx.astype(object)
assert isinstance(result, Index)
assert result.dtype == object
tm.assert_index_equal(result, expected)
assert result.name == expected.name
assert idx.tolist() == expected_list
idx = PeriodIndex(['2013-01-01', '2013-01-02', 'NaT', '2013-01-04'], freq='D', name='idx')
expected_list = [Period('2013-01-01', freq='D'), Period('2013-01-02', freq='D'), Period('NaT', freq='D'), Period('2013-01-04', freq='D')]
expected = Index(expected_list, dtype=object, name='idx')
result = idx.astype(object)
assert isinstance(result, Index)
assert result.dtype == object
tm.assert_index_equal(result, expected)
for i in [0, 1, 3]:
    assert result[i] == expected[i]
assert result[2] is NaT
assert result.name == expected.name
result_list = idx.tolist()
for i in [0, 1, 3]:
    assert result_list[i] == expected_list[i]
assert result_list[2] is NaT
```

## Next Steps


---

*Source: test_astype.py:85 | Complexity: Advanced | Last updated: 2026-06-02*