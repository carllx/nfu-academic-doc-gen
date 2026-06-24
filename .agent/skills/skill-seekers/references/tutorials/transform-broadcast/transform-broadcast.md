# How To: Transform Broadcast

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transform broadcast

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: tsframe, ts
```

## Step-by-Step Guide

### Step 1: Assign grouped = ts.groupby(...)

```python
grouped = ts.groupby(lambda x: x.month)
```

**Verification:**
```python
assert_fp_equal(result.reindex(gp.index), gp.mean())
```

### Step 2: Assign msg = 'using SeriesGroupBy.mean'

```python
msg = 'using SeriesGroupBy.mean'
```

**Verification:**
```python
assert_fp_equal(res[col], agged[col])
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, ts.index)
```

**Verification:**
```python
assert_fp_equal(res.xs(idx), agged[idx])
```

### Step 4: Assign grouped = tsframe.groupby(...)

```python
grouped = tsframe.groupby(lambda x: x.month)
```

### Step 5: Assign msg = 'using DataFrameGroupBy.mean'

```python
msg = 'using DataFrameGroupBy.mean'
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, tsframe.index)
```

### Step 7: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 8: Assign msg = 'using DataFrameGroupBy.mean'

```python
msg = 'using DataFrameGroupBy.mean'
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, tsframe.index)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.columns, tsframe.columns)
```

### Step 11: Assign result = grouped.transform(...)

```python
result = grouped.transform(np.mean)
```

### Step 12: Call assert_fp_equal()

```python
assert_fp_equal(result.reindex(gp.index), gp.mean())
```

### Step 13: Assign result = grouped.transform(...)

```python
result = grouped.transform(np.mean)
```

### Step 14: Assign agged = gp.mean(...)

```python
agged = gp.mean(axis=0)
```

### Step 15: Assign res = result.reindex(...)

```python
res = result.reindex(gp.index)
```

### Step 16: Assign grouped = tsframe.groupby(...)

```python
grouped = tsframe.groupby({'A': 0, 'B': 0, 'C': 1, 'D': 1}, axis=1)
```

### Step 17: Assign result = grouped.transform(...)

```python
result = grouped.transform(np.mean)
```

### Step 18: Assign agged = gp.mean(...)

```python
agged = gp.mean(1)
```

### Step 19: Assign res = result.reindex(...)

```python
res = result.reindex(columns=gp.columns)
```

### Step 20: Call assert_fp_equal()

```python
assert_fp_equal(res[col], agged[col])
```

### Step 21: Call assert_fp_equal()

```python
assert_fp_equal(res.xs(idx), agged[idx])
```


## Complete Example

```python
# Setup
# Fixtures: tsframe, ts

# Workflow
grouped = ts.groupby(lambda x: x.month)
msg = 'using SeriesGroupBy.mean'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = grouped.transform(np.mean)
tm.assert_index_equal(result.index, ts.index)
for _, gp in grouped:
    assert_fp_equal(result.reindex(gp.index), gp.mean())
grouped = tsframe.groupby(lambda x: x.month)
msg = 'using DataFrameGroupBy.mean'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = grouped.transform(np.mean)
tm.assert_index_equal(result.index, tsframe.index)
for _, gp in grouped:
    agged = gp.mean(axis=0)
    res = result.reindex(gp.index)
    for col in tsframe:
        assert_fp_equal(res[col], agged[col])
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    grouped = tsframe.groupby({'A': 0, 'B': 0, 'C': 1, 'D': 1}, axis=1)
msg = 'using DataFrameGroupBy.mean'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = grouped.transform(np.mean)
tm.assert_index_equal(result.index, tsframe.index)
tm.assert_index_equal(result.columns, tsframe.columns)
for _, gp in grouped:
    agged = gp.mean(1)
    res = result.reindex(columns=gp.columns)
    for idx in gp.index:
        assert_fp_equal(res.xs(idx), agged[idx])
```

## Next Steps


---

*Source: test_transform.py:152 | Complexity: Advanced | Last updated: 2026-06-02*