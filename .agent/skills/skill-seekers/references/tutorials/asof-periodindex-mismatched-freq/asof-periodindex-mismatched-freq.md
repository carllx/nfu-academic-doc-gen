# How To: Asof Periodindex Mismatched Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asof periodindex mismatched freq

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign N = 50

```python
N = 50
```

### Step 2: Assign rng = period_range(...)

```python
rng = period_range('1/1/1990', periods=N, freq='h')
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal(N), index=rng)
```

### Step 4: Assign msg = 'Input has different freq'

```python
msg = 'Input has different freq'
```

### Step 5: Call df.asof()

```python
df.asof(rng.asfreq('D'))
```


## Complete Example

```python
# Workflow
N = 50
rng = period_range('1/1/1990', periods=N, freq='h')
df = DataFrame(np.random.default_rng(2).standard_normal(N), index=rng)
msg = 'Input has different freq'
with pytest.raises(IncompatibleFrequency, match=msg):
    df.asof(rng.asfreq('D'))
```

## Next Steps


---

*Source: test_asof.py:179 | Complexity: Intermediate | Last updated: 2026-06-02*