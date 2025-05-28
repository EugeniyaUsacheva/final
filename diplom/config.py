main_url = 'https://www.kinopoisk.ru/'
api_url = 'https://api.kinopoisk.dev/'
cookie_string = 'yashr=8135859951739259937; yandexuid=5372576431739259938; my_perpages=%5B%5D; mda_exp_enabled=1; yandex_login=ar233223AR; L=Y0NGCUhOagEARwlAVAluTEFCfnRXfGEGKAVYBl50ZVg2BQ==.1739280731.16051.366706.6e6f3ca8b7d89eaa1fe00972f57dfec8; _ym_uid=1740395433592881038; stars_sort_v5=01.170.10.70.181; mustsee_sort_v5=01.10.200.21.31.41.121.131.51.61.71.81.91.101.111; _csrf=Qc-NejF6z6ekuUwEzASg7pgI; disable_server_sso_redirect=1; _yasc=rryk4ASCOz+3M2P+bBvPj4dGsoNEyJ92lfYxmTDtpl69127XMBrmgsrvrvRNQiSeRQ==; ya_sess_id=3:1747506092.5.0.1739280731366:_QxyvA:e190.1.2:1|860337910.-1.2.3:1739280731|30:10234849.794070.L-H5UCEGmrfRl7nwTI_ejbAwmHU; sessar=1.1202.CiCUZbw18NH2FhDox2ppg6h-cvs7i23aytYL9B8J8lLIiw.t6aEOBr8Y6ah0XaDi6vQnPJWQs-G8Ec_NTykheGTAsk; ys=udn.cDphcjIzMzIyM0FS#c_chck.1756353043; i=rxFa+VBYaTmk+7hV/qc+WsbP8tmn7UmssU2yOE8/EVADG64eqdYMfo/Y22xtVGuvqOJHG7XFJIDyAuta6HZNNYZv9dI=; mda2_beacon=1747506092391; sso_status=sso.passport.yandex.ru:synchronized; no-re-reg-required=1; desktop_session_key=5272be151072f6ea419fc4597a43d4c7c4f6c93ef9a8a788ee7ea1257bd5e9bd584c18fd7ba6fca7a60e43da477a1b48da02d5ff42b9cd9f06e8c1e91ea8d9a00f2c3e99d7b5ef16145d635c812503325cd8b126b6ee5f2417115b95e1463b33bcb43f33a9d03dd115e3276789df07ce; desktop_session_key.sig=QcQiq5UKj7SVd7cu6hclu4vrdjM; sgst=movie-6440213; location=1; kpunk=1; _ym_d=1747506114'
def parse_cookies(cookie_string):
    cookies = []
    for cookie in cookie_string.split(';'):
        name, value = cookie.strip().split('=', 1)
        cookies.append({'name': name, 'value': value, 'path': '/'})
    return cookies

cookies = parse_cookies(cookie_string)
