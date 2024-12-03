import json
import sys


def add_description(description):
    template = "<p data-l10n>$TEXT</p>"

    output = template.replace("$TEXT", description)

    return output


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Json file is needed")
        sys.exit(1)

    json_file = open(sys.argv[1])

    data = json.load(json_file)

    for item in data:
        print("creating status page for: " +item.get("http_code"))

        output_file = open("template.html", "r").read()

        output_file = output_file.replace("${MESSAGE}", item.get("message"))
        output_file = output_file.replace("${BUTTON_TEXT}", item.get("button_text"))
        output_file = output_file.replace("${BUTTON_LINK}", item.get("button_link"))
        output_file = output_file.replace("${HTTP_MESSAGE}", item.get("http_message"))
        output_file = output_file.replace("${HTTP_CODE}", item.get("http_code"))


        desc_ = ""
        for description in item.get("description"):
            desc_ = desc_ + add_description(description)

        output_file = output_file.replace("${DESCRIPTION}", desc_)

        # nfdi_webcomponents = open("nfdi-webcomponents.js", "r").read()
        # output_file = output_file.replace("${NFDI_NAVBAR}", nfdi_webcomponents)



        output = open("dst/" + item.get("http_code") +".html", "w")
        output.write(output_file)
        output.close()

