[English](Home) · [Dansk](Home-da) · **Bahasa Malaysia**

# Hari 48: Isi borang dengan Selenium

Projek ini menyelesaikan pelajaran hari ke-48 dalam "100 Days of Code: The Complete Python Pro Bootcamp" di Udemy. Pelajaran ini menunjukkan bagaimana Selenium WebDriver berinteraksi dengan sebuah laman: mengklik elemen, menaip ke dalam medan input, menghantar kekunci khas dan mengisi borang.

## Apa yang anda peroleh daripada setiap langkah

| Langkah | Topik pelajaran | Fungsi | Apa yang anda peroleh |
| --- | --- | --- | --- |
| 1 | Klik pautan, cari melalui teksnya | `click_link_by_text` | Menavigasi tanpa tetikus |
| 2 | Taip ke dalam input dan hantar kekunci Enter | `search_for` | Mengisi input dan menghantar dengan kekunci khas |
| 3 | Cabaran: isi borang dan klik butang | `fill_out_form` | Menggabungkan pemilih, penaipan dan klik |

- [Langkah 1: Klik pautan](Step-1-Link-Click-ms)
- [Langkah 2: Cari](Step-2-Search-ms)
- [Langkah 3: Borang](Step-3-Form-ms)

## Jalankan

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m fill_out_form
```

README repositori mengandungi arahan lengkap, ujian dan larian Docker yang tidak pernah menyentuh desktop anda.
