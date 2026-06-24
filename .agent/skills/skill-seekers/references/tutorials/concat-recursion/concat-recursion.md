# How To: Concat Recursion

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat recursion

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

### Step 1: Assign df = value

```python
df = styler.data
```

**Verification:**
```python
assert expected in result
```

### Step 2: Assign styler1 = styler

```python
styler1 = styler
```

### Step 3: Assign styler2 = Styler(...)

```python
styler2 = Styler(df.agg(['mean']), precision=3)
```

### Step 4: Assign styler3 = Styler(...)

```python
styler3 = Styler(df.agg(['mean']), precision=4)
```

### Step 5: Call styler1.concat.set_uuid()

```python
styler1.concat(styler2.concat(styler3)).set_uuid('X')
```

### Step 6: Assign result = styler.to_html(...)

```python
result = styler.to_html()
```

### Step 7: Assign fp1 = 'foot0_'

```python
fp1 = 'foot0_'
```

### Step 8: Assign fp2 = 'foot0_foot0_'

```python
fp2 = 'foot0_foot0_'
```

### Step 9: Assign expected = dedent(...)

```python
expected = dedent(f'    <tr>\n      <th id="T_X_level0_row1" class="row_heading level0 row1" >b</th>\n      <td id="T_X_row1_col0" class="data row1 col0" >2.690000</td>\n    </tr>\n    <tr>\n      <th id="T_X_level0_{fp1}row0" class="{fp1}row_heading level0 {fp1}row0" >mean</th>\n      <td id="T_X_{fp1}row0_col0" class="{fp1}data {fp1}row0 col0" >2.650</td>\n    </tr>\n    <tr>\n      <th id="T_X_level0_{fp2}row0" class="{fp2}row_heading level0 {fp2}row0" >mean</th>\n      <td id="T_X_{fp2}row0_col0" class="{fp2}data {fp2}row0 col0" >2.6500</td>\n    </tr>\n  </tbody>\n</table>\n    ')
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
df = styler.data
styler1 = styler
styler2 = Styler(df.agg(['mean']), precision=3)
styler3 = Styler(df.agg(['mean']), precision=4)
styler1.concat(styler2.concat(styler3)).set_uuid('X')
result = styler.to_html()
fp1 = 'foot0_'
fp2 = 'foot0_foot0_'
expected = dedent(f'    <tr>\n      <th id="T_X_level0_row1" class="row_heading level0 row1" >b</th>\n      <td id="T_X_row1_col0" class="data row1 col0" >2.690000</td>\n    </tr>\n    <tr>\n      <th id="T_X_level0_{fp1}row0" class="{fp1}row_heading level0 {fp1}row0" >mean</th>\n      <td id="T_X_{fp1}row0_col0" class="{fp1}data {fp1}row0 col0" >2.650</td>\n    </tr>\n    <tr>\n      <th id="T_X_level0_{fp2}row0" class="{fp2}row_heading level0 {fp2}row0" >mean</th>\n      <td id="T_X_{fp2}row0_col0" class="{fp2}data {fp2}row0 col0" >2.6500</td>\n    </tr>\n  </tbody>\n</table>\n    ')
assert expected in result
```

## Next Steps


---

*Source: test_html.py:849 | Complexity: Advanced | Last updated: 2026-06-02*