# How To: Single Level Drop Partially Missing Elements

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test single level drop partially missing elements

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([(1, 2), (2, 2), (3, 2)])
```

### Step 2: Assign msg = 'labels \\[4\\] not found in level'

```python
msg = 'labels \\[4\\] not found in level'
```

### Step 3: Assign msg = 'labels \\[nan\\] not found in level'

```python
msg = 'labels \\[nan\\] not found in level'
```

### Step 4: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([(np.nan, 1), (1, 2)])
```

### Step 5: Assign msg = "labels \\['a'\\] not found in level"

```python
msg = "labels \\['a'\\] not found in level"
```

### Step 6: Call mi.drop()

```python
mi.drop(4, level=0)
```

### Step 7: Call mi.drop()

```python
mi.drop([1, 4], level=0)
```

### Step 8: Call mi.drop()

```python
mi.drop([np.nan], level=0)
```

### Step 9: Call mi.drop()

```python
mi.drop([np.nan, 1, 2, 3], level=0)
```

### Step 10: Call mi.drop()

```python
mi.drop([np.nan, 1, 'a'], level=0)
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_tuples([(1, 2), (2, 2), (3, 2)])
msg = 'labels \\[4\\] not found in level'
with pytest.raises(KeyError, match=msg):
    mi.drop(4, level=0)
with pytest.raises(KeyError, match=msg):
    mi.drop([1, 4], level=0)
msg = 'labels \\[nan\\] not found in level'
with pytest.raises(KeyError, match=msg):
    mi.drop([np.nan], level=0)
with pytest.raises(KeyError, match=msg):
    mi.drop([np.nan, 1, 2, 3], level=0)
mi = MultiIndex.from_tuples([(np.nan, 1), (1, 2)])
msg = "labels \\['a'\\] not found in level"
with pytest.raises(KeyError, match=msg):
    mi.drop([np.nan, 1, 'a'], level=0)
```

## Next Steps


---

*Source: test_drop.py:164 | Complexity: Advanced | Last updated: 2026-06-02*