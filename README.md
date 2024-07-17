# Structure

The `main` branch contains:
- the raw website content (in Markdown)
- the website format (in Python, using Pelican)

The `gh-pages` branch contains
- the generated website (in HTML)

The `gh-pages` branch is then published to GitHub pages with a custom domain.


# Workflow for editing and publishing changes:

## Standard workflow

1) Pull the `main` branch locally (unless you're editing in the browser mode)

`git pull`

2) Make your edits, review locally

For seeing a demo version while editing:
`pelican --listen --autoreload`
https://mirekdlugosz.com/blog/2021/improving-pelican-website-development-loop/

3) Commit changes and push raw website content changes and formatting to the remote `main` branch

`git commit -a -m "description of my changes"`
`git push`

4) Generate the HTML content in the output directory

`pelican content -o output -s pelicanconf.py`

5) Push generated website HTML to the `gh-pages` branch and then that branch to GitHub

`ghp-import output -b gh-pages`
`git push origin gh-pages`

## More info
More documentation can be found in the [Pelican github pages docs](https://github.com/getpelican/pelican/blob/main/docs/tips.rst#publishing-a-project-site-to-github-pages-from-a-branch)

https://docs.getpelican.com/en/latest/quickstart.html


# Other information:

## To add youtube videos to pages:

If your video URL is: https://www.youtube.com/embed/IBdQ2YPidnk

Then use the following:
```
<div class="youtube" align="center">
<iframe width="600" height="375" src="https://www.youtube.com/embed/IBdQ2YPidnk?cc_lang_pref=en&cc_load_policy=1" frameborder="0"></iframe>
</div>
```
