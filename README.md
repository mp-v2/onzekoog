# Structure

The `main` branch contains:
- the raw website content (in Markdown)
- the website format (in Python, using Pelican)

The `gh-pages` branch contains
- the generated website (in HTML)

This is then published to GitHub pages with a custom domain.


# Editing the website:

1) Pull the `main` branch locally (unless you're editing in the browser mode)
`git pull`
2) Make your edits, then commit the changes
`git commit -a -m "description of my changes"
3) Generate the HTML content in the output directory
`pelican content -o output -s pelicanconf.py`
4) Push changes to the remote `main` branch
`git push`
4) Publish website HTML to the `gh-pages` branch
`ghp-import output -b gh-pages`
`git push origin gh-pages`

For developing this site: 
https://docs.getpelican.com/en/latest/quickstart.html

For seeing a demo version while editing:
`pelican --listen --autoreload`
https://mirekdlugosz.com/blog/2021/improving-pelican-website-development-loop/

# For publishing changes to the website:

For uploading to github pages we use ghp-import
```
pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages
git push origin gh-pages
```
https://github.com/getpelican/pelican/blob/main/docs/tips.rst#publishing-a-project-site-to-github-pages-from-a-branch


# To add youtube videos to pages:

If your video URL is: https://www.youtube.com/embed/IBdQ2YPidnk

Then use the following:
<div class="youtube" align="center">
<iframe width="600" height="375" src="https://www.youtube.com/embed/IBdQ2YPidnk?cc_lang_pref=en&cc_load_policy=1" frameborder="0"></iframe>
</div>