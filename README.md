
# Basic edits:

For developing this site: 
https://docs.getpelican.com/en/latest/quickstart.html

For seeing a demo version while editing:
`pelican --listen --autoreload`
https://mirekdlugosz.com/blog/2021/improving-pelican-website-development-loop/

For uploading to github pages we use ghp-import
`ghp-import output -b gh-pages`
`git push origin gh-pages`
https://github.com/getpelican/pelican/blob/main/docs/tips.rst#publishing-a-project-site-to-github-pages-from-a-branch


# To add youtube videos to pages:

If your video URL is: https://www.youtube.com/embed/IBdQ2YPidnk

Then use the following:
<div class="youtube" align="center">
<iframe width="600" height="375" src="https://www.youtube.com/embed/IBdQ2YPidnk?cc_lang_pref=en&cc_load_policy=1" frameborder="0"></iframe>
</div>