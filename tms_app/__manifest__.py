{
    'name': 'TMS App New',
    'summary': 'TMS Application',
    'description': 'Manage for Product Shipping & Tracking',
    'author': 'Appcode Technology',
    'website': 'http://www.appcode.co.th',
    'version': '0.1',
    'category': 'Custom',
    'depends': ['base', 'stock_account', 'web_timeline', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/car.xml',
        'views/ticket.xml',
        'views/product.xml',
        'views/template.xml',
        'report/ticket.xml',
        'views/menu.xml',
    ],
    'demo': [],
}
