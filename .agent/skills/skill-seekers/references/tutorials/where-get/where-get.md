# How To: Where Get

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where get

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas._testing._hypothesis`

**Setup Required:**
```python
# Fixtures: where_frame, float_string_frame
```

## Step-by-Step Guide

### Step 1: Assign df = where_frame

```python
df = where_frame
```

**Verification:**
```python
assert (rs.dtypes == df.dtypes).all()
```

### Step 2: Assign cond = value

```python
cond = df > 0
```

### Step 3: Call _check_get()

```python
_check_get(df, cond)
```

### Step 4: Assign other1 = _safe_add(...)

```python
other1 = _safe_add(df)
```

### Step 5: Assign rs = df.where(...)

```python
rs = df.where(cond, other1)
```

### Step 6: Assign rs2 = df.where(...)

```python
rs2 = df.where(cond.values, other1)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(rs, rs2)
```

### Step 8: Assign msg = "'>' not supported between instances of 'str' and 'int'|Invalid comparison"

```python
msg = "'>' not supported between instances of 'str' and 'int'|Invalid comparison"
```

### Step 9: Assign exp = Series(...)

```python
exp = Series(np.where(cond[k], df[k], other1[k]), index=v.index)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(v, exp, check_names=False)
```

**Verification:**
```python
assert (rs.dtypes == df.dtypes).all()
```

### Step 11: df > 0

```python
df > 0
```


## Complete Example

```python
# Setup
# Fixtures: where_frame, float_string_frame

# Workflow
def _check_get(df, cond, check_dtypes=True):
    other1 = _safe_add(df)
    rs = df.where(cond, other1)
    rs2 = df.where(cond.values, other1)
    for k, v in rs.items():
        exp = Series(np.where(cond[k], df[k], other1[k]), index=v.index)
        tm.assert_series_equal(v, exp, check_names=False)
    tm.assert_frame_equal(rs, rs2)
    if check_dtypes:
        assert (rs.dtypes == df.dtypes).all()
df = where_frame
if df is float_string_frame:
    msg = "'>' not supported between instances of 'str' and 'int'|Invalid comparison"
    with pytest.raises(TypeError, match=msg):
        df > 0
    return
cond = df > 0
_check_get(df, cond)
```

## Next Steps


---

*Source: test_where.py:49 | Complexity: Advanced | Last updated: 2026-06-02*