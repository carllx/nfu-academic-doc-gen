# How To: Setting Names From Levels Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setting names from levels raises

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_product(...)

```python
idx = MultiIndex.from_product([['a'], [1, 2]], names=['a', 'b'])
```

**Verification:**
```python
assert pd.Index._no_setting_name is False
```

### Step 2: Assign new = pd.Series(...)

```python
new = pd.Series(1, index=idx.levels[0])
```

**Verification:**
```python
assert pd.RangeIndex._no_setting_name is False
```

### Step 3: Assign unknown.name = 'foo'

```python
idx.levels[0].name = 'foo'
```

### Step 4: Assign unknown.name = 'foo'

```python
idx.levels[1].name = 'foo'
```

### Step 5: Assign new.index.name = 'bar'

```python
new.index.name = 'bar'
```


## Complete Example

```python
# Workflow
idx = MultiIndex.from_product([['a'], [1, 2]], names=['a', 'b'])
with pytest.raises(RuntimeError, match='set_names'):
    idx.levels[0].name = 'foo'
with pytest.raises(RuntimeError, match='set_names'):
    idx.levels[1].name = 'foo'
new = pd.Series(1, index=idx.levels[0])
with pytest.raises(RuntimeError, match='set_names'):
    new.index.name = 'bar'
assert pd.Index._no_setting_name is False
assert pd.RangeIndex._no_setting_name is False
```

## Next Steps


---

*Source: test_names.py:135 | Complexity: Intermediate | Last updated: 2026-06-02*