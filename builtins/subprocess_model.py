import subprocess

ret = subprocess.Popen(["mv", "script_html2pdf_bak", "script_html2pdf"])

print(ret)
