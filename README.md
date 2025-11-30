# ⚠️ Important notice! Because I want to bring this update out as soon as possible some features will be delayed ⚠️

### This is the source code for the YouTube alternative "glomble"!

Useful stuff to know:
- The code for profiles, videos, reports, etc. are stored in separate directories. These directories are also used for related things, for example the code that handles private messaging is stored in the profiles directory. 

- Frontend files are located within the separate directories, e.g. "videos/templates/videos/detail_video.html". Note: The "profiles" and "videos" directory both have a "base.html" file, this is unintentional and should be combined into one later on.

- The most important backend files are usually views.py, models.py, and urls.py. Views.py is for interaction between frontend and backend, models.py is for the database structure, and urls.py is used for assigning urls to views to access them. Another important backend file is "videos/templatetags/count.py", this is used for making 

If you're seeing this text it means I forgot to finish writing this readme before making pushing the update, whoops.