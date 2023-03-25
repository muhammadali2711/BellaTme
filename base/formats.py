from collections import OrderedDict


def format_ctg(data, lang=None):
    if lang:
        return OrderedDict([
            ('id', data.id),
            ('slug', data.slug),
            ('content', data.content.get(lang, None)),
            ('is_main', data.is_main)
        ])
    else:
        return OrderedDict([
            ('id', data.id),
            ('slug', data.slug),
            ('content', data.content),
            ('is_main', data.is_main)
        ])


def format_partner(data):
    return OrderedDict([
        ('id', data.id),
        ('company', data.company),
        ('logo_url', data.logo.url),
        ('social', data.social)
    ])


def format_why(data, lang=None):
    return OrderedDict([
        ('id', data.id),
        ('title', data.title.get(lang) if lang else data.title),
        ('desc', data.desc.get(lang) if lang else data.desc),
        ('image', data.img.url),
        ('is_active', data.is_active),
    ])


def format_teacher(data, lang=None, about=None):
    name = data.name
    if about:
        name = data.name.get(lang) if lang else data.title
    return OrderedDict([
        ('id', data.id),
        ('name', name),
        ('desc', data.desc.get(lang) if lang else data.desc),
        ('image', data.img.url),
    ])


def format_sifat(data, lang=None):
    return OrderedDict([
        ('id', data.id),
        ('title', data.title.get(lang) if lang else data.title),
        ('desc', data.desc.get(lang) if lang else data.desc),
        ('type', "For teens" if data.type == 2 else "For kids"),
        ('is_active', data.is_active),
    ])


def format_rate(data):
    return OrderedDict([
        ('id', data.id),
        ('img', data.img.url),
        ('opinion', data.opinion),
        ('name', data.name),
        ('rating', data.rating),
    ])
