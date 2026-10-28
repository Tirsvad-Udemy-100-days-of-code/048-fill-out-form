[English](Step-3-Form) · **Dansk** · [Bahasa Malaysia](Step-3-Form-ms)

# Trin 3: Udfordring, udfyld en formular

## Lektionen

Udfordringen: udfyld en tilmeldingsformular med fornavn, efternavn og e-mailadresse, og klik derefter på knappen Sign Up. Nogle elementer har intet id eller navn, der er nemt at bruge, så lektionen peger på CSS-selektorer.

## Koden

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

## Hvad browseren viser

Formularen efter indtastning, før klikket:

![Tilmeldingsformularen udfyldt med Jane, Doe og en e-mailadresse](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/raw/branch/main/docs/images/step-3-form-filled.png)

Siden efter Sign Up. Demosiden kontrollerer e-mailadressen, og standardadressen `jane.doe@example.com` afvises. Kør programmet med din egen adresse (`--email dig@dittdomæne.dk`) for at se succes-siden:

![Demosiden svarer "Uh oh" på standardadressen example.com](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/raw/branch/main/docs/images/step-3-form-signed-up.png)

## Det lærte vi

- En CSS-selektor som `input[name='fName']` finder et element uden id.
- Trin 1 og 2 kombineres her: find, skriv, klik.
- En rigtig side kan svare uventet; skærmbilledet efter klikket viser, hvad der faktisk skete.
- Når selektorer står i `constants.py`, kræver en ændret side én rettelse i stedet for en søgning i koden.
