# How To: Logical Ops Int Frame

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test logical ops int frame

## Prerequisites

**Required Modules:**
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1a_int = DataFrame(...)

```python
df1a_int = DataFrame(1, index=[1], columns=['A'])
```

### Step 2: Assign df1a_bool = DataFrame(...)

```python
df1a_bool = DataFrame(True, index=[1], columns=['A'])
```

### Step 3: Assign result = value

```python
result = df1a_int | df1a_bool
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df1a_bool)
```

### Step 5: Assign res_ser = value

```python
res_ser = df1a_int['A'] | df1a_bool['A']
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res_ser, df1a_bool['A'])
```


## Complete Example

```python
# Workflow
df1a_int = DataFrame(1, index=[1], columns=['A'])
df1a_bool = DataFrame(True, index=[1], columns=['A'])
result = df1a_int | df1a_bool
tm.assert_frame_equal(result, df1a_bool)
res_ser = df1a_int['A'] | df1a_bool['A']
tm.assert_series_equal(res_ser, df1a_bool['A'])
```

## Next Steps


---

*Source: test_logical_ops.py:87 | Complexity: Intermediate | Last updated: 2026-06-02*