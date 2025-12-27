#!/usr/bin/env python3
"""
Emoji Logger: Because reading 'ERROR' is so 2010.
Turns boring log levels into expressive emojis.
"""

import sys
import re
from datetime import datetime

# Emoji mapping - because emotions > words
EMOJI_MAP = {
    'DEBUG': '🔍',    # Sherlock Holmes mode
    'INFO': '💬',     # Just chatting
    'WARNING': '⚠️',  # Mild concern
    'ERROR': '💥',    # Things went boom
    'CRITICAL': '🚨', # Full panic mode
    'FATAL': '☠️',    # It's dead, Jim
}

# Color codes for terminal rainbows
COLORS = {
    'DEBUG': '\033[90m',     # Gray - like your debugging hopes
    'INFO': '\033[94m',      # Blue - calm waters
    'WARNING': '\033[93m',   # Yellow - caution tape
    'ERROR': '\033[91m',     # Red - alarm bells
    'CRITICAL': '\033[41m',  # Red background - panic!
    'FATAL': '\033[101m',    # Bright red - RIP
    'RESET': '\033[0m',
}


def emojify_line(line):
    """Turn boring log levels into party emojis."""
    for level, emoji in EMOJI_MAP.items():
        # Find log level patterns (case-insensitive, with brackets or spaces)
        pattern = rf'\b{level}\b'
        if re.search(pattern, line, re.IGNORECASE):
            color = COLORS.get(level, COLORS['INFO'])
            reset = COLORS['RESET']
            
            # Replace first occurrence with emoji + colored level
            line = re.sub(pattern, f'{emoji} {color}{level}{reset}', line, count=1, flags=re.IGNORECASE)
            break
    return line


def main():
    """Main function - where the magic (and emojis) happen."""
    print(f"{COLORS['INFO']}📢 Emoji Logger activated! Pipe logs through me or pass a filename.{COLORS['RESET']}")
    
    if len(sys.argv) > 1:
        # Read from file
        try:
            with open(sys.argv[1], 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"{COLORS['ERROR']}💥 File not found: {sys.argv[1]}{COLORS['RESET']}")
            return
    else:
        # Read from stdin (pipe mode)
        lines = sys.stdin.readlines()
    
    # Process and print each line with emoji goodness
    for line in lines:
        print(emojify_line(line.rstrip('\n')))


if __name__ == '__main__':
    main()
