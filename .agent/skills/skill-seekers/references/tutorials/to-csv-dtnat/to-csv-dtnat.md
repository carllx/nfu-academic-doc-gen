# How To: To Csv Dtnat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to csv dtnat

## Prerequisites

**Required Modules:**
- `csv`
- `io`
- `os`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.common`
- `pandas.io.common`


## Step-by-Step Guide

### Step 1: Assign chunksize = 1000

```python
chunksize = 1000
```

### Step 2: Assign s1 = make_dtnat_arr(...)

```python
s1 = make_dtnat_arr(chunksize + 5)
```

### Step 3: Assign s2 = make_dtnat_arr(...)

```python
s2 = make_dtnat_arr(chunksize + 5, 0)
```

### Step 4: Assign s = list(...)

```python
s = list(date_range('2000', freq='5min', periods=n))
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'a': s1, 'b': s2})
```

### Step 6: Call df.to_csv()

```python
df.to_csv(pth, chunksize=chunksize)
```

### Step 7: Assign recons = self.read_csv.apply(...)

```python
recons = self.read_csv(pth).apply(to_datetime)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, recons, check_names=False)
```

### Step 9: Assign nnat = int(...)

```python
nnat = int(n * 0.1)
```

### Step 10: Assign i = np.random.default_rng.integers(...)

```python
i = np.random.default_rng(2).integers(100)
```

### Step 11: Assign unknown = NaT

```python
s[-i] = NaT
```

### Step 12: Assign unknown = NaT

```python
s[i] = NaT
```

### Step 13: Assign unknown = NaT

```python
s[i] = NaT
```


## Complete Example

```python
# Workflow
def make_dtnat_arr(n, nnat=None):
    if nnat is None:
        nnat = int(n * 0.1)
    s = list(date_range('2000', freq='5min', periods=n))
    if nnat:
        for i in np.random.default_rng(2).integers(0, len(s), nnat):
            s[i] = NaT
        i = np.random.default_rng(2).integers(100)
        s[-i] = NaT
        s[i] = NaT
    return s
chunksize = 1000
s1 = make_dtnat_arr(chunksize + 5)
s2 = make_dtnat_arr(chunksize + 5, 0)
with tm.ensure_clean('1.csv') as pth:
    df = DataFrame({'a': s1, 'b': s2})
    df.to_csv(pth, chunksize=chunksize)
    recons = self.read_csv(pth).apply(to_datetime)
    tm.assert_frame_equal(df, recons, check_names=False)
```

## Next Steps


---

*Source: test_to_csv.py:211 | Complexity: Advanced | Last updated: 2026-06-02*