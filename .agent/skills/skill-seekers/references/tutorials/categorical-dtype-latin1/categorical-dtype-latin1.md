# How To: Categorical Dtype Latin1

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical dtype latin1

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `os`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, csv_dir_path
```

## Step-by-Step Guide

### Step 1: Assign pth = os.path.join(...)

```python
pth = os.path.join(csv_dir_path, 'unicode_series.csv')
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign encoding = 'latin-1'

```python
encoding = 'latin-1'
```

### Step 4: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(pth, header=None, encoding=encoding)
```

### Step 5: Assign unknown = Categorical(...)

```python
expected[1] = Categorical(expected[1])
```

### Step 6: Assign actual = parser.read_csv(...)

```python
actual = parser.read_csv(pth, header=None, encoding=encoding, dtype={1: 'category'})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, csv_dir_path

# Workflow
pth = os.path.join(csv_dir_path, 'unicode_series.csv')
parser = all_parsers
encoding = 'latin-1'
expected = parser.read_csv(pth, header=None, encoding=encoding)
expected[1] = Categorical(expected[1])
actual = parser.read_csv(pth, header=None, encoding=encoding, dtype={1: 'category'})
tm.assert_frame_equal(actual, expected)
```

## Next Steps


---

*Source: test_categorical.py:204 | Complexity: Intermediate | Last updated: 2026-06-02*