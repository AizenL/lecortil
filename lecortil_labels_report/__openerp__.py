{
    'name': "Delivery labels",
    'version': '1.0',
    'depends': ['sale', 'report', 'lecortil_tours', 'lecortil_product_eater', 'lecortil_product_supplement', 'lecortil_sale_order_line_description'],
    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Stock',
    'description': """
    Print labels for sandwiches deliveries.

	This modules also creates a paperreport adapted for Le Cortil labels.
	To use it, you have to set it for the given report (settings/reports/=>Labels set paperformat as "Le Cortil Labels ...").
    """,
    'data': [
        'reports.xml',
		'data.xml',
    ],
    'demo': [
      'demo.xml',
    ],
}
