import dash_mantine_components as dmc
from dash import html

from app import app
from .title import SubText, Title


def OnlyCodeBlock(code):
    return dmc.Prism(code=code, language="python", class_name="space-below-10")


def OnlyComponentBlock(components):
    return dmc.Paper(
        components, withBorder=True, padding="xl", class_name="space-below-10"
    )


def ComponentBlock(code, title="", caption=""):
    scope = {"app": app}
    code_to_display = code.replace("component = ", "", 1)
    try:
        exec(code, scope)
    except Exception as e:
        print("=============================================")
        print(f"Error running: \n{code}")
        raise e

    return html.Div(
        [
            Title(title),
            SubText(caption),
            OnlyComponentBlock([scope["component"]]),
            OnlyCodeBlock(code_to_display),
            dmc.Space(h=40),
        ]
    )
