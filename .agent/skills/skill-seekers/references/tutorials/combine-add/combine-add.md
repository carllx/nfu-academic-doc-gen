# How To: Combine Add

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine add

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.tests.extension`

**Setup Required:**
```python
# Fixtures: data_repeated
```

## Step-by-Step Guide

### Step 1: Assign unknown = data_repeated(...)

```python
orig_data1, orig_data2 = data_repeated(2)
```

### Step 2: Assign s1 = pd.Series(...)

```python
s1 = pd.Series(orig_data1)
```

### Step 3: Assign s2 = pd.Series(...)

```python
s2 = pd.Series(orig_data2)
```

### Step 4: Assign result = s1.combine(...)

```python
result = s1.combine(s2, lambda x1, x2: x1 + x2)
```

### Step 5: Assign expected = pd.Series(...)

```python
expected = pd.Series([a + b for a, b in zip(list(orig_data1), list(orig_data2))])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign val = value

```python
val = s1.iloc[0]
```

### Step 8: Assign result = s1.combine(...)

```python
result = s1.combine(val, lambda x1, x2: x1 + x2)
```

### Step 9: Assign expected = pd.Series(...)

```python
expected = pd.Series([a + val for a in list(orig_data1)])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: data_repeated

# Workflow
orig_data1, orig_data2 = data_repeated(2)
s1 = pd.Series(orig_data1)
s2 = pd.Series(orig_data2)
result = s1.combine(s2, lambda x1, x2: x1 + x2)
expected = pd.Series([a + b for a, b in zip(list(orig_data1), list(orig_data2))])
tm.assert_series_equal(result, expected)
val = s1.iloc[0]
result = s1.combine(val, lambda x1, x2: x1 + x2)
expected = pd.Series([a + val for a in list(orig_data1)])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:129 | Complexity: Advanced | Last updated: 2026-06-02*