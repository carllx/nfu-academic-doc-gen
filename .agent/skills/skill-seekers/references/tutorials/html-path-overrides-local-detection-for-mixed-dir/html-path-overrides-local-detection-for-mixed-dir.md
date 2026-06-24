# How To: Html Path Overrides Local Detection For Mixed Dir

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: A code-heavy directory with --html-path should route to html.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `textwrap`
- `pytest`
- `skill_seekers.cli.config_validator`
- `skill_seekers.cli.source_detector`
- `skill_seekers.cli.unified_skill_builder`
- `skill_seekers.cli.skill_converter`
- `importlib`
- `skill_seekers.cli.skill_converter`
- `unittest.mock`
- `skill_seekers.cli.skill_converter`
- `inspect`
- `argparse`
- `skill_seekers.cli.arguments.create`
- `skill_seekers.cli.create_command`
- `skill_seekers.cli.source_detector`
- `skill_seekers.cli.create_command`
- `skill_seekers.cli.create_command`
- `skill_seekers.cli.create_command`
- `skill_seekers.cli.execution_context`
- `skill_seekers.cli.source_detector`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: 'A code-heavy directory with --html-path should route to html.'

```python
'A code-heavy directory with --html-path should route to html.'
```

**Verification:**
```python
assert info.type == 'local'
```

### Step 2: Assign mixed = value

```python
mixed = tmp_path / 'mixed'
```

### Step 3: Call mixed.mkdir()

```python
mixed.mkdir()
```

### Step 4: Call unknown.write_text()

```python
(mixed / 'page.html').write_text('<html></html>')
```

### Step 5: Assign args = self._make_args(...)

```python
args = self._make_args(source=str(mixed), html_path=str(mixed / 'page.html'))
```

### Step 6: Assign cmd = CreateCommand(...)

```python
cmd = CreateCommand(args)
```

### Step 7: Assign detection_input = cmd._resolve_detection_input(...)

```python
detection_input = cmd._resolve_detection_input()
```

### Step 8: Assign info = SourceDetector.detect(...)

```python
info = SourceDetector.detect(detection_input)
```

**Verification:**
```python
assert info.type == 'local'
```

### Step 9: Call unknown.write_text()

```python
(mixed / f'src{i}.py').write_text('x = 1\n')
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'A code-heavy directory with --html-path should route to html.'
from skill_seekers.cli.create_command import CreateCommand
mixed = tmp_path / 'mixed'
mixed.mkdir()
for i in range(5):
    (mixed / f'src{i}.py').write_text('x = 1\n')
(mixed / 'page.html').write_text('<html></html>')
args = self._make_args(source=str(mixed), html_path=str(mixed / 'page.html'))
cmd = CreateCommand(args)
detection_input = cmd._resolve_detection_input()
from skill_seekers.cli.source_detector import SourceDetector
info = SourceDetector.detect(detection_input)
assert info.type == 'local'
```

## Next Steps


---

*Source: test_new_source_types.py:952 | Complexity: Advanced | Last updated: 2026-06-02*