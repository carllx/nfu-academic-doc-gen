# How To: Between Time Incorrect Arg Inclusive

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test between time incorrect arg inclusive

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000', '1/5/2000', freq='5min')
```

### Step 2: Assign ts = DataFrame(...)

```python
ts = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 2)), index=rng)
```

### Step 3: Assign stime = time(...)

```python
stime = time(0, 0)
```

### Step 4: Assign etime = time(...)

```python
etime = time(1, 0)
```

### Step 5: Assign inclusive = 'bad_string'

```python
inclusive = 'bad_string'
```

### Step 6: Assign msg = "Inclusive has to be either 'both', 'neither', 'left' or 'right'"

```python
msg = "Inclusive has to be either 'both', 'neither', 'left' or 'right'"
```

### Step 7: Call ts.between_time()

```python
ts.between_time(stime, etime, inclusive=inclusive)
```


## Complete Example

```python
# Workflow
rng = date_range('1/1/2000', '1/5/2000', freq='5min')
ts = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 2)), index=rng)
stime = time(0, 0)
etime = time(1, 0)
inclusive = 'bad_string'
msg = "Inclusive has to be either 'both', 'neither', 'left' or 'right'"
with pytest.raises(ValueError, match=msg):
    ts.between_time(stime, etime, inclusive=inclusive)
```

## Next Steps


---

*Source: test_between_time.py:215 | Complexity: Intermediate | Last updated: 2026-06-02*