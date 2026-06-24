# How To: Get Loc Mismatched Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get loc mismatched freq

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=3)
```

### Step 2: Assign pi = dti.to_period(...)

```python
pi = dti.to_period('D')
```

### Step 3: Assign pi2 = dti.to_period(...)

```python
pi2 = dti.to_period('W')
```

### Step 4: Assign pi3 = pi.view(...)

```python
pi3 = pi.view(pi2.dtype)
```

### Step 5: Call pi.get_loc()

```python
pi.get_loc(pi2[0])
```

### Step 6: Call pi.get_loc()

```python
pi.get_loc(pi3[0])
```


## Complete Example

```python
# Workflow
dti = date_range('2016-01-01', periods=3)
pi = dti.to_period('D')
pi2 = dti.to_period('W')
pi3 = pi.view(pi2.dtype)
with pytest.raises(KeyError, match='W-SUN'):
    pi.get_loc(pi2[0])
with pytest.raises(KeyError, match='W-SUN'):
    pi.get_loc(pi3[0])
```

## Next Steps


---

*Source: test_indexing.py:346 | Complexity: Intermediate | Last updated: 2026-06-02*