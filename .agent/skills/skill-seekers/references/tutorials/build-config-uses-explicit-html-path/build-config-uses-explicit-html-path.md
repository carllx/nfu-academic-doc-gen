# How To: Build Config Uses Explicit Html Path

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: `config["html_path"]` reflects --html-path, not the positional path.

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

### Step 1: '`config["html_path"]` reflects --html-path, not the positional path.'

```python
'`config["html_path"]` reflects --html-path, not the positional path.'
```

**Verification:**
```python
assert config['html_path'] == str(explicit)
```

### Step 2: Assign positional_dir = value

```python
positional_dir = tmp_path / 'site'
```

### Step 3: Call positional_dir.mkdir()

```python
positional_dir.mkdir()
```

### Step 4: Assign explicit = value

```python
explicit = tmp_path / 'doc.html'
```

### Step 5: Call explicit.write_text()

```python
explicit.write_text('<html></html>')
```

### Step 6: Assign args = self._make_args(...)

```python
args = self._make_args(source=str(positional_dir), html_path=str(explicit))
```

### Step 7: Assign cmd = CreateCommand(...)

```python
cmd = CreateCommand(args)
```

### Step 8: Assign cmd.source_info = SourceInfo(...)

```python
cmd.source_info = SourceInfo(type='html', parsed={'file_path': str(positional_dir)}, suggested_name='site', raw_input=str(positional_dir))
```

### Step 9: Call ExecutionContext.initialize()

```python
ExecutionContext.initialize(args=args, source_info=cmd.source_info)
```

### Step 10: Assign ctx = ExecutionContext.get(...)

```python
ctx = ExecutionContext.get()
```

### Step 11: Assign config = cmd._build_config(...)

```python
config = cmd._build_config('html', ctx)
```

**Verification:**
```python
assert config['html_path'] == str(explicit)
```

### Step 12: Call ExecutionContext.reset()

```python
ExecutionContext.reset()
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'`config["html_path"]` reflects --html-path, not the positional path.'
from skill_seekers.cli.create_command import CreateCommand
from skill_seekers.cli.execution_context import ExecutionContext
from skill_seekers.cli.source_detector import SourceInfo
positional_dir = tmp_path / 'site'
positional_dir.mkdir()
explicit = tmp_path / 'doc.html'
explicit.write_text('<html></html>')
args = self._make_args(source=str(positional_dir), html_path=str(explicit))
cmd = CreateCommand(args)
cmd.source_info = SourceInfo(type='html', parsed={'file_path': str(positional_dir)}, suggested_name='site', raw_input=str(positional_dir))
ExecutionContext.initialize(args=args, source_info=cmd.source_info)
try:
    ctx = ExecutionContext.get()
    config = cmd._build_config('html', ctx)
    assert config['html_path'] == str(explicit)
finally:
    ExecutionContext.reset()
```

## Next Steps


---

*Source: test_new_source_types.py:997 | Complexity: Advanced | Last updated: 2026-06-02*