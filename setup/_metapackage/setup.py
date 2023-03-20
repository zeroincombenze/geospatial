import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-geospatial",
    description="Meta package for oca-geospatial Odoo addons",
    version=version,
    install_requires=[
<<<<<<< HEAD
        'odoo14-addon-base_geoengine',
=======
>>>>>>> 05704c09af5ff31998550ce01af93dedc21f5c9f
        'odoo14-addon-base_google_map',
        'odoo14-addon-web_view_google_map',
        'odoo14-addon-web_widget_google_marker_icon_picker',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
