[English](Step-1-Link-Click) · [Dansk](Step-1-Link-Click-da) · **Bahasa Malaysia**

# Langkah 1: Klik pautan melalui teksnya

## Pelajaran

Selepas mengulang kaji cara mencari elemen, pelajaran menunjukkan bahawa tag anchor boleh diklik dengan kaedah `.click()`, supaya pelayar bergerak sendiri dan bukan dengan klik tetikus. Kemudian diperkenalkan jalan pintas untuk pautan: cari pautan melalui teks yang dipaparkannya, di sini "Content portals".

## Kod

```python
def click_link_by_text(browser, link_text=LINK_TEXT_CONTENT_PORTALS):
    browser.find_element(BY_LINK_TEXT, link_text).click()
```

`BY_LINK_TEXT` mempunyai nilai yang sama dengan `By.LINK_TEXT` Selenium; ujian unit menjaganya. Teks pautan berada dalam `constants.py`.

## Apa yang dipaparkan pelayar

![Laman Wikipedia "Contents/Portals" selepas klik](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/raw/branch/main/docs/images/step-1-click-link.png)

## Apa yang kita peroleh

- Pautan ialah elemen seperti yang lain: cari, kemudian panggil `.click()`.
- `By.LINK_TEXT` mencari pautan melalui teks yang kelihatan, lebih mudah daripada pemilih CSS.
- Selepas klik, pelayar sudah berada di laman baharu; langkah seterusnya bermula dari situ.
