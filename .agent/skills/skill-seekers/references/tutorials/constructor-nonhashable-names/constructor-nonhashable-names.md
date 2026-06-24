# How To: Constructor Nonhashable Names

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor nonhashable names

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign levels = value

```python
levels = [[1, 2], ['one', 'two']]
```

### Step 2: Assign codes = value

```python
codes = [[0, 0, 1, 1], [0, 1, 0, 1]]
```

### Step 3: Assign names = value

```python
names = (['foo'], ['bar'])
```

### Step 4: Assign msg = 'MultiIndex\\.name must be a hashable type'

```python
msg = 'MultiIndex\\.name must be a hashable type'
```

### Step 5: Assign mi = MultiIndex(...)

```python
mi = MultiIndex(levels=[[1, 2], ['one', 'two']], codes=[[0, 0, 1, 1], [0, 1, 0, 1]], names=('foo', 'bar'))
```

### Step 6: Assign renamed = value

```python
renamed = [['fooo'], ['barr']]
```

### Step 7: Call MultiIndex()

```python
MultiIndex(levels=levels, codes=codes, names=names)
```

### Step 8: Call mi.rename()

```python
mi.rename(names=renamed)
```

### Step 9: Call mi.set_names()

```python
mi.set_names(names=renamed)
```


## Complete Example

```python
# Workflow
levels = [[1, 2], ['one', 'two']]
codes = [[0, 0, 1, 1], [0, 1, 0, 1]]
names = (['foo'], ['bar'])
msg = 'MultiIndex\\.name must be a hashable type'
with pytest.raises(TypeError, match=msg):
    MultiIndex(levels=levels, codes=codes, names=names)
mi = MultiIndex(levels=[[1, 2], ['one', 'two']], codes=[[0, 0, 1, 1], [0, 1, 0, 1]], names=('foo', 'bar'))
renamed = [['fooo'], ['barr']]
with pytest.raises(TypeError, match=msg):
    mi.rename(names=renamed)
with pytest.raises(TypeError, match=msg):
    mi.set_names(names=renamed)
```

## Next Steps


---

*Source: test_constructors.py:45 | Complexity: Advanced | Last updated: 2026-06-02*