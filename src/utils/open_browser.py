import webbrowser


def open_browser():
    """
    The open_browser function opens the web browser in a separate thread.

    :return: None
    """

    webbrowser.open("http://localhost:8000")
