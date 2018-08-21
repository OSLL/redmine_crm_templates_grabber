# redmine_crm_templates_grabber

## Description

This tool solves one task - downloads a bunch of Redmine HelpDesk templates in a format, which allows to import them into Confluence without issues of cyrillic texts.

How does it work:
- login to Redmine using Selenium,
- save each page using Selenium,
- transform each page to Docx format using Pandoc. 

## Dependencies 

<pre>
sudo pip3 install selenium
sudo apt-get install pandoc firefox
</pre>

Download geckodriver from https://github.com/mozilla/geckodriver/releases and unpack to repo root. 

## Execution

<pre>
PATH="./:$PATH" python3 grabber.py --login LOGIN --password PASSWORD --project PROJECT --host HOST --start_id START_ID --end_id END_ID
</pre>
