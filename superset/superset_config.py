SECRET_KEY = '21d6b15514174940a34cf9b37e1e4152c1f137de33d0598d161860e112a94b43'


BABEL_DEFAULT_LOCALE = "pt_BR"
BABEL_DEFAULT_TIMEZONE = "America/Sao_Paulo"

LANGUAGES = {
    "pt_BR": {
        "flag": "br",
        "name": "Português (Brasil)"
    },
    "en": {
        "flag": "us",
        "name": "English"
    }
}

D3_FORMAT = {
    "decimal": ",",
    "thousands": ".",
    "grouping": [3],
    "currency": ["R$", ""],
}


D3_TIME_FORMAT = {
    "dateTime": "%d/%m/%Y %H:%M:%S",
    "date": "%d/%m/%Y",
    "time": "%H:%M:%S",
    "periods": ["AM", "PM"],
    "days": ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"],
    "shortDays": ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"],
    "months": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
    "shortMonths": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
}