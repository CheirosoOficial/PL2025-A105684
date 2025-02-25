import re
import json

# Abrir ficheiro
def open_file(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    message = f.read()
    f.close()
    return message


# converts all .md headers into .html headers
def header_md_html(line):
    # if # ... then <h1></h1>   if ## ... then <h2></h2>   if ...
    pattern_header = r'(#+)\s*(.+)'

    def replace_header(match):
        return f'<h{len(match.group(1))}>{match.group(2)}</h{len(match.group(1))}>'

    return re.sub(pattern_header, replace_header, line)
# converts all .md fonts into .html fonts
def font_md_html(line):
    # if *w* then <i></i>   if **w** then <b></b>
    pattern_bold = r'(\*+)([^*]+)(\*+)'

    def replace_bold(match):
        if match.group(1) == '**': return f'<b>{match.group(2)}</b>'
        else: return f'<i>{match.group(2)}</i>'

    return re.sub(pattern_bold, replace_bold, line)
# converts all .md lists into .html lists
def list_md_html(md_text):
    lines = md_text.split("\n")
    html_lines = []
    in_list = False

    for line in lines:
        match = re.match(r'^\s*\d+\.\s*(.+)', line)
        if match:
            if not in_list:
                html_lines.append("<ol>")
                in_list = True
            html_lines.append(f"<li>{match.group(1)}</li>")
        else:
            if in_list:
                html_lines.append("</ol>")
                in_list = False
            html_lines.append(line)

    if in_list:
        html_lines.append("</ol>")

    return "\n".join(html_lines)
# converts all .md links into .html links
def link_md_html(line):
    # if ![] then image <img src="http://www.coellho.com" alt="imagem dum coelho"/>
    # if [] then link <a href="http://www.uc.pt">página da UC</a>
    pattern_link = r'(!?\[)([^\[\]\n]+)\]\(([^)\n]+)\)'

    def replace_link(match):
        if match.group(1) == '![': return f'<img src="{match.group(3)}" alt="{match.group(2)}">'
        else: return f'<a href="{match.group(3)}">{match.group(2)}</a>'

    return re.sub(pattern_link, replace_link, line)



def convert_md_html(filename):
    line = open_file(filename)
    after_header_proc = header_md_html(line)
    after_font_proc = font_md_html(after_header_proc)
    after_link_proc = link_md_html(after_font_proc)
    finished = list_md_html(after_link_proc)

    file_message = "<!DOCTYPE html>\n<html lang=\"en\">\n<body>" + finished + "\n</body>\n</html>"
    f = open("src/result.html", 'w+', encoding='utf-8')
    f.write(file_message)


convert_md_html("src/Test.md")