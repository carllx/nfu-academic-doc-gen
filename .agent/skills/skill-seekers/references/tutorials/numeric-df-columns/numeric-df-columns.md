# How To: Numeric Df Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numeric df columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `numpy`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: columns
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1.2, decimal.Decimal(3.14), decimal.Decimal('infinity'), '0.1'], 'b': [1.0, 2.0, 3.0, 4.0]})
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1.2, 3.14, np.inf, 0.1], 'b': [1.0, 2.0, 3.0, 4.0]})
```

### Step 3: Assign df_copy = df.copy(...)

```python
df_copy = df.copy()
```

### Step 4: Assign unknown = unknown.apply(...)

```python
df_copy[columns] = df_copy[columns].apply(to_numeric)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_copy, expected)
```


## Complete Example

```python
# Setup
# Fixtures: columns

# Workflow
df = DataFrame({'a': [1.2, decimal.Decimal(3.14), decimal.Decimal('infinity'), '0.1'], 'b': [1.0, 2.0, 3.0, 4.0]})
expected = DataFrame({'a': [1.2, 3.14, np.inf, 0.1], 'b': [1.0, 2.0, 3.0, 4.0]})
df_copy = df.copy()
df_copy[columns] = df_copy[columns].apply(to_numeric)
tm.assert_frame_equal(df_copy, expected)
```

## Next Steps


---

*Source: test_to_numeric.py:197 | Complexity: Intermediate | Last updated: 2026-06-02*