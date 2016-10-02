# William theme for Pelican static site generator


"William" is a theme for [Pelican static site generator](http://getpelican.com/). It is mobile/responsive oriented using a single column layout. It combines a bold typography with pristine graphical elements and restrained content placement. 

William is heavily based on [Martin-Pelican](https://github.com/cpaulik/martin-pelican), which is a port for Pelican of [Allison House](http://allison.house/)'s HTML theme ["Martin"](https://github.com/house/martin). The original description clarifies the naming of the themes:

> Showcase your project in style with Martin, a bold, timeless theme for GitHub pages! Named for the punchcutter William Martin, apprentice to John Baskerville.

## Licence

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0) License](http://creativecommons.org/licenses/by-sa/3.0/).


## Features and usage

This is a non-exhaustive list of features of the theme with example configuration snippets to put in `pelicanconf.py`:


- Define the menu with `MENUITEMS`. In addition, enable  `DISPLAY_PAGES_ON_MENU` to add all pages or `DISPLAY_CATEGORIES_ON_MENU` to add all categories to the menu.

    ```
    MENUITEMS = [
        ("My blog", '/index.html'),
        ('Tags', '/tags.html'),
        ('About', '/pages/about.html'),
    ]
    DISPLAY_PAGES_ON_MENU = False
    DISPLAY_CATEGORIES_ON_MENU = False
    ```
    
- [Slicknav](http://slicknav.com/) for compact menu on mobile. Enable by setting configuration variable `ENABLE_SLICKNAV`

    ```
    ENABLE_SLICKNAV = True
    ```

- Google Analytics: use the configuration variable `GOOGLE_ANALYTICS` to set your Google Analytics ID.

    ```
    GOOGLE_ANALYTICS = 'UA-XXXX-YYYY'
    ```

- [Disqus](http://www.disqus.com) integration: use the configuration variable setting the variable `DISQUS_SITENAME`

    ```
    DISQUS_SITENAME = "your_site_name"
    ```

- Use `HEAD_EXTRA` to inject customisation elements into HTML head. 
    - For example to set up favicon/apple-touch-icon (stored under `content/extra/`):
    
        ```
        STATIC_PATHS = [
            'extra/favicon.ico',
            'extra/apple-touch-icon.png',
        ]
        
        EXTRA_PATH_METADATA = {
            'extra/favicon.ico': {'path': 'favicon.ico'},
            'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
        }
        
        HEAD_EXTRA = u"""
            <link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48 64x64" type="image/vnd.microsoft.icon">
            <link rel="apple-touch-icon" href="/apple-touch-icon.png">
        """
        ```
    
