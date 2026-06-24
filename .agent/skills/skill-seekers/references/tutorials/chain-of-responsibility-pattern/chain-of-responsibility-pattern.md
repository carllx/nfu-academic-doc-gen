# How To: Chain Of Responsibility Pattern

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test chain of responsibility pattern

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `unittest`
- `skill_seekers.cli.pattern_recognizer`
- `skill_seekers.cli.code_analyzer`
- `skill_seekers.cli.pattern_recognizer`
- `skill_seekers.cli.code_analyzer`
- `skill_seekers.cli.pattern_recognizer`


## Step-by-Step Guide

### Step 1: Assign code = '\nclass Handler:\n    def __init__(self): self.next_handler = None\n    def set_next(self, handler): self.next_handler = handler; return handler\n    def handle(self, request):\n        if self.next_handler: return self.next_handler.handle(request)\nclass AuthHandler(Handler):\n    def handle(self, request):\n        if not request.get("authenticated"): return "Not authenticated"\n        return super().handle(request)\n'

```python
code = '\nclass Handler:\n    def __init__(self): self.next_handler = None\n    def set_next(self, handler): self.next_handler = handler; return handler\n    def handle(self, request):\n        if self.next_handler: return self.next_handler.handle(request)\nclass AuthHandler(Handler):\n    def handle(self, request):\n        if not request.get("authenticated"): return "Not authenticated"\n        return super().handle(request)\n'
```

**Verification:**
```python
assert len(report.patterns) >= 0
```

### Step 2: Assign file_info = self.analyzer.analyze_file(...)

```python
file_info = self.analyzer.analyze_file('test.py', code, 'Python')
```

### Step 3: Assign report = self.recognizer.analyze_file(...)

```python
report = self.recognizer.analyze_file('test.py', code, 'Python')
```

**Verification:**
```python
assert len(report.patterns) >= 0
```

### Step 4: Call self.skipTest()

```python
self.skipTest('CodeAnalyzer did not extract classes')
```


## Complete Example

```python
# Workflow
code = '\nclass Handler:\n    def __init__(self): self.next_handler = None\n    def set_next(self, handler): self.next_handler = handler; return handler\n    def handle(self, request):\n        if self.next_handler: return self.next_handler.handle(request)\nclass AuthHandler(Handler):\n    def handle(self, request):\n        if not request.get("authenticated"): return "Not authenticated"\n        return super().handle(request)\n'
file_info = self.analyzer.analyze_file('test.py', code, 'Python')
if not file_info or not file_info.get('classes'):
    self.skipTest('CodeAnalyzer did not extract classes')
report = self.recognizer.analyze_file('test.py', code, 'Python')
assert len(report.patterns) >= 0
```

## Next Steps


---

*Source: test_pattern_recognizer.py:591 | Complexity: Intermediate | Last updated: 2026-06-02*