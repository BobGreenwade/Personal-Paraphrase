# Personal Paraphrase

**Persona-driven editorial rewriter for AI agents and companion modules.**

Personal Paraphrase transforms generic output into the stylistic voice of the AI's own persona—drawing from real descriptors, recent chat history, and emotional tone cues. It’s designed to be used by modules like Fact Check or DLI, and can be extended to any system that benefits from rhythm-aware, persona-infused phrasing.

---

## 🔍 Purpose

This module rephrases "stock" text into the AI's own editorial voice. It does not use presets or templates—instead, it dynamically constructs prompts using:

- Config-driven persona descriptors
- Recent chat history
- Optional tone and style cues

The result is output that reflects the AI’s rhythm, wit, and editorial nuance.

---

## 🧩 Architecture

- `paraphrase.py`: Main module for persona-aware paraphrasing
- `config.json`: Defines paths, patterns, and LLM parameters
- `configEditor.py`: Standalone and importable utility for editing `config.json`

> Note: A separate module called `configHub.py` is planned to aggregate config editors across multiple systems, including this one.

---

## 🔗 Integration

Modules that can benefit from Personal Paraphrase include:
- Any companion or agent AI: Especially those with distinct personalities or editorial styles
- Any "wrapper" module that generates text (such as Fact Check or Delusion Loop Interrupter)

To integrate, simply import and call:
```
from paraphrase import paraphrase

output = paraphrase("Original text here", persona="persona")
```

---

## ⚙️ Configuration

Settings are defined in config.json, including:
- Persona resolution: Where to find descriptor files (e.g., persona/Draco.txt)
- Chat history: Recent lines used to model voice
- LLM settings: Endpoint, model, and temperature
Use configEditor.py to safely view, edit, and validate this file. It supports both standalone use and modular import.

---

## 🧠 Editorial Principles

- No presets: All paraphrasing is based on real persona descriptors and recent voice history.
- Voice fidelity: Output reflects the AI’s rhythm, tone, and editorial nuance—not a generic rewording.
- Fallback logic: If the LLM fails or returns unchanged output, the original text is used.

---

## 📜 License

Licensed under the MIT License.

---

## ✅ Status

**Ready to go!** 

Modular, persona-aware, and built for editorial integrity (if I do say so myself).
