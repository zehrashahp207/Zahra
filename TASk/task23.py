from jinja2 import Template

template = Template("Salam, {{ ad }}!")
nəticə = template.render(ad="Nicat")

print(nəticə)