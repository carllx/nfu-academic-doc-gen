# How To: Multinomial Pvals Float32

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multinomial pvals float32

## Prerequisites

**Required Modules:**
- `hashlib`
- `os.path`
- `sys`
- `warnings`
- `pytest`
- `numpy`
- `numpy.exceptions`
- `numpy.linalg`
- `numpy.random`
- `numpy.testing`
- `pickle`
- `gzip`
- `pickle`
- `threading`


## Step-by-Step Guide

### Step 1: Assign x = np.array(...)

```python
x = np.array([0.99, 0.99, 1e-09, 1e-09, 1e-09, 1e-09, 1e-09, 1e-09, 1e-09, 1e-09], dtype=np.float32)
```

### Step 2: Assign pvals = value

```python
pvals = x / x.sum()
```

### Step 3: Assign random = Generator(...)

```python
random = Generator(MT19937(1432985819))
```

### Step 4: Assign match = '[\\w\\s]*pvals array is cast to 64-bit floating'

```python
match = '[\\w\\s]*pvals array is cast to 64-bit floating'
```

### Step 5: Call random.multinomial()

```python
random.multinomial(1, pvals)
```


## Complete Example

```python
# Workflow
x = np.array([0.99, 0.99, 1e-09, 1e-09, 1e-09, 1e-09, 1e-09, 1e-09, 1e-09, 1e-09], dtype=np.float32)
pvals = x / x.sum()
random = Generator(MT19937(1432985819))
match = '[\\w\\s]*pvals array is cast to 64-bit floating'
with pytest.raises(ValueError, match=match):
    random.multinomial(1, pvals)
```

## Next Steps


---

*Source: test_generator_mt19937.py:166 | Complexity: Intermediate | Last updated: 2026-06-02*