# How To: Read Csv Buglet 4X Multi Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read csv buglet 4x multi index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `csv`
- `io`
- `typing`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `collections.abc`

**Setup Required:**
```python
# Fixtures: python_parser_only
```

## Step-by-Step Guide

### Step 1: Assign data = '                      A       B       C       D        E\none two three   four\na   b   10.0032 5    -0.5109 -2.3358 -0.4645  0.05076  0.3640\na   q   20      4     0.4473  1.4152  0.2834  1.00661  0.1744\nx   q   30      3    -0.6662 -0.5243 -0.3580  0.89145  2.5838'

```python
data = '                      A       B       C       D        E\none two three   four\na   b   10.0032 5    -0.5109 -2.3358 -0.4645  0.05076  0.3640\na   q   20      4     0.4473  1.4152  0.2834  1.00661  0.1744\nx   q   30      3    -0.6662 -0.5243 -0.3580  0.89145  2.5838'
```

### Step 2: Assign parser = python_parser_only

```python
parser = python_parser_only
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[-0.5109, -2.3358, -0.4645, 0.05076, 0.364], [0.4473, 1.4152, 0.2834, 1.00661, 0.1744], [-0.6662, -0.5243, -0.358, 0.89145, 2.5838]], columns=['A', 'B', 'C', 'D', 'E'], index=MultiIndex.from_tuples([('a', 'b', 10.0032, 5), ('a', 'q', 20, 4), ('x', 'q', 30, 3)], names=['one', 'two', 'three', 'four']))
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), sep='\\s+')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: python_parser_only

# Workflow
data = '                      A       B       C       D        E\none two three   four\na   b   10.0032 5    -0.5109 -2.3358 -0.4645  0.05076  0.3640\na   q   20      4     0.4473  1.4152  0.2834  1.00661  0.1744\nx   q   30      3    -0.6662 -0.5243 -0.3580  0.89145  2.5838'
parser = python_parser_only
expected = DataFrame([[-0.5109, -2.3358, -0.4645, 0.05076, 0.364], [0.4473, 1.4152, 0.2834, 1.00661, 0.1744], [-0.6662, -0.5243, -0.358, 0.89145, 2.5838]], columns=['A', 'B', 'C', 'D', 'E'], index=MultiIndex.from_tuples([('a', 'b', 10.0032, 5), ('a', 'q', 20, 4), ('x', 'q', 30, 3)], names=['one', 'two', 'three', 'four']))
result = parser.read_csv(StringIO(data), sep='\\s+')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_python_parser_only.py:181 | Complexity: Intermediate | Last updated: 2026-06-02*