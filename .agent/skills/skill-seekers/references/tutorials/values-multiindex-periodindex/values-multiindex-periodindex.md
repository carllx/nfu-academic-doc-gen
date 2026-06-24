# How To: Values Multiindex Periodindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test values multiindex periodindex

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ints = np.arange(...)

```python
ints = np.arange(2007, 2012)
```

### Step 2: Assign pidx = pd.PeriodIndex(...)

```python
pidx = pd.PeriodIndex(ints, freq='D')
```

### Step 3: Assign idx = MultiIndex.from_arrays(...)

```python
idx = MultiIndex.from_arrays([ints, pidx])
```

### Step 4: Assign result = value

```python
result = idx.values
```

### Step 5: Assign outer = Index(...)

```python
outer = Index([x[0] for x in result])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(outer, Index(ints, dtype=np.int64))
```

### Step 7: Assign inner = pd.PeriodIndex(...)

```python
inner = pd.PeriodIndex([x[1] for x in result])
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(inner, pidx)
```

### Step 9: Assign result = value

```python
result = idx[:2].values
```

### Step 10: Assign outer = Index(...)

```python
outer = Index([x[0] for x in result])
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(outer, Index(ints[:2], dtype=np.int64))
```

### Step 12: Assign inner = pd.PeriodIndex(...)

```python
inner = pd.PeriodIndex([x[1] for x in result])
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(inner, pidx[:2])
```


## Complete Example

```python
# Workflow
ints = np.arange(2007, 2012)
pidx = pd.PeriodIndex(ints, freq='D')
idx = MultiIndex.from_arrays([ints, pidx])
result = idx.values
outer = Index([x[0] for x in result])
tm.assert_index_equal(outer, Index(ints, dtype=np.int64))
inner = pd.PeriodIndex([x[1] for x in result])
tm.assert_index_equal(inner, pidx)
result = idx[:2].values
outer = Index([x[0] for x in result])
tm.assert_index_equal(outer, Index(ints[:2], dtype=np.int64))
inner = pd.PeriodIndex([x[1] for x in result])
tm.assert_index_equal(inner, pidx[:2])
```

## Next Steps


---

*Source: test_integrity.py:80 | Complexity: Advanced | Last updated: 2026-06-02*