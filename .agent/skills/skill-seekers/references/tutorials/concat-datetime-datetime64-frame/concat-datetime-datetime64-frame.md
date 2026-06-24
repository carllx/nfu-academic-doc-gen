# How To: Concat Datetime Datetime64 Frame

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat datetime datetime64 frame

## Prerequisites

**Required Modules:**
- `datetime`
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rows = value

```python
rows = []
```

### Step 2: Call rows.append()

```python
rows.append([datetime(2010, 1, 1), 1])
```

### Step 3: Call rows.append()

```python
rows.append([datetime(2010, 1, 2), 'hi'])
```

### Step 4: Assign df2_obj = DataFrame.from_records(...)

```python
df2_obj = DataFrame.from_records(rows, columns=['date', 'test'])
```

### Step 5: Assign ind = date_range(...)

```python
ind = date_range(start='2000/1/1', freq='D', periods=10)
```

### Step 6: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'date': ind, 'test': range(10)})
```

### Step 7: Call concat()

```python
concat([df1, df2_obj])
```


## Complete Example

```python
# Workflow
rows = []
rows.append([datetime(2010, 1, 1), 1])
rows.append([datetime(2010, 1, 2), 'hi'])
df2_obj = DataFrame.from_records(rows, columns=['date', 'test'])
ind = date_range(start='2000/1/1', freq='D', periods=10)
df1 = DataFrame({'date': ind, 'test': range(10)})
concat([df1, df2_obj])
```

## Next Steps


---

*Source: test_datetimes.py:33 | Complexity: Intermediate | Last updated: 2026-06-02*