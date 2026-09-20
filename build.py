# -*- coding: utf-8 -*-
"""Generuje site/kasia/index.html i site/zosia/index.html z template.html"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
TO = "stasiu2626@gmail.com"     # tu przychodzą powiadomienia z formularza
SIGN = "Łukasz"                  # podpis pod życzeniami

PEOPLE = {
    "kasia": dict(
        NAME="Kasia", VOC="Kasiu", SLUG="kasia",
        SISTER="Zosia", SISTER_INSTR="Zosią",
        WISHES="""
<p>Kasiu, trzydzieści lat to nie jest żadna granica — to raczej moment, w którym wreszcie wiadomo, co się lubi, a na co szkoda czasu. Życzę Ci, żeby ten nowy rozdział kręcił się w Twoim tempie: wolno, kiedy potrzebujesz oddechu, i szybko, kiedy masz plan.</p>
<p>Żebyś miała odwagę wycentrować to, co dla Ciebie ważne, i nie bała się, że coś się rozjedzie — z gliny zawsze da się ulepić coś nowego. Zdrowia, śmiechu do łez, ludzi, przy których jesteś w stu procentach sobą, i przynajmniej jednego kubka własnej roboty, z którego będziesz rano pić kawę i myśleć: „sama to zrobiłam”.</p>
<p>Sto lat!</p>
""".strip(),
    ),
    "zosia": dict(
        NAME="Zosia", VOC="Zosiu", SLUG="zosia",
        SISTER="Kasia", SISTER_INSTR="Kasią",
        WISHES="""
<p>Zosiu, na trzydziestkę życzę Ci tego, co garncarze wiedzą od pięciu tysięcy lat: że najważniejsze jest nie to, jak szybko kręci się koło, tylko jak spokojne są ręce. Żebyś miała ten spokój — w pracy, w domu, w głowie.</p>
<p>Życzę Ci pomysłów, które warto realizować, ludzi, którzy trzymają kciuki naprawdę, i zdrowia, żeby to wszystko udźwignąć. Niech ten rok będzie z tych, które się potem wspomina. I niech Twoja pierwsza miska wyjdzie choć trochę mniej krzywa niż Kasi (ale to zostanie między nami).</p>
<p>Sto lat!</p>
""".strip(),
    ),
}

tpl = open(os.path.join(BASE, "template.html"), encoding="utf-8").read()
tpl = tpl.replace("Zdjęcia: Unsplash (Quino Al, Alex Jones, Tom Crew, Earl Wilcox, Courtney Cook, Andrew Neel).", "Zdjęcia: Unsplash.")

for slug, d in PEOPLE.items():
    d = dict(d, TO=TO, SIGN=SIGN)
    html = tpl
    for k, v in d.items():
        html = html.replace("{{%s}}" % k, v)
    left = re.findall(r"{{\w+}}", html)
    assert not left, left
    out = os.path.join(BASE, "docs", slug)
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)
    print("ok", out)

# strona główna repo – nic nie zdradza
open(os.path.join(BASE, "docs", "index.html"), "w", encoding="utf-8").write(
    '<!DOCTYPE html><meta charset="utf-8"><meta name="robots" content="noindex"><title>🎁</title>'
    '<body style="font-family:Georgia;display:grid;place-items:center;height:100vh;margin:0;background:#e7e1db;color:#3a2e28">'
    '<p>Hmm, ten link nie jest kompletny. Poproś o właściwy 😉</p></body>')
open(os.path.join(BASE, "docs", ".nojekyll"), "w").close()
