def test_titulo_should_be_true_when_web_title_are_equals(page):
    page.goto("https://www.ucp.edu.ar/")
    titulo = page.title()
    assert "Universidad de la Cuenca del Plata -" == titulo