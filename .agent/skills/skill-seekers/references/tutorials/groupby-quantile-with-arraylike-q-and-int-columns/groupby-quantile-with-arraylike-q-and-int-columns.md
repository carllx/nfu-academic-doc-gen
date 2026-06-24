# How To: Groupby Quantile With Arraylike Q And Int Columns

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby quantile with arraylike q and int columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_size, groupby, q
```

## Step-by-Step Guide

### Step 1: Assign unknown = frame_size

```python
nrow, ncol = frame_size
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.array([ncol * [_ % 4] for _ in range(nrow)]), columns=range(ncol))
```

### Step 3: Assign idx_levels = value

```python
idx_levels = [np.arange(min(nrow, 4))] * len(groupby) + [q]
```

### Step 4: Assign idx_codes = value

```python
idx_codes = [[x for x in range(min(nrow, 4)) for _ in q]] * len(groupby) + [list(range(len(q))) * min(nrow, 4)]
```

### Step 5: Assign expected_index = pd.MultiIndex(...)

```python
expected_index = pd.MultiIndex(levels=idx_levels, codes=idx_codes, names=groupby + [None])
```

### Step 6: Assign expected_values = value

```python
expected_values = [[float(x)] * (ncol - len(groupby)) for x in range(min(nrow, 4)) for _ in q]
```

### Step 7: Assign expected_columns = value

```python
expected_columns = [x for x in range(ncol) if x not in groupby]
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_values, index=expected_index, columns=expected_columns)
```

### Step 9: Assign result = df.groupby.quantile(...)

```python
result = df.groupby(groupby).quantile(q)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_size, groupby, q

# Workflow
nrow, ncol = frame_size
df = DataFrame(np.array([ncol * [_ % 4] for _ in range(nrow)]), columns=range(ncol))
idx_levels = [np.arange(min(nrow, 4))] * len(groupby) + [q]
idx_codes = [[x for x in range(min(nrow, 4)) for _ in q]] * len(groupby) + [list(range(len(q))) * min(nrow, 4)]
expected_index = pd.MultiIndex(levels=idx_levels, codes=idx_codes, names=groupby + [None])
expected_values = [[float(x)] * (ncol - len(groupby)) for x in range(min(nrow, 4)) for _ in q]
expected_columns = [x for x in range(ncol) if x not in groupby]
expected = DataFrame(expected_values, index=expected_index, columns=expected_columns)
result = df.groupby(groupby).quantile(q)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_quantile.py:147 | Complexity: Advanced | Last updated: 2026-06-02*