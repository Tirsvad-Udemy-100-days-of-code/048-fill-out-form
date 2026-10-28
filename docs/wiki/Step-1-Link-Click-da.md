[English](Step-1-Link-Click) · **Dansk** · [Bahasa Malaysia](Step-1-Link-Click-ms)

# Trin 1: Klik på et link via dets tekst

## Lektionen

Efter en gennemgang af, hvordan man finder elementer, viser lektionen, at et anchor-tag kan klikkes med metoden `.click()`, så browseren navigerer af sig selv i stedet for med et museklik. Derefter vises en genvej til links: find linket via den tekst, det viser, her "Content portals".

## Koden

```python
def click_link_by_text(browser, link_text=LINK_TEXT_CONTENT_PORTALS):
    browser.find_element(BY_LINK_TEXT, link_text).click()
```

`BY_LINK_TEXT` har samme værdi som Selenium's `By.LINK_TEXT`; en enhedstest sikrer det. Linkteksten står i `constants.py`.

## Hvad browseren viser

![Wikipedia-siden "Contents/Portals" efter klikket](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/raw/branch/main/docs/images/step-1-click-link.png)

## Det lærte vi

- Et link er et element som alle andre: find det, og kald `.click()`.
- `By.LINK_TEXT` finder et link via den synlige tekst, hvilket er enklere end en CSS-selektor.
- Efter klikket er browseren på en ny side; næste trin starter derfra.
