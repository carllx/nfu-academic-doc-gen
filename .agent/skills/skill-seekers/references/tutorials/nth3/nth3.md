# How To: Nth3

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nth3

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).integers(1, 10, (100, 2)), dtype='int64')
```

**Verification:**
```python
assert expected.name == 1
```

### Step 2: Assign ser = value

```python
ser = df[1]
```

**Verification:**
```python
assert expected2.name == 1
```

### Step 3: Assign gb = value

```python
gb = df[0]
```

**Verification:**
```python
assert expected.iloc[0] == v
```

### Step 4: Assign expected = ser.groupby.first(...)

```python
expected = ser.groupby(gb).first()
```

**Verification:**
```python
assert expected2.iloc[0] == v
```

### Step 5: Assign expected2 = ser.groupby.apply(...)

```python
expected2 = ser.groupby(gb).apply(lambda x: x.iloc[0])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected2, expected, check_names=False)
```

**Verification:**
```python
assert expected.name == 1
```

### Step 7: Assign v = value

```python
v = ser[gb == 1].iloc[0]
```

**Verification:**
```python
assert expected.iloc[0] == v
```

### Step 8: Call ser.groupby.nth()

```python
ser.groupby(gb, sort=False).nth(0, dropna=True)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).integers(1, 10, (100, 2)), dtype='int64')
ser = df[1]
gb = df[0]
expected = ser.groupby(gb).first()
expected2 = ser.groupby(gb).apply(lambda x: x.iloc[0])
tm.assert_series_equal(expected2, expected, check_names=False)
assert expected.name == 1
assert expected2.name == 1
v = ser[gb == 1].iloc[0]
assert expected.iloc[0] == v
assert expected2.iloc[0] == v
with pytest.raises(ValueError, match='For a DataFrame'):
    ser.groupby(gb, sort=False).nth(0, dropna=True)
```

## Next Steps


---

*Source: test_nth.py:253 | Complexity: Advanced | Last updated: 2026-06-02*