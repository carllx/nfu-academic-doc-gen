# How To: Read Csv Dataframe

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read csv dataframe

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `inspect`
- `io`
- `os`
- `pathlib`
- `sys`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.io.parsers`
- `pandas.io.parsers.c_parser_wrapper`

**Setup Required:**
```python
# Fixtures: all_parsers, csv1
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(csv1, index_col=0, parse_dates=True)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[0.980269, 3.685731, -0.364216805298, -1.159738], [1.047916, -0.041232, -0.16181208307, 0.212549], [0.498581, 0.731168, -0.537677223318, 1.34627], [1.120202, 1.567621, 0.00364077397681, 0.675253], [-0.487094, 0.571455, -1.6116394093, 0.103469], [0.836649, 0.246462, 0.588542635376, 1.062782], [-0.157161, 1.340307, 1.1957779562, -1.097007]], columns=['A', 'B', 'C', 'D'], index=Index([datetime(2000, 1, 3), datetime(2000, 1, 4), datetime(2000, 1, 5), datetime(2000, 1, 6), datetime(2000, 1, 7), datetime(2000, 1, 10), datetime(2000, 1, 11)], name='index'))
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result.index = result.index.as_unit(...)

```python
result.index = result.index.as_unit('ns')
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, csv1

# Workflow
parser = all_parsers
result = parser.read_csv(csv1, index_col=0, parse_dates=True)
if parser.engine == 'pyarrow':
    result.index = result.index.as_unit('ns')
expected = DataFrame([[0.980269, 3.685731, -0.364216805298, -1.159738], [1.047916, -0.041232, -0.16181208307, 0.212549], [0.498581, 0.731168, -0.537677223318, 1.34627], [1.120202, 1.567621, 0.00364077397681, 0.675253], [-0.487094, 0.571455, -1.6116394093, 0.103469], [0.836649, 0.246462, 0.588542635376, 1.062782], [-0.157161, 1.340307, 1.1957779562, -1.097007]], columns=['A', 'B', 'C', 'D'], index=Index([datetime(2000, 1, 3), datetime(2000, 1, 4), datetime(2000, 1, 5), datetime(2000, 1, 6), datetime(2000, 1, 7), datetime(2000, 1, 10), datetime(2000, 1, 11)], name='index'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_common_basic.py:197 | Complexity: Intermediate | Last updated: 2026-06-02*