"use strict";

$(document).ready(function () {
  //better use on() event handler for dynamically creating elements
  $(document).on('click', '.product-fields-button', function (e) {
    var productForm = $(this);
    var fieldNumber = productForm.data('field-number');
    var field = $('#product-field-modal-' + fieldNumber);
    var content = $('#product-field-modal-content-' + fieldNumber);
    field.show();
    field.css('overflow', 'scroll');
    field.css('padding', '10px');
    content.css('padding', '10px');
  });
  $(document).on('click', '.product-fields-close', function (e) {
    var productForm = $(this);
    var fieldNumber = productForm.data('field-number');
    $('#product-field-modal-' + fieldNumber).hide();
  }); // $('.client-type-radio').click(function () {
  //     $.ajax({
  //         url: '/api/product_type/',
  //         method: "GET",
  //         success: function (data) {
  //             console.log(data);
  //             if (data.success === true) {
  //                 product.empty().append('<option selected="selected"></option>');
  //                 const products = data.data;
  //                 const length = products.length;
  //                 for (let i = 0; i < length; i++) {
  //                     product.append(`<option value="${products[i].id}">${products[i].name}</option>`);
  //                 }
  //             }
  //         },
  //         error: function () {
  //             console.log('error');
  //         }
  //     })
  // });
});