# How To: Grouper Groups

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test grouper groups

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': 1})
```

**Verification:**
```python
assert res is gb.groups
```

### Step 2: Assign grper = Grouper(...)

```python
grper = Grouper(key='a')
```

**Verification:**
```python
assert res is gb._grouper
```

### Step 3: Assign gb = df.groupby(...)

```python
gb = df.groupby(grper)
```

**Verification:**
```python
assert res is gb.obj
```

### Step 4: Assign msg = 'Use GroupBy.groups instead'

```python
msg = 'Use GroupBy.groups instead'
```

**Verification:**
```python
assert res is gb.groups
```

### Step 5: Assign msg = 'Use GroupBy.grouper instead'

```python
msg = 'Use GroupBy.grouper instead'
```

**Verification:**
```python
assert res is gb._grouper
```

### Step 6: Assign msg = 'Grouper.obj is deprecated and will be removed'

```python
msg = 'Grouper.obj is deprecated and will be removed'
```

**Verification:**
```python
assert res is gb.obj
```

### Step 7: Assign msg = 'Use Resampler.ax instead'

```python
msg = 'Use Resampler.ax instead'
```

### Step 8: Assign msg = 'Grouper.indexer is deprecated'

```python
msg = 'Grouper.indexer is deprecated'
```

### Step 9: Assign res = value

```python
res = grper.groups
```

### Step 10: Assign res = value

```python
res = grper.grouper
```

### Step 11: Assign res = value

```python
res = grper.obj
```

### Step 12: grper.ax

```python
grper.ax
```

### Step 13: grper.indexer

```python
grper.indexer
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': 1})
grper = Grouper(key='a')
gb = df.groupby(grper)
msg = 'Use GroupBy.groups instead'
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = grper.groups
assert res is gb.groups
msg = 'Use GroupBy.grouper instead'
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = grper.grouper
assert res is gb._grouper
msg = 'Grouper.obj is deprecated and will be removed'
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = grper.obj
assert res is gb.obj
msg = 'Use Resampler.ax instead'
with tm.assert_produces_warning(FutureWarning, match=msg):
    grper.ax
msg = 'Grouper.indexer is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    grper.indexer
```

## Next Steps


---

*Source: test_grouping.py:1201 | Complexity: Advanced | Last updated: 2026-06-02*