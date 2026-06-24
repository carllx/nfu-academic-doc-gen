# How To: Pass Args Kwargs Duplicate Columns

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test pass args kwargs duplicate columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: tsframe, as_index
```

## Step-by-Step Guide

### Step 1: Assign tsframe.columns = value

```python
tsframe.columns = ['A', 'B', 'A', 'C']
```

### Step 2: Assign gb = tsframe.groupby(...)

```python
gb = tsframe.groupby(lambda x: x.month, as_index=as_index)
```

### Step 3: Assign warn = value

```python
warn = None if as_index else FutureWarning
```

### Step 4: Assign msg = 'A grouping .* was excluded from the result'

```python
msg = 'A grouping .* was excluded from the result'
```

### Step 5: Assign ex_data = value

```python
ex_data = {1: tsframe[tsframe.index.month == 1].quantile(0.8), 2: tsframe[tsframe.index.month == 2].quantile(0.8)}
```

### Step 6: Assign expected = value

```python
expected = DataFrame(ex_data).T
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```

### Step 8: Assign res = gb.agg(...)

```python
res = gb.agg(np.percentile, 80, axis=0)
```

### Step 9: Assign expected.index = Index(...)

```python
expected.index = Index(range(2))
```


## Complete Example

```python
# Setup
# Fixtures: tsframe, as_index

# Workflow
tsframe.columns = ['A', 'B', 'A', 'C']
gb = tsframe.groupby(lambda x: x.month, as_index=as_index)
warn = None if as_index else FutureWarning
msg = 'A grouping .* was excluded from the result'
with tm.assert_produces_warning(warn, match=msg):
    res = gb.agg(np.percentile, 80, axis=0)
ex_data = {1: tsframe[tsframe.index.month == 1].quantile(0.8), 2: tsframe[tsframe.index.month == 2].quantile(0.8)}
expected = DataFrame(ex_data).T
if not as_index:
    expected.index = Index(range(2))
tm.assert_frame_equal(res, expected)
```

## Next Steps


---

*Source: test_groupby.py:297 | Complexity: Advanced | Last updated: 2026-06-02*