# How To: Skip Row With Quote

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test skip row with quote

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'id,text,num_lines\n1,"line \'11\' line 12",2\n2,"line \'21\' line 22",2\n3,"line \'31\' line 32",1'

```python
data = 'id,text,num_lines\n1,"line \'11\' line 12",2\n2,"line \'21\' line 22",2\n3,"line \'31\' line 32",1'
```

### Step 3: Assign exp_data = value

```python
exp_data = [[2, "line '21' line 22", 2], [3, "line '31' line 32", 1]]
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(exp_data, columns=['id', 'text', 'num_lines'])
```

### Step 5: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), skiprows=[1])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'id,text,num_lines\n1,"line \'11\' line 12",2\n2,"line \'21\' line 22",2\n3,"line \'31\' line 32",1'
exp_data = [[2, "line '21' line 22", 2], [3, "line '31' line 32", 1]]
expected = DataFrame(exp_data, columns=['id', 'text', 'num_lines'])
result = parser.read_csv(StringIO(data), skiprows=[1])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_skiprows.py:139 | Complexity: Intermediate | Last updated: 2026-06-02*