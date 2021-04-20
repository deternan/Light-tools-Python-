from tika import parser
import os, re, json

pdf_dir = 'pdf'
output_dir = 'output'
paper_abstract = 'paper_abstract'

os.makedirs(output_dir, exist_ok=True)
paper_abstract = open(os.path.join(output_dir, paper_abstract), 'w', encoding='utf-8')

# get abstract part only from content
def get_Abstract(content):
    _content = re.split('\n(Abstract|ABSTRACT)[ .\n—]+', content)
    if len(_content) > 1:
        _content = _content[2]
        
        abstract = re.split("\n[1. ]*(Introduction|INTRODUCTION|Background|BACKGROUND)", _content)[0]
        return abstract
    else:
        return ''

# get content txt file and process
def process_pdf(pdf_file):
    pdf_name = pdf_file.rsplit('\\', 1)[1].split('.')[0]
    print("Process {{{}}} ...".format(pdf_file))
    txt_file = os.path.join(output_dir, "txt_{}.txt".format(pdf_name))
    
    if not os.path.exists(txt_file):
        raw_dict = parser.from_file(pdf_file)
        content = raw_dict["content"]
        cf = open(txt_file, 'w', encoding='utf-8')
        cf.write(content)
        cf.close()
    else:
        content = open(txt_file, 'r', encoding='utf-8').read()

    # you can modify from here
    abstract = get_Abstract(content)
    paper_abstract.write(abstract+'\n')

for pdf_file in os.listdir(pdf_dir):
    process_pdf(os.path.join(pdf_dir, pdf_file))

paper_abstract.close()
