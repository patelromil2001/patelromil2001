#!/usr/bin/env python3
import random
heights = [random.randint(30,110) for _ in range(24)]
svg = '<?xml version="1.0" encoding="UTF-8"?>\n'
svg += '<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="200" viewBox="0 0 1000 200'>\n'
svg += '<rect width="100%" height="100%" fill="transparent"/>\n'
svg += '<defs>\n  <linearGradient id="grad" x1="0" y1="0" x2="0" y2="1">\n    <stop offset="0%" stop-color="#7c3aed" stop-opacity="1" />\n    <stop offset="100%" stop-color="#00d4ff" stop-opacity="1" />\n  </linearGradient>\n</defs>\n'
x = 20
for h in heights:
    svg += f'<g transform="translate({x},80)">\n'
    svg += f'  <rect x="0" y="{120-h}" width="28" height="{h}" rx="4" fill="url(#grad)"/>\n'
    svg += f'  <rect x="4" y="{122-h}" width="20" height="{h-6}" rx="3" fill="rgba(0,0,0,0.08)"/>\n'
    svg += '</g>\n'
    x += 38
svg += '</svg>\n'
open('assets/skyline.svg','w',encoding='utf-8').write(svg)
print("skyline.svg generated at assets/skyline.svg")
