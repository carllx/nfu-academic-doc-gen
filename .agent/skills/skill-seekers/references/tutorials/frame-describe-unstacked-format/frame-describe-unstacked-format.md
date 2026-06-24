# How To: Frame Describe Unstacked Format

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame describe unstacked format

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign prices = value

```python
prices = {Timestamp('2011-01-06 10:59:05', tz=None): 24990, Timestamp('2011-01-06 12:43:33', tz=None): 25499, Timestamp('2011-01-06 12:54:09', tz=None): 25499}
```

### Step 2: Assign volumes = value

```python
volumes = {Timestamp('2011-01-06 10:59:05', tz=None): 1500000000, Timestamp('2011-01-06 12:43:33', tz=None): 5000000000, Timestamp('2011-01-06 12:54:09', tz=None): 100000000}
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'PRICE': prices, 'VOLUME': volumes})
```

### Step 4: Assign result = df.groupby.VOLUME.describe(...)

```python
result = df.groupby('PRICE').VOLUME.describe()
```

### Step 5: Assign data = value

```python
data = [df[df.PRICE == 24990].VOLUME.describe().values.tolist(), df[df.PRICE == 25499].VOLUME.describe().values.tolist()]
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame(data, index=Index([24990, 25499], name='PRICE'), columns=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
prices = {Timestamp('2011-01-06 10:59:05', tz=None): 24990, Timestamp('2011-01-06 12:43:33', tz=None): 25499, Timestamp('2011-01-06 12:54:09', tz=None): 25499}
volumes = {Timestamp('2011-01-06 10:59:05', tz=None): 1500000000, Timestamp('2011-01-06 12:43:33', tz=None): 5000000000, Timestamp('2011-01-06 12:54:09', tz=None): 100000000}
df = DataFrame({'PRICE': prices, 'VOLUME': volumes})
result = df.groupby('PRICE').VOLUME.describe()
data = [df[df.PRICE == 24990].VOLUME.describe().values.tolist(), df[df.PRICE == 25499].VOLUME.describe().values.tolist()]
expected = DataFrame(data, index=Index([24990, 25499], name='PRICE'), columns=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:125 | Complexity: Intermediate | Last updated: 2026-06-02*