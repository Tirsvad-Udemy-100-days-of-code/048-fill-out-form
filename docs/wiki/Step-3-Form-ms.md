[English](Step-3-Form) · [Dansk](Step-3-Form-da) · **Bahasa Malaysia**

# Langkah 3: Cabaran, isi borang

## Pelajaran

Cabarannya: isi borang pendaftaran dengan nama pertama, nama akhir dan alamat e-mel, kemudian klik butang Sign Up. Sesetengah elemen tidak mempunyai id atau nama yang mudah digunakan, jadi pelajaran menunjuk kepada pemilih CSS.

## Kod

```python
def fill_out_form(browser, form_data=None, before_submit=None):
    data = form_data if form_data is not None else default_form_data()
    browser.find_element(BY_CSS_SELECTOR, FIRST_NAME_SELECTOR).send_keys(data.first_name)
    browser.find_element(BY_CSS_SELECTOR, LAST_NAME_SELECTOR).send_keys(data.last_name)
    browser.find_element(BY_CSS_SELECTOR, EMAIL_SELECTOR).send_keys(data.email)
    if before_submit is not None:
        before_submit()
    browser.find_element(BY_CSS_SELECTOR, SIGN_UP_BUTTON_SELECTOR).click()
```

## Apa yang dipaparkan pelayar

Borang selepas menaip, sebelum klik:

![Borang pendaftaran diisi dengan Jane, Doe dan alamat e-mel](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/raw/branch/main/docs/images/step-3-form-filled.png)

Laman selepas Sign Up. Laman demo memeriksa alamat e-mel, dan alamat lalai `jane.doe@example.com` ditolak. Jalankan program dengan alamat anda sendiri (`--email anda@domainanda.com`) untuk melihat laman berjaya:

![Laman demo menjawab "Uh oh" kepada alamat lalai example.com](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/raw/branch/main/docs/images/step-3-form-signed-up.png)

## Apa yang kita peroleh

- Pemilih CSS seperti `input[name='fName']` mencari elemen yang tiada id.
- Langkah 1 dan 2 digabungkan di sini: cari, taip, klik.
- Laman sebenar boleh menjawab di luar jangkaan; tangkapan skrin selepas klik menunjukkan apa yang benar-benar berlaku.
- Menyimpan pemilih dalam `constants.py` bermakna laman yang berubah hanya memerlukan satu pembetulan, bukan mencari dalam kod.
