import prodigy
from prodigy.components.loaders import JSONL

global_css = """
    .header {
        background-color: rgb(88, 63, 207);
        color: white;
        font-weight: 600;
        font-size: 1.1em;
        padding: 8px;   
    }
    .prodigy-content {
        text-align: left !important;
    }
"""

html_template = """
<div class="prodigy-content header">Text for summarization</div>
<div class="prodigy-content">{{text}}</div>
<h4 style='text-align:left;color:#583fcf;margin-bottom:0;padding:0 20 0 20px;'>Accept or reject the following summary:</h4>
<div class="prodigy-content">{{option.value}}</div>
"""

@prodigy.recipe("my-choice-binary")
def my_choice(dataset: str, source: str):

    stream = JSONL(source)

    return {
        "dataset": dataset,
        "view_id": "html",
        "stream": stream,
        "config": {
            "custom_theme" : {
                "cardMaxWidth" : "70%",  # optional
                "cardTextAlign" : "left", # This one is not working
            },
            "buttons" : [
                "accept",
                "reject",
                # "ignore"
                "undo"
            ],
            "html_template" : html_template,
            "global_css" : global_css,
        }
    }
