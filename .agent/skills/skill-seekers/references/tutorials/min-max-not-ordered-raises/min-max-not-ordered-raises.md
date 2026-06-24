# How To: Min Max Not Ordered Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test min max not ordered raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `sys`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: aggregation
```

## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'c', 'd'], ordered=False)
```

### Step 2: Assign msg = value

```python
msg = f'Categorical is not ordered for operation {aggregation}'
```

### Step 3: Assign agg_func = getattr(...)

```python
agg_func = getattr(cat, aggregation)
```

### Step 4: Assign ufunc = value

```python
ufunc = np.minimum if aggregation == 'min' else np.maximum
```

### Step 5: Call agg_func()

```python
agg_func()
```

### Step 6: Call ufunc.reduce()

```python
ufunc.reduce(cat)
```


## Complete Example

```python
# Setup
# Fixtures: aggregation

# Workflow
cat = Categorical(['a', 'b', 'c', 'd'], ordered=False)
msg = f'Categorical is not ordered for operation {aggregation}'
agg_func = getattr(cat, aggregation)
with pytest.raises(TypeError, match=msg):
    agg_func()
ufunc = np.minimum if aggregation == 'min' else np.maximum
with pytest.raises(TypeError, match=msg):
    ufunc.reduce(cat)
```

## Next Steps


---

*Source: test_analytics.py:24 | Complexity: Intermediate | Last updated: 2026-06-02*