# How To: Read Csv No Index Name

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read csv no index name

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `os`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, csv_dir_path
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign csv2 = os.path.join(...)

```python
csv2 = os.path.join(csv_dir_path, 'test2.csv')
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(csv2, index_col=0, parse_dates=True)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[0.980269, 3.685731, -0.364216805298, -1.159738, 'foo'], [1.047916, -0.041232, -0.16181208307, 0.212549, 'bar'], [0.498581, 0.731168, -0.537677223318, 1.34627, 'baz'], [1.120202, 1.567621, 0.00364077397681, 0.675253, 'qux'], [-0.487094, 0.571455, -1.6116394093, 0.103469, 'foo2']], columns=['A', 'B', 'C', 'D', 'E'], index=Index([datetime(2000, 1, 3), datetime(2000, 1, 4), datetime(2000, 1, 5), datetime(2000, 1, 6), datetime(2000, 1, 7)]))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, csv_dir_path

# Workflow
parser = all_parsers
csv2 = os.path.join(csv_dir_path, 'test2.csv')
result = parser.read_csv(csv2, index_col=0, parse_dates=True)
expected = DataFrame([[0.980269, 3.685731, -0.364216805298, -1.159738, 'foo'], [1.047916, -0.041232, -0.16181208307, 0.212549, 'bar'], [0.498581, 0.731168, -0.537677223318, 1.34627, 'baz'], [1.120202, 1.567621, 0.00364077397681, 0.675253, 'qux'], [-0.487094, 0.571455, -1.6116394093, 0.103469, 'foo2']], columns=['A', 'B', 'C', 'D', 'E'], index=Index([datetime(2000, 1, 3), datetime(2000, 1, 4), datetime(2000, 1, 5), datetime(2000, 1, 6), datetime(2000, 1, 7)]))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_index.py:242 | Complexity: Intermediate | Last updated: 2026-06-02*