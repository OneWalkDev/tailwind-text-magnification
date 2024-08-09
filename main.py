import re

def multiply_tailwind_text_size(html_content, multiplier=1.5):
    pattern = r'text-\[(\d+)px\]'
    

    def replace_function(match):
        original_value = int(match.group(1))
        new_value = int(original_value * multiplier)
        return f'text-[{new_value}px]'
    
    modified_content = re.sub(pattern, replace_function, html_content)
    
    return modified_content

input_file = './input/index.html'
output_file = './output/index.html'

with open(input_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

modified_content = multiply_tailwind_text_size(html_content)

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(modified_content)

print(output_file)