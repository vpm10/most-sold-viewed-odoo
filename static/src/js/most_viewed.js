odoo.define('most_viewed_sold_pdt.dynamic', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var core = require('web.core')
   var Qweb = core.qweb
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet_blog_1',
       start: function () {
//            console.log("ssssssuiIIIIIIIIIIIIIIIII");
           var self = this;
           rpc.query({
               route: '/most_viewed_sold',
               params: {},
           })
           .then(function (result) {
              console.log(result);
           result[0].set_active = true;
           $('.qweb_pdt').append(Qweb.render('most_viewed_sold_pdt.product', {result}));
           });
           rpc.query({
               route: '/most_sold',
               params: {},
           })
           .then(function (result1) {
              console.log(result1);
           result1[0].set_active = true;
           $('.qweb_product').append(Qweb.render('most_viewed_sold_pdt.most_sold', {result1}));
           });
       },
   });
   PublicWidget.registry.dynamic_snippet_blog = Dynamic;
   return Dynamic;
});
