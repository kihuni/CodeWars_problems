
"""
Using python, Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width.

Here are the rules:

Use spaces to fill in the gaps between words.
Each line should contain as many words as possible.
Use '\n' to separate lines.
Last line should not terminate in '\n'
'\n' is not included in the length of a line.
Gaps between words can't differ by more than one space.
Lines should end with a word not a space.
Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
Last line should not be justified, use only one space between words.
Lines with one word do not need gaps ('somelongword\n').

Example with width=30:

"""






def justify_text(text, width):
    words = text.split()
    lines = []
    current_line = words[0]
    
    for word in words[1:]:
        if len(current_line) + len(word) + 1 > width:
            lines.append(current_line)
            current_line = word
        else:
            current_line += ' ' + word
    
    lines.append(current_line)
    
    justified_lines = []
    for line in lines:
        if len(line.split()) > 1:
            words = line.split()
            total_spaces = width - sum(len(word) for word in words)
            num_gaps = len(words) - 1
            spaces_per_gap = total_spaces // num_gaps
            extra_spaces = total_spaces % num_gaps
            
            justified_line = words[0]
            for i in range(1, len(words)):
                justified_line += ' ' * (spaces_per_gap + 1)
                if i <= extra_spaces:
                    justified_line += ' '
                justified_line += words[i]
            
            justified_lines.append(justified_line)
        else:
            justified_lines.append(line)
    
    return '\n'.join(justified_lines)
