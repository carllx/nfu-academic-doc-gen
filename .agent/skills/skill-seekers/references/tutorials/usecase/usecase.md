# How To: Usecase

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test usecase

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame.set_index(...)

```python
df = pd.DataFrame([[11, range(5), 10], [22, range(3), 20]], columns=list('ABC')).set_index('C')
```

### Step 2: Assign result = df.explode(...)

```python
result = df.explode('B')
```

### Step 3: Assign expected = pd.DataFrame.set_index(...)

```python
expected = pd.DataFrame({'A': [11, 11, 11, 11, 11, 22, 22, 22], 'B': np.array([0, 1, 2, 3, 4, 0, 1, 2], dtype=object), 'C': [10, 10, 10, 10, 10, 20, 20, 20]}, columns=list('ABC')).set_index('C')
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame([['2014-01-01', 'Alice', 'A B'], ['2014-01-02', 'Bob', 'C D']], columns=['dt', 'name', 'text'])
```

### Step 6: Assign result = df.assign.explode(...)

```python
result = df.assign(text=df.text.str.split(' ')).explode('text')
```

### Step 7: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([['2014-01-01', 'Alice', 'A'], ['2014-01-01', 'Alice', 'B'], ['2014-01-02', 'Bob', 'C'], ['2014-01-02', 'Bob', 'D']], columns=['dt', 'name', 'text'], index=[0, 0, 1, 1])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame([[11, range(5), 10], [22, range(3), 20]], columns=list('ABC')).set_index('C')
result = df.explode('B')
expected = pd.DataFrame({'A': [11, 11, 11, 11, 11, 22, 22, 22], 'B': np.array([0, 1, 2, 3, 4, 0, 1, 2], dtype=object), 'C': [10, 10, 10, 10, 10, 20, 20, 20]}, columns=list('ABC')).set_index('C')
tm.assert_frame_equal(result, expected)
df = pd.DataFrame([['2014-01-01', 'Alice', 'A B'], ['2014-01-02', 'Bob', 'C D']], columns=['dt', 'name', 'text'])
result = df.assign(text=df.text.str.split(' ')).explode('text')
expected = pd.DataFrame([['2014-01-01', 'Alice', 'A'], ['2014-01-01', 'Alice', 'B'], ['2014-01-02', 'Bob', 'C'], ['2014-01-02', 'Bob', 'D']], columns=['dt', 'name', 'text'], index=[0, 0, 1, 1])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_explode.py:130 | Complexity: Advanced | Last updated: 2026-06-02*