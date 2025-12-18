# Desktop Organizer (Rule-Based File Organization Engine)

A lightweight desktop file organization tool implemented in Python and packaged as a standalone Windows executable.

The tool organizes desktop files using a **rule-based classification engine**, prioritizing **deterministic behavior, safety, and configurability** over hard-coded logic.

---

## Motivation

Desktop clutter grows organically over time, and manual organization is repetitive and error-prone.

This project was built to explore how simple, deterministic systems can automate file organization safely while remaining easy to extend and reason about.

---

## Core Features

- Rule-based file classification driven by external configuration
- Deterministic rule ordering using explicit priorities
- Supports common file types (documents, images, code, presentations)
- **Undo support** via a persistent move log
- **Dry-run mode** to preview changes without modifying files
- Idempotent execution (safe to run multiple times)
- Packaged as a standalone Windows `.exe`

---

## How It Works

Organization behavior is defined declaratively using rules rather than hard-coded logic.

Each rule specifies:
- File extensions to match
- Destination folder
- Priority (lower value = higher precedence)

The engine evaluates files against rules in priority order and applies the first matching rule.

This design allows new file types to be supported by updating configuration rather than modifying code.

---

## Rule Configuration

Rules are defined in `rules.json`:

```json
{
  "rules": [
    {
      "name": "Images",
      "extensions": [".jpg", ".png", ".jpeg",".jfif",".webp"],
      "destination": "Images",
      "priority": 1
    },
    {
      "name": "Documents",
      "extensions": [".pdf", ".docx", ".txt", ".pptx", ".xlsx",".ppt"],
      "destination": "Documents",
      "priority": 2
    },
    {
      "name": "Code",
      "extensions": [".py", ".java", ".c", ".cpp"],
      "destination": "Code",
      "priority": 3
    }
  ]
}

```

## Usage

Organize Desktop

Double-click the executable:
```text
organize_desktop.exe
```

Undo Last Organization
```text
organize_desktop.exe --undo
```

Preview Changes (Dry Run)
```text
organize_desktop.exe --dry-run
```

## Safety Guarantees

- **Undo** functionality allows all changes to be reverted
- **Dry-run mode** prevents accidental file movement
- Files already in correct folders are skipped
- Execution is deterministic and repeatable

## Design Decisions & Tradeoffs

- **Rule-based classification** was chosen over heuristic or ML-based approaches to ensure predictability and explainability
- **External configuration** allows extensibility without code changes
- **Undo logging** provides transactional safety
- **Single-file executable** simplifies distribution and usage

---

## Limitations & Future Improvements

- Recursive directory organization
- Cross-platform support
- Scheduled or background execution
- GUI-based rule editor

---

## Why This Project

This project demonstrates how a small, focused system can apply core software engineering principles, **separation of concerns**, **determinism**, and **safety**, to solve a practical automation problem.

The emphasis is on clarity, correctness, and controlled behavior rather than feature complexity.



