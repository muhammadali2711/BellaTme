import json
from collections import OrderedDict

from api.v1.pages.texts import Texts
from base.formats import format_ctg, format_partner, format_why, format_sifat, format_rate, format_teacher
from bmain.models import *


def header(lang='en'):
    return OrderedDict([
        ('course', {
            'uz': "Kurslar",
            'ru': "Курсы",
            'en': "Courses",

        }[lang]),
        ('teacher', {
            'uz': "O'qituvchilar",
            'ru': "Учителя",
            'en': "Teachers",

        }[lang]),
        ('prices', {
            'uz': "Narxlar",
            'ru': "Цены",
            'en': "Prices",
        }[lang]),
        ('vacancy', {
            'uz': "Vakansiyalar",
            'ru': "Вакансии",
            'en': "Vacancy",
        }[lang]),

        ('bron', {
            'uz': "Kursni tanlash",
            'ru': "Забронировать урок",
            'en': "Ranging the lesson",
        }[lang]),

    ])


def sifat(lang):
    sifat_teen = [format_sifat(x, lang) for x in Sifat.objects.filter(is_active=True, type=2)[:6]]
    sifat_kid = [format_sifat(x, lang) for x in Sifat.objects.filter(is_active=True, type=1)[:6]]

    btns = {
        "kids": {
            "uz": "Bolalar uchun",
            "ru": "Для детей",
            "en": "For kids",
        }[lang],
        "teens": {
            "uz": "O'smirlar uchun",
            "ru": "Для взрослых",
            "en": "For Teens",
        }[lang],
    }

    return OrderedDict([
        ("caption", Texts['sifat-cap'][lang]),
        ('btns', btns),
        ("teen", sifat_teen),
        ("kid", sifat_kid),
    ])


def parents(lang):
    rate = [format_rate(x) for x in Rating.objects.all()[:10]]

    return OrderedDict([
        ("caption", Texts['rate-cap'][lang]),
        ("rate", rate),
    ])


def partners(lang):
    partners = [format_partner(x) for x in Partner.objects.all()]

    return OrderedDict([
        ("caption", Texts['partner_cap'][lang]),
        ("desc", Texts['partner_decs'][lang]),
        ("all", partners),
    ])


def probniy(lang):
    prob = {
        "1": {
            "uz": "O'qituvchi bilan tanishuv",
            "ru": "Познакомим с учителем",
            "en": "Getting to know the teacher",
        },
        "2": {
            "uz": "Bilim darajasini aniqlash",
            "ru": "Определим уровень знаний",
            "en": "Determine the level of knowledge",
        },
        "3": {
            "uz": "O'quv rejasini tanlanadi",
            "ru": "Подберем программу обучения",
            "en": "The curriculum is selected",
        },

        "def": {
            "uz": "Sinov darsida nimalar bo'ladi",
            "ru": "Что будет на пробном уроке:",
            "en": "What will happen in the trial lesson:",
        }}

    return OrderedDict([
        ("caption", Texts['prob_cap'][lang]),
        ("desc", prob['def'][lang]),
        ("1", prob["1"][lang]),
        ("2", prob["2"][lang]),
        ("3", prob["3"][lang]),
    ])


def why(lang):
    all = [format_why(x, lang) for x in Why.objects.filter(is_active=True)[:4]]

    return OrderedDict([
        ("caption", Texts['why_cap'][lang]),
        ('all', all)
    ])


def about_course(lang='en'):
    all = [format_teacher(x, lang, about=True) for x in AboutCourse.objects.all().order_by("-pk")[:10]]

    return OrderedDict([
        ("caption", Texts['our_course_cap'][lang]),
        ('all', all)
    ])


def about_vac(lang='en'):
    all = [format_teacher(x, lang, about=True) for x in AboutVacancy.objects.all().order_by("-pk")[:3]]

    return all


def teachers(lang='en'):
    all = [format_teacher(x, lang) for x in Teacher.objects.all()]

    return OrderedDict([
        ("caption", {
            'uz': "O'qituvchilar",
            'ru': "Учителя",
            'en': "Teachers",

        }[lang]),
        ("video", {
            "uz": "Video Tanishuv",
            "ru": "Видео приветствие",
            "en": "Greeting on video",
        }[lang]),
        ('bron', {
            'uz': "Kursni tanlash",
            'ru': "Забронировать урок",
            'en': "Ranging the lesson",
        }[lang]),
        ('all', all)
    ])


def page_vacancy(lang='en'):
    work = {
        "caption": Texts['online_work'][lang],
    }
    online_work = OnlineWork.objects.all().order_by("-pk")[:1]
    if online_work:
        work['desc'] = online_work[0].desc
        work['img'] = online_work[0].img.url

    return OrderedDict([
        ("header", header(lang)),
        ("online_work", work),
        ("resume", Texts['SendResume'][lang]),
        ("about_vac", about_vac(lang))

    ])


def page_teacher(lang="en"):
    return OrderedDict([
        ("header", header(lang)),
        ("teacher", teachers(lang)),

    ])


def page_index(lang="en"):
    first = {
        "first": Texts['first']['menu'][lang],
        "1": Texts['first']['1'][lang],
        "2": Texts['first']['2'][lang],
        "3": Texts['first']['3'][lang],
        "4": Texts['first']['4'][lang],
        "try": Texts['first']['try_free'][lang],
    }

    ctgs = [format_ctg(x, lang) for x in (Category.objects.filter(is_main=True).order_by('-pk')[:5])]

    not_main = [format_ctg(x, lang) for x in Category.objects.filter(is_main=False).order_by('-pk')[:5]]
    inf = {
        "name": {
            "uz": "Ism",
            "en": "Name",
            "ru": "Имя",
        }[lang],
        "phone": {
            "ru": "Телефон",
            "uz": "Telefon",
            "en": "Phone",
        }[lang]
    }

    return OrderedDict([
        ('header', header(lang)),
        ('ctgs', ctgs),
        ("first", first),
        ("video_cap", Texts['video_cap'][lang]),
        # ("not_main", not_main),
        # ("subs", subs"),
        ('why', why(lang)),
        ('sifat', sifat(lang)),
        ('parents', parents(lang)),
        ('probniy', probniy(lang)),
        ('inf', inf),
        ("about_course", about_course(lang)),

        ('partners', partners(lang)),

    ])
