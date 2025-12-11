#!/usr/bin/env python3
import random
from datetime import datetime
svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1000" height="120" viewBox="0 0 1000 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00d4ff"/>
      <stop offset="50%" stop-color="#6a00ff"/>
      <stop offset="100%" stop-color="#ff0066"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="transparent"/>
  <g transform="translate(20,20)">
'''
box_w = 14
gap = 6
for week in range(0,26):
    for day in range(0,7):
        x = week*(box_w+gap)
        y = day*(box_w+gap)
        svg += f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_w}" rx="2" ry="2" fill="#0b1220" stroke="#111827" />\n'
svg += '<path id="snakePath" d="M5,5 '
coords = []
for week in range(0,26):
    for day in range(0,7):
        x = week*(box_w+gap) + box_w/2
        y = day*(box_w+gap) + box_w/2
        coords.append(f"L{x},{y}")
svg += " ".join(coords)
svg += '" fill="none" stroke="none"/>
'
svg += '<g><circle r="8" fill="url(#g)"><animateMotion dur="12s" repeatCount="indefinite"><mpath xlink:href="#snakePath" /></animateMotion></circle></g>\n'
svg += '</g>\n</svg>'
open('assets/snake.svg','w',encoding='utf-8').write(svg)
print("snake.svg generated at assets/snake.svg")
