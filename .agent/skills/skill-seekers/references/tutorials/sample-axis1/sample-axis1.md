# How To: Sample Axis1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sample axis1

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign easy_weight_list = value

```python
easy_weight_list = [0] * 3
```

### Step 2: Assign unknown = 1

```python
easy_weight_list[2] = 1
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'col1': range(10, 20), 'col2': range(20, 30), 'colString': ['a'] * 10})
```

### Step 4: Assign sample1 = df.sample(...)

```python
sample1 = df.sample(n=1, axis=1, weights=easy_weight_list)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sample1, df[['colString']])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.sample(n=3, random_state=42), df.sample(n=3, axis=0, random_state=42))
```


## Complete Example

```python
# Workflow
easy_weight_list = [0] * 3
easy_weight_list[2] = 1
df = DataFrame({'col1': range(10, 20), 'col2': range(20, 30), 'colString': ['a'] * 10})
sample1 = df.sample(n=1, axis=1, weights=easy_weight_list)
tm.assert_frame_equal(sample1, df[['colString']])
tm.assert_frame_equal(df.sample(n=3, random_state=42), df.sample(n=3, axis=0, random_state=42))
```

## Next Steps


---

*Source: test_sample.py:299 | Complexity: Intermediate | Last updated: 2026-06-02*