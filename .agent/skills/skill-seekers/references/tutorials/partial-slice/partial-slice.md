# How To: Partial Slice

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test partial slice

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range(freq='D', start=datetime(2005, 1, 1), periods=500)
```

**Verification:**
```python
assert result == s.iloc[0]
```

### Step 2: Assign s = Series(...)

```python
s = Series(np.arange(len(rng)), index=rng)
```

### Step 3: Assign result = value

```python
result = s['2005-05':'2006-02']
```

### Step 4: Assign expected = value

```python
expected = s['20050501':'20060228']
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = s['2005-05':]
```

### Step 7: Assign expected = value

```python
expected = s['20050501':]
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = value

```python
result = s[:'2006-02']
```

### Step 10: Assign expected = value

```python
expected = s[:'20060228']
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign result = value

```python
result = s['2005-1-1']
```

**Verification:**
```python
assert result == s.iloc[0]
```

### Step 13: s['2004-12-31']

```python
s['2004-12-31']
```


## Complete Example

```python
# Workflow
rng = date_range(freq='D', start=datetime(2005, 1, 1), periods=500)
s = Series(np.arange(len(rng)), index=rng)
result = s['2005-05':'2006-02']
expected = s['20050501':'20060228']
tm.assert_series_equal(result, expected)
result = s['2005-05':]
expected = s['20050501':]
tm.assert_series_equal(result, expected)
result = s[:'2006-02']
expected = s[:'20060228']
tm.assert_series_equal(result, expected)
result = s['2005-1-1']
assert result == s.iloc[0]
with pytest.raises(KeyError, match="^'2004-12-31'$"):
    s['2004-12-31']
```

## Next Steps


---

*Source: test_partial_slicing.py:175 | Complexity: Advanced | Last updated: 2026-06-02*