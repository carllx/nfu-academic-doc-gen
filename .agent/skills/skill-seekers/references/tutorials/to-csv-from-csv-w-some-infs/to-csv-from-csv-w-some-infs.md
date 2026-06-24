# How To: To Csv From Csv W Some Infs

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to csv from csv w some infs

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
float_frame['G'] = np.nan
```

### Step 2: Assign f = value

```python
f = lambda x: [np.inf, np.nan][np.random.default_rng(2).random() < 0.5]
```

### Step 3: Assign unknown = float_frame.index.map(...)

```python
float_frame['h'] = float_frame.index.map(f)
```

### Step 4: Call float_frame.to_csv()

```python
float_frame.to_csv(path)
```

### Step 5: Assign recons = self.read_csv(...)

```python
recons = self.read_csv(path)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(float_frame, recons)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(np.isinf(float_frame), np.isinf(recons))
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
float_frame['G'] = np.nan
f = lambda x: [np.inf, np.nan][np.random.default_rng(2).random() < 0.5]
float_frame['h'] = float_frame.index.map(f)
with tm.ensure_clean() as path:
    float_frame.to_csv(path)
    recons = self.read_csv(path)
    tm.assert_frame_equal(float_frame, recons)
    tm.assert_frame_equal(np.isinf(float_frame), np.isinf(recons))
```

## Next Steps


---

*Source: test_to_csv.py:468 | Complexity: Intermediate | Last updated: 2026-06-02*