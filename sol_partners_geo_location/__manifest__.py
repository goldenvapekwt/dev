# -*- coding: utf-8 -*-
{
    'name': "Geo, locate, draw into map case Partners Addon",

    'summary': "Sol map test res partner. ",
    'description': """
        Sol map test for res partner
    """,
    "category": "Web",
    'author': "0Solver0",
    'license': 'LGPL-3',
    'version': '15.0',
    'website': 'https://addons4.odoo.com/',
    'depends': ['sol_ol_map_draw','contacts'],
    'data': [
         "views/data.xml"
    ],
    'images': ['sol_partners_geo_location/static/description/thumbnails_screenshot.png','sol_partners_geo_location/static/description/icon.png'],
    'installable': True,
    'auto_install': False
}