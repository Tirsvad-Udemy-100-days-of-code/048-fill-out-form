[English](Step-2-Search) · **Dansk** · [Bahasa Malaysia](Step-2-Search-ms)

# Trin 2: Skriv i et felt og tryk på Enter

## Lektionen

Lektionen skriver "Python" i Wikipedias søgefelt. Feltet findes via dets `name`-attribut, teksten skrives med `send_keys`, og specialtasten Enter sendes med klassen `Keys` fra `selenium.webdriver.common.keys`, hvilket udfører søgningen.

## Koden

```python
def search_for(browser, term=SEARCH_TERM):
    search_input = browser.find_element(BY_NAME, SEARCH_INPUT_NAME)
    search_input.send_keys(term)
    search_input.send_keys(KEY_ENTER)
```

`KEY_ENTER` har samme værdi som `Keys.ENTER`, også sikret af en enhedstest.

## Hvad browseren viser

![Wikipedia-artiklen "Python" efter søgningen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/raw/branch/main/docs/images/step-2-search.png)

## Det lærte vi

- `By.NAME` finder et felt via dets `name`-attribut.
- `send_keys` skriver tekst i et felt og sender også specialtaster som Enter.
- Når man sender Enter, udføres en søgning som en person ville gøre det, uden at finde en søgeknap.
