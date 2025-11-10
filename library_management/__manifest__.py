
{
    'name': 'Library Management',
    'author': 'Abdallah El-Saadany',
    'version': '18.0.0.1.0',
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/book.xml',
        'views/author.xml',
    ],
    'depends': ['base','mail'],
}
