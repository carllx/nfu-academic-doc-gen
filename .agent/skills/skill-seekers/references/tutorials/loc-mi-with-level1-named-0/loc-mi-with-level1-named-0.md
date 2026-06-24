# How To: Loc Mi With Level1 Named 0

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc mi with level1 named 0

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('2016-01-01', periods=3, tz='US/Pacific')
```

**Verification:**
```python
assert df2.index.names == (None, 0)
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(range(3), index=dti)
```

**Verification:**
```python
assert ser2.index.names == (None, 0)
```

### Step 3: Assign df = ser.to_frame(...)

```python
df = ser.to_frame()
```

### Step 4: Assign unknown = dti

```python
df[1] = dti
```

### Step 5: Assign df2 = df.set_index(...)

```python
df2 = df.set_index(0, append=True)
```

**Verification:**
```python
assert df2.index.names == (None, 0)
```

### Step 6: Call df2.index.get_loc()

```python
df2.index.get_loc(dti[0])
```

### Step 7: Assign result = value

```python
result = df2.loc[dti[0]]
```

### Step 8: Assign expected = unknown.droplevel(...)

```python
expected = df2.iloc[[0]].droplevel(None)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign ser2 = value

```python
ser2 = df2[1]
```

**Verification:**
```python
assert ser2.index.names == (None, 0)
```

### Step 11: Assign result = value

```python
result = ser2.loc[dti[0]]
```

### Step 12: Assign expected = unknown.droplevel(...)

```python
expected = ser2.iloc[[0]].droplevel(None)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
dti = pd.date_range('2016-01-01', periods=3, tz='US/Pacific')
ser = Series(range(3), index=dti)
df = ser.to_frame()
df[1] = dti
df2 = df.set_index(0, append=True)
assert df2.index.names == (None, 0)
df2.index.get_loc(dti[0])
result = df2.loc[dti[0]]
expected = df2.iloc[[0]].droplevel(None)
tm.assert_frame_equal(result, expected)
ser2 = df2[1]
assert ser2.index.names == (None, 0)
result = ser2.loc[dti[0]]
expected = ser2.iloc[[0]].droplevel(None)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_loc.py:689 | Complexity: Advanced | Last updated: 2026-06-02*