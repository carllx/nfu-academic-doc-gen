# How To: From Records Lists Generator

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from records lists generator

## Prerequisites

**Required Modules:**
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pytz`
- `pandas._config`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign columns_names = value

```python
columns_names = ['Integer', 'String', 'Float']
```

### Step 2: Assign columns = value

```python
columns = [[i[j] for i in list_generator(10)] for j in range(len(columns_names))]
```

### Step 3: Assign data = value

```python
data = {'Integer': columns[0], 'String': columns[1], 'Float': columns[2]}
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(data, columns=columns_names)
```

### Step 5: Assign generator = list_generator(...)

```python
generator = list_generator(10)
```

### Step 6: Assign result = DataFrame.from_records(...)

```python
result = DataFrame.from_records(generator, columns=columns_names)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

```python
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
```

### Step 9: yield [i, letters[i % len(letters)], i / length]

```python
yield [i, letters[i % len(letters)], i / length]
```


## Complete Example

```python
# Workflow
def list_generator(length):
    for i in range(length):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        yield [i, letters[i % len(letters)], i / length]
columns_names = ['Integer', 'String', 'Float']
columns = [[i[j] for i in list_generator(10)] for j in range(len(columns_names))]
data = {'Integer': columns[0], 'String': columns[1], 'Float': columns[2]}
expected = DataFrame(data, columns=columns_names)
generator = list_generator(10)
result = DataFrame.from_records(generator, columns=columns_names)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_from_records.py:368 | Complexity: Advanced | Last updated: 2026-06-02*