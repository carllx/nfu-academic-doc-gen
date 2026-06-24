# How To: Sample Inf Weights

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sample inf weights

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: obj
```

## Step-by-Step Guide

### Step 1: Assign weights_with_inf = value

```python
weights_with_inf = [0.1] * 10
```

### Step 2: Assign unknown = value

```python
weights_with_inf[0] = np.inf
```

### Step 3: Assign msg = 'weight vector may not include `inf` values'

```python
msg = 'weight vector may not include `inf` values'
```

### Step 4: Assign weights_with_ninf = value

```python
weights_with_ninf = [0.1] * 10
```

### Step 5: Assign unknown = value

```python
weights_with_ninf[0] = -np.inf
```

### Step 6: Call obj.sample()

```python
obj.sample(n=3, weights=weights_with_inf)
```

### Step 7: Call obj.sample()

```python
obj.sample(n=3, weights=weights_with_ninf)
```


## Complete Example

```python
# Setup
# Fixtures: obj

# Workflow
weights_with_inf = [0.1] * 10
weights_with_inf[0] = np.inf
msg = 'weight vector may not include `inf` values'
with pytest.raises(ValueError, match=msg):
    obj.sample(n=3, weights=weights_with_inf)
weights_with_ninf = [0.1] * 10
weights_with_ninf[0] = -np.inf
with pytest.raises(ValueError, match=msg):
    obj.sample(n=3, weights=weights_with_ninf)
```

## Next Steps


---

*Source: test_sample.py:128 | Complexity: Intermediate | Last updated: 2026-06-02*