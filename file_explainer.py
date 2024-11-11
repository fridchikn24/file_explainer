%pip install -U -q "google-generativeai>=0.8.3"

import google.generativeai as genai
from IPython.display import HTML, Markdown, display

GOOGLE_API_KEY ='' #input google api key
genai.configure(api_key=GOOGLE_API_KEY)


file_contents = !curl https://raw.githubusercontent.com/magicmonty/bash-git-prompt/refs/heads/master/gitprompt.sh

explain_prompt = f"""
Please explain what this file does at a very high level. What is it, and why would I use it?

```
{file_contents}
```
"""

model = genai.GenerativeModel('gemini-1.5-flash-latest')

response = model.generate_content(explain_prompt)
Markdown(response.text)

