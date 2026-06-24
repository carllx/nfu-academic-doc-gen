# How To: Concat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`

**Setup Required:**
```python
# Fixtures: styler
```

## Step-by-Step Guide

### Step 1: Assign other = value

```python
other = styler.data.agg(['mean']).style
```

**Verification:**
```python
assert expected in result
```

### Step 2: Call styler.concat.set_uuid()

```python
styler.concat(other).set_uuid('X')
```

### Step 3: Assign result = styler.to_html(...)

```python
result = styler.to_html()
```

### Step 4: Assign fp = 'foot0_'

```python
fp = 'foot0_'
```

### Step 5: Assign expected = dedent(...)

```python
expected = dedent(f'    <tr>\n      <th id="T_X_level0_row1" class="row_heading level0 row1" >b</th>\n      <td id="T_X_row1_col0" class="data row1 col0" >2.690000</td>\n    </tr>\n    <tr>\n      <th id="T_X_level0_{fp}row0" class="{fp}row_heading level0 {fp}row0" >mean</th>\n      <td id="T_X_{fp}row0_col0" class="{fp}data {fp}row0 col0" >2.650000</td>\n    </tr>\n  </tbody>\n</table>\n    ')
```

**Verification:**
```python
assert expected in result
```


## Complete Example

```python
# Setup
# Fixtures: styler

# Workflow
other = styler.data.agg(['mean']).style
styler.concat(other).set_uuid('X')
result = styler.to_html()
fp = 'foot0_'
expected = dedent(f'    <tr>\n      <th id="T_X_level0_row1" class="row_heading level0 row1" >b</th>\n      <td id="T_X_row1_col0" class="data row1 col0" >2.690000</td>\n    </tr>\n    <tr>\n      <th id="T_X_level0_{fp}row0" class="{fp}row_heading level0 {fp}row0" >mean</th>\n      <td id="T_X_{fp}row0_col0" class="{fp}data {fp}row0 col0" >2.650000</td>\n    </tr>\n  </tbody>\n</table>\n    ')
assert expected in result
```

## Next Steps


---

*Source: test_html.py:827 | Complexity: Intermediate | Last updated: 2026-06-02*