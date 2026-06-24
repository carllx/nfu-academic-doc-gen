# How To: To Period Invalid Axis

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to period invalid axis

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dr = date_range(...)

```python
dr = date_range('1/1/2000', '1/1/2001')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((len(dr), 5)), index=dr)
```

### Step 3: Assign unknown = 'a'

```python
df['mix'] = 'a'
```

### Step 4: Assign msg = 'No axis named 2 for object type DataFrame'

```python
msg = 'No axis named 2 for object type DataFrame'
```

### Step 5: Call df.to_period()

```python
df.to_period(axis=2)
```


## Complete Example

```python
# Workflow
dr = date_range('1/1/2000', '1/1/2001')
df = DataFrame(np.random.default_rng(2).standard_normal((len(dr), 5)), index=dr)
df['mix'] = 'a'
msg = 'No axis named 2 for object type DataFrame'
with pytest.raises(ValueError, match=msg):
    df.to_period(axis=2)
```

## Next Steps


---

*Source: test_to_period.py:71 | Complexity: Intermediate | Last updated: 2026-06-02*