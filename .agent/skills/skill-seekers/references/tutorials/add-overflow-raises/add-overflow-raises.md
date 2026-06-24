# How To: Add Overflow Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add overflow raises

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign per = Timestamp.max.to_period(...)

```python
per = Timestamp.max.to_period('ns')
```

### Step 2: Assign msg = unknown.join(...)

```python
msg = '|'.join(['Python int too large to convert to C long', 'int too big to convert'])
```

### Step 3: Assign msg = 'value too large'

```python
msg = 'value too large'
```

### Step 4: per + 1

```python
per + 1
```

### Step 5: per + Timedelta(1)

```python
per + Timedelta(1)
```

### Step 6: per + offsets.Nano(1)

```python
per + offsets.Nano(1)
```


## Complete Example

```python
# Workflow
per = Timestamp.max.to_period('ns')
msg = '|'.join(['Python int too large to convert to C long', 'int too big to convert'])
with pytest.raises(OverflowError, match=msg):
    per + 1
msg = 'value too large'
with pytest.raises(OverflowError, match=msg):
    per + Timedelta(1)
with pytest.raises(OverflowError, match=msg):
    per + offsets.Nano(1)
```

## Next Steps


---

*Source: test_arithmetic.py:18 | Complexity: Intermediate | Last updated: 2026-06-02*