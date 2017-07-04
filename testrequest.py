import requests
string="""{
                "ENABLE_MKTG_SITE": false,
                "LANGUAGE_CODE": "es-CO",
                "PLATFORM_NAME": "eduNEXT Academy",
                "SITE_NAME": "demo.edunext.io",
                "TIME_ZONE_DISPLAYED_FOR_DEADLINES": "America/Bogota",
                "LAST_ACCESSED": "Tue Jun 13 08:19:44 CEST 2017",
                "course_about_show_social_links": false,
                "course_index_overlay_logo_file": "/static/edunext/images/logo.png",
                "course_org_filter": "eneXT",
                "released_languages": "es-419,en-US",
                "show_homepage_promo_video": false,
                "show_partners": false
            }"""
data={'data':string}
url='http://127.0.0.1:8000/api/v1/customerdata/1b2f7b83-7b4d-441d-a210-afaa970e5b76/'
r=requests.put(url,data)
print r.status_code
print r.json()
