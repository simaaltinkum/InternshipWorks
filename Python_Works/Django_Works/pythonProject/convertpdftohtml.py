from PDFNetPython import Convert, HTMLOutputOptions

filename = "PRO-FORMA - S00197 (2).pdf"
output_filename = "PRO-FORMA - S00197 (2)1.html"

htmlOutputOptions = HTMLOutputOptions()
htmlOutputOptions.SetContentReflowSetting(HTMLOutputOptions.e_reflow_full)

Convert.ToHtml(filename, output_filename, htmlOutputOptions)
