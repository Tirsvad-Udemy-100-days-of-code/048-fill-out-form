[English](Step-2-Search) · [Dansk](Step-2-Search-da) · **Bahasa Malaysia**

# Langkah 2: Taip ke dalam input dan tekan Enter

## Pelajaran

Pelajaran menaip "Python" ke dalam bar carian Wikipedia. Bar itu dicari melalui atribut `name`, teks ditaip dengan `send_keys`, dan kekunci khas Enter dihantar dengan kelas `Keys` daripada `selenium.webdriver.common.keys`, yang menghantar carian.

## Kod

```python
def search_for(browser, term=SEARCH_TERM):
    search_input = browser.find_element(BY_NAME, SEARCH_INPUT_NAME)
    search_input.send_keys(term)
    search_input.send_keys(KEY_ENTER)
```

`KEY_ENTER` mempunyai nilai yang sama dengan `Keys.ENTER`, juga dijaga oleh ujian unit.

## Apa yang dipaparkan pelayar

![Artikel Wikipedia "Python" selepas carian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/raw/branch/main/docs/images/step-2-search.png)

## Apa yang kita peroleh

- `By.NAME` mencari input melalui atribut `name`.
- `send_keys` menaip teks ke dalam input dan juga menghantar kekunci khas seperti Enter.
- Menghantar Enter membuat carian seperti yang dilakukan seseorang, tanpa mencari butang carian.
