import os
import re
from pathlib import Path

# Configuraciones
src_dir = Path(r"d:\JONATHAN\Proyectos\Servicios Logísticos JHT\Front_Jht_webLading\src\pages")
dest_dir_public = Path(r"d:\JONATHAN\Proyectos\Servicios Logísticos JHT\Front_Jht_webLading\jht_cms\templates\public")
dest_dir_status = Path(r"d:\JONATHAN\Proyectos\Servicios Logísticos JHT\Front_Jht_webLading\jht_cms\templates\service_status")

# Mapeo de archivos y aplicaciones
pages = {
    'index.html': {'dest': dest_dir_public, 'title': 'JHT Transport Company'},
    'servicios.html': {'dest': dest_dir_public, 'title': 'Servicios - JHT Transport'},
    'flota.html': {'dest': dest_dir_public, 'title': 'Nuestra Flota - JHT Transport'},
    'nosotros.html': {'dest': dest_dir_public, 'title': 'Nosotros - JHT Transport'},
    'contacto.html': {'dest': dest_dir_public, 'title': 'Contacto - JHT Transport'},
    'landing.html': {'dest': dest_dir_public, 'title': 'Landing - JHT Transport'},
    'rastreo.html': {'dest': dest_dir_status, 'title': 'Rastreo - JHT Transport', 'name': 'consulta.html'},
}

def extract_main_content(html):
    # Encontrar <main ...> y </main>
    match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ""

def process_links_and_assets(content):
    # Reemplazar urls
    content = content.replace('href="index.html"', 'href="{% url \'website:index\' %}"')
    content = content.replace('href="servicios.html"', 'href="{% url \'website:servicios\' %}"')
    content = content.replace('href="flota.html"', 'href="{% url \'website:flota\' %}"')
    content = content.replace('href="nosotros.html"', 'href="{% url \'website:nosotros\' %}"')
    content = content.replace('href="contacto.html"', 'href="{% url \'website:contacto\' %}"')
    content = content.replace('href="landing.html"', 'href="{% url \'website:landing\' %}"')
    content = content.replace('href="acceso.html"', 'href="{% url \'login\' %}"')
    content = content.replace('href="rastreo.html"', 'href="{% url \'service_status:consulta\' %}"')
    content = content.replace("window.location.href='rastreo.html'", "window.location.href='{% url \"service_status:consulta\" %}'")
    
    # Reemplazar assets
    # src="../assets/..."
    content = re.sub(r'src="\.\./assets/([^"]+)"', "src=\"{% static 'assets/\\1' %}\"", content)
    # href="../assets/..."
    content = re.sub(r'href="\.\./assets/([^"]+)"', "href=\"{% static 'assets/\\1' %}\"", content)
    # style="background-image: url('../assets/...')"
    content = re.sub(r"url\(['\"]\.\./assets/([^'\"]+)['\"]\)", "url('{% static 'assets/\\1' %}')", content)

    # Tambien podria haber src="assets/..."
    content = re.sub(r'src="assets/([^"]+)"', "src=\"{% static 'assets/\\1' %}\"", content)
    content = re.sub(r'href="assets/([^"]+)"', "href=\"{% static 'assets/\\1' %}\"", content)
    content = re.sub(r"url\(['\"]assets/([^'\"]+)['\"]\)", "url('{% static 'assets/\\1' %}')", content)

    # Replace \'  (si quedó alguno por accidente)
    content = content.replace("\\'", "'")
    return content

for file_name, info in pages.items():
    src_file = src_dir / file_name
    if not src_file.exists():
        print(f"No encontrado: {src_file}")
        continue
        
    with open(src_file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    main_content = extract_main_content(html)
    processed_content = process_links_and_assets(main_content)
    
    dest_name = info.get('name', file_name)
    dest_file = info['dest'] / dest_name
    
    final_template = f"""{{% extends "base/base.html" %}}
{{% load static %}}

{{% block title %}}{info['title']}{{% endblock %}}

{{% block content %}}
{processed_content}
{{% endblock %}}
"""
    
    with open(dest_file, 'w', encoding='utf-8') as f:
        f.write(final_template)
    
    print(f"Procesado: {file_name} -> {dest_file}")
