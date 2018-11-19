#!/usr/bin/env python3
"""Add constant to a range of pdf pages, and then export those pages."""

from dataclasses import dataclass
from typing import List


@dataclass
class PageRange:
    """A range of pages."""

    start: int
    end: int


def tokenize(ranges: str) -> List[PageRange]:
    """Convert input into list of ranges."""
    split_ranges = [[int(p) for p in r.split("-")] for r in ranges.split(",")]
    return [PageRange(r[0], r[1]) for r in split_ranges]


def validate(prange: PageRange) -> None:
    """Perform basic sanity checks on PageRange."""
    assert isinstance(prange.start, int)
    assert isinstance(prange.end, int)
    assert prange.end - prange.start >= 0


def add_const(prange: PageRange, const: int) -> PageRange:
    """Add a constant to a PageRange."""
    return PageRange(start=prange.start + const, end=prange.end + const)


def find_offset(papernum: int, virtualnum: int):
    """Find how far the paper and virtual numbers are offset, from an example."""
    return virtualnum - papernum


def coalesce(ranges: List[PageRange]) -> str:
    """Inversion of tokenize function"""
    return ",".join([f"{p.start}-{p.end}" for p in ranges])


def create_command(ranges: str, filename: str) -> str:
    """Create pdftk command"""
    return f"pdftk {filename} cat {ranges} output {filename[:5]}_output.pdf"


if __name__ == "__main__":
    toks = tokenize(input("Input page numbers: "))
    for tok in toks:
        validate(tok)
    offset = find_offset(int(input("Number on paper: ")), int(input("Number on pdf: ")))
    adjusted = [add_const(p, offset) for p in toks]
    print(coalesce(adjusted))
