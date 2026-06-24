# How To: Get Indexer Mismatched Dtype With Method

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get indexer mismatched dtype with method

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: non_comparable_idx, method
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=3)
```

### Step 2: Assign pi = dti.to_period(...)

```python
pi = dti.to_period('D')
```

### Step 3: Assign other = non_comparable_idx

```python
other = non_comparable_idx
```

### Step 4: Assign msg = re.escape(...)

```python
msg = re.escape(f'Cannot compare dtypes {pi.dtype} and {other.dtype}')
```

### Step 5: Call pi.get_indexer()

```python
pi.get_indexer(other, method=method)
```

### Step 6: Assign other2 = other.astype(...)

```python
other2 = other.astype(dtype)
```

### Step 7: Assign msg = unknown.join(...)

```python
msg = '|'.join([re.escape(msg) for msg in (f'Cannot compare dtypes {pi.dtype} and {other.dtype}', ' not supported between instances of ')])
```

### Step 8: Call pi.get_indexer()

```python
pi.get_indexer(other2, method=method)
```


## Complete Example

```python
# Setup
# Fixtures: non_comparable_idx, method

# Workflow
dti = date_range('2016-01-01', periods=3)
pi = dti.to_period('D')
other = non_comparable_idx
msg = re.escape(f'Cannot compare dtypes {pi.dtype} and {other.dtype}')
with pytest.raises(TypeError, match=msg):
    pi.get_indexer(other, method=method)
for dtype in ['object', 'category']:
    other2 = other.astype(dtype)
    if dtype == 'object' and isinstance(other, PeriodIndex):
        continue
    msg = '|'.join([re.escape(msg) for msg in (f'Cannot compare dtypes {pi.dtype} and {other.dtype}', ' not supported between instances of ')])
    with pytest.raises(TypeError, match=msg):
        pi.get_indexer(other2, method=method)
```

## Next Steps


---

*Source: test_indexing.py:436 | Complexity: Advanced | Last updated: 2026-06-02*