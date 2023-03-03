{
    'name': 'Most Viewed and Sold Product',
    'version': '16.0.1.0.0',
    'sequence': '-7',
    'category': 'website',
    'summary': 'Show Most Viewed and Sold Product',
    'description': 'Show Most Viewed and Sold Product',

    'installation': True,
    'application': True,

    'depends': ['base', 'website'],
    'data': [
        'views/snippet.xml',
        'views/most_viewed_sold.xml',
    ],
    'assets': {
       'web.assets_frontend': [
           'most_viewed_sold_pdt/static/src/xml/template.xml',
           'most_viewed_sold_pdt/static/src/js/most_viewed.js',
           'most_viewed_sold_pdt/static/src/css/carousel_design.scss',

       ],
}
}