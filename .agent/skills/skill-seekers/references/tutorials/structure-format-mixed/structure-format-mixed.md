# How To: Structure Format Mixed

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test structure format mixed

## Prerequisites

**Required Modules:**
- `gc`
- `sys`
- `textwrap`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `numpy`
- `numpy._core.arrayprint`
- `numpy.testing`
- `numpy.testing._private.utils`


## Step-by-Step Guide

### Step 1: Assign dt = np.dtype(...)

```python
dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
```

**Verification:**
```python
assert_equal(np.array2string(x), "[('Sarah', [8., 7.]) ('John', [6., 7.])]")
```

### Step 2: Assign x = np.array(...)

```python
x = np.array([('Sarah', (8.0, 7.0)), ('John', (6.0, 7.0))], dtype=dt)
```

**Verification:**
```python
assert_equal(np.array2string(A), textwrap.dedent("                [('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',)\n                 ('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',) ('NaT',) ('NaT',)\n                 ('NaT',) ('NaT',) ('NaT',)]"))
```

### Step 3: Call assert_equal()

```python
assert_equal(np.array2string(x), "[('Sarah', [8., 7.]) ('John', [6., 7.])]")
```

**Verification:**
```python
assert_equal(np.array2string(A), textwrap.dedent("            [('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',)\n             ('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',)\n             ('1970-01-01T00:00:00',) (                'NaT',)\n             (                'NaT',) (                'NaT',)\n             (                'NaT',) (                'NaT',)]"))
```

### Step 4: Call np.set_printoptions()

```python
np.set_printoptions(legacy='1.13')
```

**Verification:**
```python
assert_equal(np.array2string(A), textwrap.dedent("            [(123456,) (123456,) (123456,) (123456,) (123456,) ( 'NaT',) ( 'NaT',)\n             ( 'NaT',) ( 'NaT',) ( 'NaT',)]"))
```

### Step 5: Call assert_equal()

```python
assert_equal(np.array2string(A), textwrap.dedent("            [('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',)\n             ('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',)\n             ('1970-01-01T00:00:00',) (                'NaT',)\n             (                'NaT',) (                'NaT',)\n             (                'NaT',) (                'NaT',)]"))
```

### Step 6: Assign A = np.full(...)

```python
A = np.full(10, 123456, dtype=[('A', 'm8[s]')])
```

### Step 7: Call unknown.fill()

```python
A[5:].fill(np.datetime64('NaT'))
```

### Step 8: Call assert_equal()

```python
assert_equal(np.array2string(A), textwrap.dedent("            [(123456,) (123456,) (123456,) (123456,) (123456,) ( 'NaT',) ( 'NaT',)\n             ( 'NaT',) ( 'NaT',) ( 'NaT',)]"))
```

### Step 9: Assign A = np.zeros(...)

```python
A = np.zeros(shape=10, dtype=[('A', 'M8[s]')])
```

### Step 10: Call unknown.fill()

```python
A[5:].fill(np.datetime64('NaT'))
```

### Step 11: Call assert_equal()

```python
assert_equal(np.array2string(A), textwrap.dedent("                [('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',)\n                 ('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',) ('NaT',) ('NaT',)\n                 ('NaT',) ('NaT',) ('NaT',)]"))
```

### Step 12: Call np.set_printoptions()

```python
np.set_printoptions(legacy=False)
```


## Complete Example

```python
# Workflow
dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
x = np.array([('Sarah', (8.0, 7.0)), ('John', (6.0, 7.0))], dtype=dt)
assert_equal(np.array2string(x), "[('Sarah', [8., 7.]) ('John', [6., 7.])]")
np.set_printoptions(legacy='1.13')
try:
    A = np.zeros(shape=10, dtype=[('A', 'M8[s]')])
    A[5:].fill(np.datetime64('NaT'))
    assert_equal(np.array2string(A), textwrap.dedent("                [('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',)\n                 ('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',) ('NaT',) ('NaT',)\n                 ('NaT',) ('NaT',) ('NaT',)]"))
finally:
    np.set_printoptions(legacy=False)
assert_equal(np.array2string(A), textwrap.dedent("            [('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',)\n             ('1970-01-01T00:00:00',) ('1970-01-01T00:00:00',)\n             ('1970-01-01T00:00:00',) (                'NaT',)\n             (                'NaT',) (                'NaT',)\n             (                'NaT',) (                'NaT',)]"))
A = np.full(10, 123456, dtype=[('A', 'm8[s]')])
A[5:].fill(np.datetime64('NaT'))
assert_equal(np.array2string(A), textwrap.dedent("            [(123456,) (123456,) (123456,) (123456,) (123456,) ( 'NaT',) ( 'NaT',)\n             ( 'NaT',) ( 'NaT',) ( 'NaT',)]"))
```

## Next Steps


---

*Source: test_arrayprint.py:269 | Complexity: Advanced | Last updated: 2026-06-02*