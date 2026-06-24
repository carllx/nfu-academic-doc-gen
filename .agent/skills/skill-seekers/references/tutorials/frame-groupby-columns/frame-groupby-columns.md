# How To: Frame Groupby Columns

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame groupby columns

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
# Fixtures: tsframe
```

## Step-by-Step Guide

### Step 1: Assign mapping = value

```python
mapping = {'A': 0, 'B': 0, 'C': 1, 'D': 1}
```

**Verification:**
```python
assert len(aggregated) == len(tsframe)
```

### Step 2: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

**Verification:**
```python
assert len(aggregated.columns) == 2
```

### Step 3: Assign aggregated = grouped.aggregate(...)

```python
aggregated = grouped.aggregate('mean')
```

**Verification:**
```python
assert len(v.columns) == 2
```

### Step 4: Assign tf = value

```python
tf = lambda x: x - x.mean()
```

### Step 5: Assign msg = "The 'axis' keyword in DataFrame.groupby is deprecated"

```python
msg = "The 'axis' keyword in DataFrame.groupby is deprecated"
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(groupedT.transform(tf).T, grouped.transform(tf))
```

### Step 7: Assign grouped = tsframe.groupby(...)

```python
grouped = tsframe.groupby(mapping, axis=1)
```

### Step 8: Assign groupedT = tsframe.T.groupby(...)

```python
groupedT = tsframe.T.groupby(mapping, axis=0)
```

**Verification:**
```python
assert len(v.columns) == 2
```


## Complete Example

```python
# Setup
# Fixtures: tsframe

# Workflow
mapping = {'A': 0, 'B': 0, 'C': 1, 'D': 1}
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    grouped = tsframe.groupby(mapping, axis=1)
aggregated = grouped.aggregate('mean')
assert len(aggregated) == len(tsframe)
assert len(aggregated.columns) == 2
tf = lambda x: x - x.mean()
msg = "The 'axis' keyword in DataFrame.groupby is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    groupedT = tsframe.T.groupby(mapping, axis=0)
tm.assert_frame_equal(groupedT.transform(tf).T, grouped.transform(tf))
for k, v in grouped:
    assert len(v.columns) == 2
```

## Next Steps


---

*Source: test_groupby.py:507 | Complexity: Advanced | Last updated: 2026-06-02*