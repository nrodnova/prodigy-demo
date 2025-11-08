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

@prodigy.recipe("my-choice")
def my_choice(dataset: str, source: str):

    stream = JSONL(source)

    return {
        "dataset": dataset,
        "view_id": "blocks",
        "stream": stream,
        "config": {
            "choice_style": "single",  # or "multiple"
            "choice_auto_accept": False,
            "custom_theme" : {
                "cardMaxWidth" : "70%",  # optional
                "cardTextAlign" : "left" # This one is not working
            },
            "global_css" : global_css,
            "blocks" : [
                {"view_id" : "html", "html_template" : "<div class='header'>Text for summarization</div>"},
                {"view_id" : "text"},
                {"view_id" : "html", "html_template" : "<h4 style='text-align:left;color:#583fcf;margin-bottom:0;padding:0 20 0 20px;'>Select the best summary:</h4>"},
                {"view_id" : "choice", "text" : None},
            ],
        }
    }
