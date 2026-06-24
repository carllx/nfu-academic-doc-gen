# How To: Recarray From Obj

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test recarray from obj

## Prerequisites

**Required Modules:**
- `collections.abc`
- `pickle`
- `textwrap`
- `io`
- `os`
- `pathlib`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign count = 10

```python
count = 10
```

**Verification:**
```python
assert_(mine.date[i] == list(range(1, 10)))
```

### Step 2: Assign a = np.zeros(...)

```python
a = np.zeros(count, dtype='O')
```

**Verification:**
```python
assert_(mine.data1[i] == 0.0)
```

### Step 3: Assign b = np.zeros(...)

```python
b = np.zeros(count, dtype='f8')
```

**Verification:**
```python
assert_(mine.data2[i] == 0.0)
```

### Step 4: Assign c = np.zeros(...)

```python
c = np.zeros(count, dtype='f8')
```

### Step 5: Assign mine = np.rec.fromarrays(...)

```python
mine = np.rec.fromarrays([a, b, c], names='date,data1,data2')
```

### Step 6: Assign unknown = list(...)

```python
a[i] = list(range(1, 10))
```

### Step 7: Call assert_()

```python
assert_(mine.date[i] == list(range(1, 10)))
```

### Step 8: Call assert_()

```python
assert_(mine.data1[i] == 0.0)
```

### Step 9: Call assert_()

```python
assert_(mine.data2[i] == 0.0)
```


## Complete Example

```python
# Workflow
count = 10
a = np.zeros(count, dtype='O')
b = np.zeros(count, dtype='f8')
c = np.zeros(count, dtype='f8')
for i in range(len(a)):
    a[i] = list(range(1, 10))
mine = np.rec.fromarrays([a, b, c], names='date,data1,data2')
for i in range(len(a)):
    assert_(mine.date[i] == list(range(1, 10)))
    assert_(mine.data1[i] == 0.0)
    assert_(mine.data2[i] == 0.0)
```

## Next Steps


---

*Source: test_records.py:111 | Complexity: Advanced | Last updated: 2026-06-02*