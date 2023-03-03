from odoo import http
from odoo.http import request, Controller
import numpy as np


class MostViewedSold(Controller):

    @http.route(['/most_viewed_sold'], type="json", auth="public")
    def most_viewed(self):
        products = request.env['website.track'].sudo().search([]).\
            mapped('product_id')
        # print(products)
        view_product_tmpl = products.product_tmpl_id
        # print(view_product_tmpl)
        product_list = [[view.name, view.id, view.description_sale] for
                        view in view_product_tmpl]
        # print(product_list)
        new_list = [product_list[i:i + 4] for i in range(
            0, len(product_list), 4)]
        print(new_list)
        return new_list

    @http.route(['/most_sold'], type="json", auth="public")
    def most_sold(self):
        sale_orders = request.env['sale.order'].sudo().search([
            ('state', 'in', ['sale', 'done'])])
        # print(sale_orders)
        most_sold = {}
        for sale in sale_orders:
            # print(sale)
            for line in sale.order_line:
                # print(line)
                if line.product_template_id in most_sold.keys():
                    most_sold[line.product_template_id] = \
                        most_sold[line.product_template_id] + \
                        line.product_uom_qty
                else:
                    most_sold.update({
                        line.product_template_id: line.product_uom_qty
                    })
        # print(most_sold)
        values = list(most_sold.values())
        keys = list(most_sold.keys())
        # print(values)
        # print(keys)
        sorted_value_index = np.argsort(values)
        # print(sorted_value_index)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
        print(sorted_dict)
        res = dict(reversed(list(sorted_dict.items())))
        print(res)
        product_list = [[view.name, view.id, view.description_sale] for
                        view in res]
        print(product_list)
        new_list = [product_list[i:i + 4] for i in range(
            0, len(product_list), 4)]
        # print(new_list)
        return new_list
