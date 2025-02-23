import os
import glob


for file in sorted(glob.glob('_columns/The_Short_Side/*.md')):
    slag = os.path.basename(file)[:-3]
    print(file)
    with open(file, 'r+') as f:
        content = f.read()
        parts = content.split('---')
        parts[1] += f'origin_url: https://www.investors.com/research/the-short-side/{slag}\n'
        content = '---'.join(parts)
        f.seek(0)
        f.write(content)
    # break
