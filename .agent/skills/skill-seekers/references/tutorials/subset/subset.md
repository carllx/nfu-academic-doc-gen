# How To: Subset

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subset

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: date_range_frame
```

## Step-by-Step Guide

### Step 1: Assign N = 10

```python
N = 10
```

### Step 2: Assign df = unknown.copy.astype(...)

```python
df = date_range_frame.iloc[:N].copy().astype({'A': 'float'})
```

### Step 3: Assign unknown = value

```python
df.loc[df.index[4:8], 'A'] = np.nan
```

### Step 4: Assign dates = date_range(...)

```python
dates = date_range('1/1/1990', periods=N * 3, freq='25s')
```

### Step 5: Assign result = df.asof(...)

```python
result = df.asof(dates, subset='A')
```

### Step 6: Assign expected = df.asof(...)

```python
expected = df.asof(dates)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = df.asof(...)

```python
result = df.asof(dates, subset=['A', 'B'])
```

### Step 9: Assign expected = df.asof(...)

```python
expected = df.asof(dates)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = df.asof(...)

```python
result = df.asof(dates, subset='B')
```

### Step 12: Assign expected = df.resample.ffill.reindex(...)

```python
expected = df.resample('25s', closed='right').ffill().reindex(dates)
```

### Step 13: Assign unknown = 9

```python
expected.iloc[20:] = 9
```

### Step 14: Assign unknown = unknown.astype(...)

```python
expected['B'] = expected['B'].astype(df['B'].dtype)
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: date_range_frame

# Workflow
N = 10
df = date_range_frame.iloc[:N].copy().astype({'A': 'float'})
df.loc[df.index[4:8], 'A'] = np.nan
dates = date_range('1/1/1990', periods=N * 3, freq='25s')
result = df.asof(dates, subset='A')
expected = df.asof(dates)
tm.assert_frame_equal(result, expected)
result = df.asof(dates, subset=['A', 'B'])
expected = df.asof(dates)
tm.assert_frame_equal(result, expected)
result = df.asof(dates, subset='B')
expected = df.resample('25s', closed='right').ffill().reindex(dates)
expected.iloc[20:] = 9
expected['B'] = expected['B'].astype(df['B'].dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_asof.py:52 | Complexity: Advanced | Last updated: 2026-06-02*