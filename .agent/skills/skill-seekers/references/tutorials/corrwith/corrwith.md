# How To: Corrwith

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test corrwith

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_frame, dtype
```

## Step-by-Step Guide

### Step 1: Assign datetime_frame = datetime_frame.astype(...)

```python
datetime_frame = datetime_frame.astype(dtype)
```

**Verification:**
```python
assert 'B' not in dropped
```

### Step 2: Assign a = datetime_frame

```python
a = datetime_frame
```

**Verification:**
```python
assert a.index[-1] not in dropped.index
```

### Step 3: Assign noise = Series(...)

```python
noise = Series(np.random.default_rng(2).standard_normal(len(a)), index=a.index)
```

### Step 4: Assign b = datetime_frame.add(...)

```python
b = datetime_frame.add(noise, axis=0)
```

### Step 5: Assign b = b.reindex(...)

```python
b = b.reindex(columns=b.columns[::-1], index=b.index[::-1][10:])
```

### Step 6: Assign colcorr = a.corrwith(...)

```python
colcorr = a.corrwith(b, axis=0)
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(colcorr['A'], a['A'].corr(b['A']))
```

### Step 8: Assign rowcorr = a.corrwith(...)

```python
rowcorr = a.corrwith(b, axis=1)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rowcorr, a.T.corrwith(b.T, axis=0))
```

### Step 10: Assign dropped = a.corrwith(...)

```python
dropped = a.corrwith(b, axis=0, drop=True)
```

### Step 11: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(dropped['A'], a['A'].corr(b['A']))
```

**Verification:**
```python
assert 'B' not in dropped
```

### Step 12: Assign dropped = a.corrwith(...)

```python
dropped = a.corrwith(b, axis=1, drop=True)
```

**Verification:**
```python
assert a.index[-1] not in dropped.index
```

### Step 13: Assign index = value

```python
index = ['a', 'b', 'c', 'd', 'e']
```

### Step 14: Assign columns = value

```python
columns = ['one', 'two', 'three', 'four']
```

### Step 15: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(np.random.default_rng(2).standard_normal((5, 4)), index=index, columns=columns)
```

### Step 16: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), index=index[:4], columns=columns)
```

### Step 17: Assign correls = df1.corrwith(...)

```python
correls = df1.corrwith(df2, axis=1)
```

### Step 18: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(correls[row], df1.loc[row].corr(df2.loc[row]))
```


## Complete Example

```python
# Setup
# Fixtures: datetime_frame, dtype

# Workflow
datetime_frame = datetime_frame.astype(dtype)
a = datetime_frame
noise = Series(np.random.default_rng(2).standard_normal(len(a)), index=a.index)
b = datetime_frame.add(noise, axis=0)
b = b.reindex(columns=b.columns[::-1], index=b.index[::-1][10:])
del b['B']
colcorr = a.corrwith(b, axis=0)
tm.assert_almost_equal(colcorr['A'], a['A'].corr(b['A']))
rowcorr = a.corrwith(b, axis=1)
tm.assert_series_equal(rowcorr, a.T.corrwith(b.T, axis=0))
dropped = a.corrwith(b, axis=0, drop=True)
tm.assert_almost_equal(dropped['A'], a['A'].corr(b['A']))
assert 'B' not in dropped
dropped = a.corrwith(b, axis=1, drop=True)
assert a.index[-1] not in dropped.index
index = ['a', 'b', 'c', 'd', 'e']
columns = ['one', 'two', 'three', 'four']
df1 = DataFrame(np.random.default_rng(2).standard_normal((5, 4)), index=index, columns=columns)
df2 = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), index=index[:4], columns=columns)
correls = df1.corrwith(df2, axis=1)
for row in index[:4]:
    tm.assert_almost_equal(correls[row], df1.loc[row].corr(df2.loc[row]))
```

## Next Steps


---

*Source: test_cov_corr.py:287 | Complexity: Advanced | Last updated: 2026-06-02*