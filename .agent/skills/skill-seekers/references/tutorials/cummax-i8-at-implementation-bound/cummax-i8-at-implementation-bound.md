# How To: Cummax I8 At Implementation Bound

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cummax i8 at implementation bound

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([pd.NaT._value + n for n in range(5)])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': 1, 'B': ser, 'C': ser._values.view('M8[ns]')})
```

### Step 3: Assign gb = df.groupby(...)

```python
gb = df.groupby('A')
```

### Step 4: Assign res = gb.cummax(...)

```python
res = gb.cummax()
```

### Step 5: Assign exp = value

```python
exp = df[['B', 'C']]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```


## Complete Example

```python
# Workflow
ser = Series([pd.NaT._value + n for n in range(5)])
df = DataFrame({'A': 1, 'B': ser, 'C': ser._values.view('M8[ns]')})
gb = df.groupby('A')
res = gb.cummax()
exp = df[['B', 'C']]
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_cumulative.py:216 | Complexity: Intermediate | Last updated: 2026-06-02*