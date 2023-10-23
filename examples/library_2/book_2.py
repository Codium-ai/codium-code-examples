from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Book2:
    title: str
    author: str
