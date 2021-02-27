"use strict";

function addRow() {
  var empTab = document.getElementById('empTable');
  var fieldNames = ['polis-num-', 'polis-series-', 'period_polis-', 'polis-agent-', 'polis-id-', 'polis-mark-', 'polis-model-', 'polis-modification-', 'polis-gos-num-', 'polis-teh-passport-', 'polis-num-engine-', 'polis-num-body-', 'polis-payload-', 'polis-places-', 'insurance_sum-', 'overall_insurance_sum-', 'insurance_premium-'];
  var rowCnt = empTab.rows.length; // get the number of rows.

  var tr = empTab.insertRow(rowCnt - 1); // table row.

  productFieldNumber++;
  var rowsAmount = $("#empTable thead tr th").length + 1;

  for (var _c = 0; _c < rowsAmount; _c++) {
    var td = document.createElement('td'); // TABLE DEFINITION.

    td = tr.insertCell(_c);

    if (_c == rowsAmount - 1) {
      // if its the last column of the table.
      // add delete a button
      var button = document.createElement('input'); // set the attributes.

      button.setAttribute('type', 'button');
      button.setAttribute('value', 'Удалить'); // add button's "onclick" event.

      button.setAttribute('onclick', 'removeRow(this)');
      button.setAttribute('data-field-number', productFieldNumber);
      button.setAttribute('class', 'btn btn-warning');
      td.appendChild(button); // add delete a button

      var button2 = document.createElement('input');
      button2.setAttribute('type', 'button');
      button2.setAttribute('value', 'Заполнить');
      button2.setAttribute('class', 'btn btn-success product-fields-button');
      button2.setAttribute('id', 'product-fields-button-' + productFieldNumber);
      button2.setAttribute('data-field-number', productFieldNumber);
      var td2 = document.createElement('td'); // TABLE DEFINITION.

      var fieldNumer = _c + 1;
      td2 = tr.insertCell(fieldNumer);
      td2.appendChild(button2);
    } else {
      // all except the last colum will have input field.
      var ele = document.createElement('input');
      var fieldIndex = _c + 1;
      var columnName = fieldNames[_c];
      ele.setAttribute('name', columnName + productFieldNumber);

      if (_c === 1) {
        ele = document.createElement('select');
      } else if (_c === 3) {
        ele = document.createElement('select');
      } else {
        ele.setAttribute('type', 'text');
      }

      if (columnName === 'polis-places-') {
        ele.setAttribute('class', 'form-control forsum2');
      } else if (columnName === 'insurance_sum-') {
        ele.setAttribute('class', 'form-control forsum insurance_sum-' + productFieldNumber);
        ele.setAttribute('data-field-number', productFieldNumber);
      } else if (columnName === 'insurance_premium-') {
        ele.setAttribute('class', 'form-control forsum3 insurance_premium-' + productFieldNumber);
        ele.setAttribute('readonly', 'true');
      } else if (columnName === 'overall_insurance_sum-') {
        ele.setAttribute('class', 'form-control forsum4 overall_insurance_sum-' + productFieldNumber);
      } else if (columnName === 'polis-num-') {
        ele.setAttribute('class', 'form-control polis-num-' + productFieldNumber);
        ele.setAttribute('readonly', 'true');
      } else {
        ele.setAttribute('class', 'form-control');
      }

      td.appendChild(ele);
    }
  }

  addProductFields(productFieldNumber);
}

var num1 = 1;
var num2 = 1;
$('#insurer-modal-button').on('click', function () {
  var clone = $('#clone-insurance:last').clone();
  clone.insertAfter('#clone-insurance:last');
  clone.find('#insurer-name').attr('name', "insurer-name".concat(num1));
  clone.find('#insurer-address').attr('name', "insurer-address".concat(num1));
  clone.find('#insurer-tel').attr('name', "insurer-tel".concat(num1));
  clone.find('#insurer-schet').attr('name', "insurer-schet".concat(num1));
  clone.find('#insurer-inn').attr('name', "insurer-inn".concat(num1));
  clone.find('#insurer-mfo').attr('name', "insurer-mfo".concat(num1));
  clone.find('#insurer-bank').attr('name', "insurer-bank".concat(num1));
  clone.find('#insurer-okonh').attr('name', "insurer-okonh".concat(num1));
  clone.find('#insurer-name').attr('id', "insurer-name".concat(num1));
  clone.find('#insurer-address').attr('id', "insurer-address".concat(num1));
  clone.find('#insurer-tel').attr('id', "insurer-tel".concat(num1));
  clone.find('#insurer-schet').attr('id', "insurer-schet".concat(num1));
  clone.find('#insurer-inn').attr('id', "insurer-inn".concat(num1));
  clone.find('#insurer-mfo').attr('id', "insurer-mfo".concat(num1));
  clone.find('#insurer-bank').attr('id', "insurer-bank".concat(num1));
  clone.find('#insurer-okonh').attr('id', "insurer-okonh".concat(num1));
  clone.find('#insurer-name').prev().attr('for', "insurer-name".concat(num1));
  clone.find('#insurer-address').prev().attr('for', "insurer-address".concat(num1));
  clone.find('#insurer-tel').prev().attr('for', "insurer-tel".concat(num1));
  clone.find('#insurer-schet').prev().attr('for', "insurer-schet".concat(num1));
  clone.find('#insurer-inn').prev().attr('for', "insurer-inn".concat(num1));
  clone.find('#insurer-mfo').prev().attr('for', "insurer-mfo".concat(num1));
  clone.find('#insurer-bank').prev().attr('for', "insurer-bank".concat(num1));
  clone.find('#insurer-okonh').prev().attr('for', "insurer-okonh".concat(num1));
  num1++;
  clone.find('.card-title').html("\u0421\u0442\u0440\u0430\u0445\u043E\u0432\u0430\u0442\u0435\u043B\u044C \u2116".concat(num1));
  clone.find('#insurer-modal-button').html("\u0423\u0434\u0430\u043B\u0438\u0442\u044C").attr('class', 'btn btn-warning');
  clone.find('#insurer-modal-button').on('click', function () {
    $(this).parent().parent().parent().remove();
    num1--;
  });
});
$('#beneficiary-modal-button').on('click', function () {
  var clone = $('#clone-beneficiary:last').clone();
  clone.insertAfter('#clone-beneficiary:first');
  clone.find('#beneficiary-name').attr('name', "beneficiary-name".concat(num2));
  clone.find('#beneficiary-address').attr('name', "beneficiary-address".concat(num2));
  clone.find('#beneficiary-tel').attr('name', "beneficiary-tel".concat(num2));
  clone.find('#beneficiary-schet').attr('name', "beneficiary-schet".concat(num2));
  clone.find('#beneficiary-inn').attr('name', "beneficiary-inn".concat(num2));
  clone.find('#beneficiary-mfo').attr('name', "beneficiary-mfo".concat(num2));
  clone.find('#beneficiary-bank').attr('name', "beneficiary-bank".concat(num2));
  clone.find('#beneficiary-okonh').attr('name', "beneficiary-okonh".concat(num2));
  clone.find('#beneficiary-name').attr('id', "beneficiary-name".concat(num2));
  clone.find('#beneficiary-address').attr('id', "beneficiary-address".concat(num2));
  clone.find('#beneficiary-tel').attr('id', "beneficiary-tel".concat(num2));
  clone.find('#beneficiary-schet').attr('id', "beneficiary-schet".concat(num2));
  clone.find('#beneficiary-inn').attr('id', "beneficiary-inn".concat(num2));
  clone.find('#beneficiary-mfo').attr('id', "beneficiary-mfo".concat(num2));
  clone.find('#beneficiary-bank').attr('id', "beneficiary-bank".concat(num2));
  clone.find('#beneficiary-okonh').attr('id', "beneficiary-okonh".concat(num2));
  clone.find('#beneficiary-name').prev().attr('for', "beneficiary-name".concat(num2));
  clone.find('#beneficiary-address').prev().attr('for', "beneficiary-address".concat(num2));
  clone.find('#beneficiary-tel').prev().attr('for', "beneficiary-tel".concat(num2));
  clone.find('#beneficiary-schet').prev().attr('for', "beneficiary-schet".concat(num2));
  clone.find('#beneficiary-inn').prev().attr('for', "beneficiary-inn".concat(num2));
  clone.find('#beneficiary-mfo').prev().attr('for', "beneficiary-mfo".concat(num2));
  clone.find('#beneficiary-bank').prev().attr('for', "beneficiary-bank".concat(num2));
  clone.find('#beneficiary-okonh').prev().attr('for', "beneficiary-okonh".concat(num2));
  num2++;
  clone.find('.card-title').html("\u0412\u044B\u0433\u043E\u0434\u043E\u043F\u0440\u0438\u043E\u0431\u0440\u0435\u0442\u0430\u0442\u0435\u043B\u044C \u2116".concat(num2));
  clone.find('#beneficiary-modal-button').html("\u0423\u0434\u0430\u043B\u0438\u0442\u044C").attr('class', 'btn btn-warning');
  clone.find('#beneficiary-modal-button').on('click', function () {
    $(this).parent().parent().parent().remove();
    num2--;
  });
});
$(document).ready(function () {
  $(document).on("keyup", ".forsum", calculateSum);
  $(document).on("keyup", ".forsum2", calculateSum2);
  $(document).on("keyup", ".forsum3", calculateSum3);
  $(document).on("keyup", ".forsum4", calculateSum4);
  $(document).on("keyup", ".forsum5", calculateSum5);
  $('.defects').on('change', function () {
    console.log('sa');
    var targetBox = $('.defects_images');

    if ($(this).attr("value") === '1') {
      $(targetBox).show(400);
    } else {
      $(targetBox).hide(400);
    }
  });
});
$(document).on('keyup', function () {
  if ($('.overall-sum4').val() < $('.overall-sum').val()) {
    alert('Страховая стоимость не должна превышать страховую сумму');
    $('#form-save-button').attr('disabled', true);
  } else {
    $('#form-save-button').removeAttr('disabled');
  }
});
$(document).on("keyup", ".modal", function () {
  var fieldNumber = $(this).data('field-number');
  overallSum = parseFloat($('#insurance_sum-' + fieldNumber).val() || 0) + parseFloat($('.terror-tc-' + fieldNumber).val() || 0) + parseFloat($('.terror-zl-' + fieldNumber).val() || 0) + parseFloat($('.evocuation-' + fieldNumber).val() || 0) + parseFloat($('.r-1-sum-' + fieldNumber).val() || 0) + parseFloat($('.r-2-sum-' + fieldNumber).val() || 0) + parseFloat($('.r-3-sum-' + fieldNumber).val() || 0) + parseFloat($('.r-3-sum-1-' + fieldNumber).val() || 0) + parseFloat($('.r-3-sum-2-' + fieldNumber).val() || 0);
  var modalTableSum2 = parseFloat($('.r-3-sum-' + fieldNumber).val() || 0) + parseFloat($('.r-3-sum-1-' + fieldNumber).val() || 0) + parseFloat($('.r-3-sum-2-' + fieldNumber).val() || 0);
  var modalTableSum3 = parseFloat($('.r-3-premia-' + fieldNumber).val() || 0) + parseFloat($('.r-3-premia-1-' + fieldNumber).val() || 0) + parseFloat($('.r-3-premia-2-' + fieldNumber).val() || 0);
  $('#overall-sum-' + fieldNumber).val(overallSum);
  $('.r-summ-' + fieldNumber).val(modalTableSum2);
  $('.r-summ-premia-' + fieldNumber).val(modalTableSum3);
  $('#totalLimit-' + fieldNumber).on('keyup', function () {
    if ($('.r-summ-' + fieldNumber).val() >= $('#totalLimit-' + fieldNumber).val()) {
      $('#form-save-button').attr('disabled', true); // alert('Общий лимит ответственности не может превышать страховую сумму по видам опасностей');
    } else {
      $('#form-save-button').removeAttr('disabled');
    }
  });
  calculateSum4(fieldNumber);
});
$(document).on("change", ".modal", function () {
  var fieldNumber = $(this).data('field-number');
  $('.other_insurance-' + fieldNumber).on('change', function () {
    var targetBox = $('.other_insurance_info-' + fieldNumber);

    if ($(this).attr("value") === '1') {
      $(targetBox).show(400);
    } else {
      $(targetBox).hide(400);
    }
  });
  $('.r-1-' + fieldNumber).on('change', function () {
    var targetBox = $('.r-1-show-' + fieldNumber);

    if ($(this).attr("value") === '1') {
      $(targetBox).show(400);
    } else {
      $(targetBox).hide(400);
    }
  });
  $('.r-2-' + fieldNumber).on('change', function () {
    var targetBox = $(".r-2-show-".concat(fieldNumber));

    if ($(this).attr("value") === '1') {
      $(targetBox).show(400);
    } else {
      $(targetBox).hide(400);
    }
  });
  $('.r-3-' + fieldNumber).on('change', function () {
    var targetBox = $(".r-3-show-".concat(fieldNumber));

    if ($(this).attr("value") === '1') {
      $(targetBox).show(400);
    } else {
      $(targetBox).hide(400);
    }
  });
  $('.r-3-one-' + fieldNumber).on('keyup', function () {
    var numOne = $(this).val() * $(".r-3-pass-".concat(fieldNumber)).val();
    $(document).find(".r-3-sum-".concat(fieldNumber)).val(numOne);
  });
  $('.r-3-pass-1-' + fieldNumber).on('keyup', function () {
    var numOne = $(this).val() * $(".r-3-one-1-".concat(fieldNumber)).val();
    $(document).find(".r-3-sum-1-".concat(fieldNumber)).val(numOne);
  });
  $('.r-3-one-1-' + fieldNumber).on('keyup', function () {
    var numOne = $(this).val() * $(".r-3-pass-1-".concat(fieldNumber)).val();
    $(document).find(".r-3-sum-1-".concat(fieldNumber)).val(numOne);
  });
  $('.r-3-pass-2-' + fieldNumber).on('keyup', function () {
    var numOne = $(this).val() * $(".r-3-one-2-".concat(fieldNumber)).val();
    $(document).find(".r-3-sum-2-".concat(fieldNumber)).val(numOne);
  });
  $('.r-3-one-2-' + fieldNumber).on('keyup', function () {
    var numOne = $(this).val() * $(".r-3-pass-2-".concat(fieldNumber)).val();
    $(document).find(".r-3-sum-2-".concat(fieldNumber)).val(numOne);
  });
});

function calculateSum() {
  var sum = 0;
  $('.forsum').each(function () {
    if (!isNaN(this.value) && this.value.length != 0) {
      sum += parseFloat(this.value);
    }
  });
  $('.overall-sum').val(sum.toFixed(2));
}

function calculateSum2() {
  var sum = 0;
  $('.forsum2').each(function () {
    if (!isNaN(this.value) && this.value.length != 0) {
      sum += parseFloat(this.value);
    }
  });
  $('.overall-sum2').val(sum.toFixed(2));
}

function calculateSum3() {
  var sum = 0;
  $('.forsum3').each(function () {
    if (!isNaN(this.value) && this.value.length != 0) {
      sum += parseFloat(this.value);
    }
  });
  $('.overall-sum3').val(sum.toFixed(2));
}

function calculateSum4(fieldNumber) {
  var sum = 0;

  try {
    $('.forsum4').each(function () {
      if (!isNaN(this.value) && this.value.length != 0) {
        sum = parseFloat(this.value) + parseFloat($('#overall-sum-' + fieldNumber).val());
      }
    });
  } catch (_unused) {
    $('.forsum4').each(function () {
      if (!isNaN(this.value) && this.value.length != 0) {
        sum = parseFloat(this.value);
      }
    });
  }

  $('.overall-sum4').val(sum.toFixed(2));
}

function calculateSum5() {
  var sum = 0;
  $('.forsum5').each(function () {
    if (!isNaN(this.value) && this.value.length != 0) {
      sum += parseFloat(this.value);
    }
  });
  $('.overall-sum5').val(sum.toFixed(2));
} // function to delete a row.


function removeRow(oButton) {
  var empTab = document.getElementById('empTable');
  empTab.deleteRow(oButton.parentNode.parentNode.rowIndex); // buttton -> td -> tr

  var id = oButton.dataset.fieldNumber;
  $("#product-field-modal-" + id).remove();
  calculateSum();
  calculateSum2();
  calculateSum3();
  calculateSum5();
} // function to add new row.


function addRow2() {
  var empTab = document.getElementById('empTable2');
  var rowCnt = empTab.rows.length; // get the number of rows.

  var tr = empTab.insertRow(rowCnt - 1); // table row.

  for (var _c2 = 0; _c2 < $("#empTable2 tr th").length; _c2++) {
    var td = document.createElement('td'); // TABLE DEFINITION.

    td = tr.insertCell(_c2);
    var ele = document.createElement('input');
    ele.setAttribute('type', 'text');
    ele.setAttribute('class', 'form-control');
    td.appendChild(ele);
  }
} // function to delete a row.


function removeRow2(oButton) {
  var empTab = document.getElementById('empTable2');
  empTab.deleteRow(oButton.parentNode.parentNode.rowIndex); // buttton -> td -> tr
}

function showDiv(divId, element) {
  document.getElementById(divId).style.display = element.value == 'other' ? 'block' : 'none';
}

function addRow3(fieldNumber) {
  var empTab = document.getElementById('empTable3');
  var rowCnt = empTab.rows.length; // get the number of rows.

  var tr = empTab.insertRow(rowCnt); // table row.

  paymentTypeFieldNumber++;

  for (var _c3 = 0; _c3 < $("#empTable3 tr th").length; _c3++) {
    var td = document.createElement('td'); // TABLE DEFINITION.

    td = tr.insertCell(_c3);

    if (_c3 == $("#empTable3 tr th").length - 1) {
      // if its the first column of the table.
      // add a button control.
      var button = document.createElement('input'); // set the attributes.

      button.setAttribute('type', 'button');
      button.setAttribute('value', 'Удалить'); // add button's "onclick" event.

      button.setAttribute('onclick', 'removeRow3(this)');
      button.setAttribute('class', 'btn btn-warning');
      td.appendChild(button);
    } else {
      // all except the last colum will have input field.
      var ele = document.createElement('input');

      if (_c3 === 1) {
        ele.setAttribute('type', 'date');
        ele.setAttribute('id', "payment_from-".concat(fieldNumber, "-").concat(paymentTypeFieldNumber));
      } else {
        ele.setAttribute('type', 'text');
        ele.setAttribute('id', "payment_sum-".concat(fieldNumber, "-").concat(paymentTypeFieldNumber));
      }

      ele.setAttribute('class', 'form-control');
      td.appendChild(ele);
    }
  }
} // function to delete a row.


function removeRow3(oButton) {
  var empTab = document.getElementById('empTable3');
  empTab.deleteRow(oButton.parentNode.parentNode.rowIndex); // buttton -> td -> tr
} // function to extract and submit table data.


function submit() {
  var myTab = document.getElementById('empTable');
  var arrValues = []; // loop through each row of the table.

  for (row = 1; row < myTab.rows.length - 1; row++) {
    // loop through each cell in a row.
    for (c = 0; c < myTab.rows[row].cells.length; c++) {
      var element = myTab.rows.item(row).cells[c];

      if (element.childNodes[0].getAttribute('type') == 'text') {
        arrValues.push("'" + element.childNodes[0].value + "'");
      }
    }
  }
}

$('#form-save-button').on('click', function () {
  $('#mainFormKasko').submit();
}); //ToDo: delete one of the addproductfields function

function addProductFields(fieldNumber) {
  var fields = "\n<div id=\"product-field-modal-".concat(fieldNumber, "\" class=\"modal\" data-field-number=\"").concat(fieldNumber, "\">\n    <div class=\"modal-content\" id=\"product-field-modal-content-").concat(fieldNumber, "\">\n        <span class=\"close product-fields-close\" id=\"product-fields-close-").concat(fieldNumber, "\" data-field-number=\"").concat(fieldNumber, "\">&times;</span>\n        <div class=\"card card-success\">\n            <div class=\"card-header\">\n                <h3 class=\"card-title\">\u041F\u0435\u0440\u0435\u0447\u0435\u043D\u044C \u0434\u043E\u043F\u043E\u043B\u043D\u0438\u0442\u0435\u043B\u044C\u043D\u043E\u0433\u043E \u043E\u0431\u043E\u0440\u0443\u0434\u043E\u0432\u0430\u043D\u0438\u044F</h3>\n                <div class=\"card-tools\">\n                    <button type=\"button\" class=\"btn btn-tool\" data-card-widget=\"collapse\" data-toggle=\"tooltip\" title=\"Collapse\">\n                    <i class=\"fas fa-minus\"></i>\n                </button>\n                </div>\n            </div>\n            <div class=\"card-body\">\n                <div class=\"table-responsive p-0 \" style=\"max-height: 300px;\">\n                    <form method=\"POST\" id=\"product-fields-").concat(fieldNumber, "-1\">\n                        <table class=\"table table-hover table-head-fixed\" id=\"empTable2\">\n                            <thead>\n                                <tr>\n                                    <th class=\"text-nowrap\">\u041C\u0430\u0440\u043A\u0430, \u043C\u043E\u0434\u0435\u043B\u044C, \u043C\u043E\u0434\u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F \u0422\u0421</th>\n                                    <th>\u041D\u0430\u0438\u043C\u0435\u043D\u043E\u0432\u0430\u043D\u0438\u0435 \u043E\u0431\u043E\u0440\u0443\u0434\u043E\u0432\u0430\u043D\u0438\u044F</th>\n                                    <th>\u0421\u0435\u0440\u0438\u0439\u043D\u044B\u0439 \u043D\u043E\u043C\u0435\u0440</th>\n                                    <th>\u0421\u0442\u0440\u0430\u0445\u043E\u0432\u0430\u044F \u0441\u0443\u043C\u043C\u0430</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n                                <tr>\n                                    <td><input type=\"text\" class=\"form-control\" name=\"mark_model\"></td>\n                                    <td><input type=\"text\" class=\"form-control\" name=\"name\"></td>\n                                    <td><input type=\"text\" class=\"form-control\" name=\"series_number\"></td>\n                                    <td><input type=\"text\" class=\"form-control forsum5\" name=\"insurance_sum\" id=\"insurance_sum-").concat(fieldNumber, "\"></td>\n                                </tr>\n                                <tr>\n                                    <td colspan=\"3\"><label class=\"text-bold\">\u0418\u0442\u043E\u0433\u043E</label></td>\n                                    <td><input type=\"text\" class=\"form-control overall-sum").concat(fieldNumber, "\" readonly name=\"total\"></td>\n                                </tr>\n                            </tbody>\n                        </table>\n                    </form>\n                </div>\n            </div>\n        </div>\n\n        <div class=\"card card-success\">\n            <div class=\"card-header\">\n                <h3 class=\"card-title\">\u0414\u043E\u043F\u043E\u043B\u043D\u0438\u0442\u0435\u043B\u044C\u043D\u043E\u0435 \u0441\u0442\u0440\u0430\u0445\u043E\u0432\u043E\u0435 \u043F\u043E\u043A\u0440\u044B\u0442\u0438\u0435</h3>\n                <div class=\"card-tools\">\n                    <button type=\"button\" class=\"btn btn-tool\" data-card-widget=\"collapse\" data-toggle=\"tooltip\" title=\"Collapse\">\n                    <i class=\"fas fa-minus\"></i>\n                </button>\n                </div>\n            </div>\n\n            <div class=\"card-body\">\n                <form method=\"POST\" id=\"product-fields-").concat(fieldNumber, "-2\">\n                    <div class=\"form-group\">\n                        <label>\u041F\u043E\u043A\u0440\u044B\u0442\u0438\u0435 \u0442\u0435\u0440\u0440\u043E\u0440\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043A\u0438\u0445 \u0430\u043A\u0442\u043E\u0432 \u0441 \u0422\u0421 </label>\n                        <div class=\"input-group mb-4\">\n                            <input type=\"text\" class=\"form-control terror-tc-").concat(fieldNumber, "\" name=\"cover_terror_attacks_sum\">\n                            <div class=\"input-group-append\">\n                                <select class=\"form-control success\" name=\"cover_terror_attacks_currency\" style=\"width: 100%;\">\n                                    <option selected=\"selected\">UZS</option>\n                                    <option>USD</option>\n                                </select>\n                            </div>\n                        </div>\n                    </div>\n\n                    <div class=\"form-group\">\n                        <label>\u041F\u043E\u043A\u0440\u044B\u0442\u0438\u0435 \u0442\u0435\u0440\u0440\u043E\u0440\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043A\u0438\u0445 \u0430\u043A\u0442\u043E\u0432 \u0441 \u0437\u0430\u0441\u0442\u0440\u0430\u0445\u043E\u0432\u0430\u043D\u043D\u044B\u043C\u0438 \u043B\u0438\u0446\u0430\u043C\u0438 </label>\n                        <div class=\"input-group mb-4\">\n                            <input type=\"text\" class=\"form-control terror-zl-").concat(fieldNumber, "\" name=\"cover_terror_attacks_insured_sum\">\n                            <div class=\"input-group-append\">\n                                <select class=\"form-control success\" name=\"cover_terror_attacks_insured_currency\" style=\"width: 100%;\">\n                                    <option selected=\"selected\">UZS</option>\n                                    <option>USD</option>\n                                </select>\n                            </div>\n                        </div>\n                    </div>\n\n                    <div class=\"form-group\">\n                        <label>\u041F\u043E\u043A\u0440\u044B\u0442\u0438\u0435 \u0440\u0430\u0441\u0445\u043E\u0434\u044B \u043F\u043E \u044D\u0432\u0430\u043A\u0443\u0430\u0446\u0438\u0438</label>\n                        <div class=\"input-group mb-4\">\n                            <input type=\"text\" class=\"form-control evocuation-").concat(fieldNumber, "\" name=\"coverage_evacuation_cost\">\n                            <div class=\"input-group-append\">\n                                <select class=\"form-control success\" name=\"coverage_evacuation_currency\" style=\"width: 100%;\">\n                                <option selected=\"selected\">UZS</option>\n                                <option>USD</option>\n                            </select>\n                            </div>\n                        </div>\n                    </div>\n                </form>\n            </div>\n        </div>\n\n        <div class=\"card card-success\">\n            <div class=\"card-header\">\n                <h3 class=\"card-title\">\u0421\u0432\u0435\u0434\u0435\u043D\u0438 \u043E \u0442\u0440\u0430\u043D\u0441\u043E\u0440\u0442\u043D\u044B\u0445 \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0430\u0445</h3>\n                <div class=\"card-tools\">\n                    <button type=\"button\" class=\"btn btn-tool\" data-card-widget=\"collapse\" data-toggle=\"tooltip\" title=\"Collapse\">\n                        <i class=\"fas fa-minus\"></i>\n                    </button>\n                </div>\n            </div>\n            <div class=\"card-body\">\n                <form method=\"POST\" id=\"product-fields-").concat(fieldNumber, "-3\">\n                    <div class=\"form-group\">\n                        <label>\u0417\u0430\u0441\u0442\u0440\u0430\u0445\u043E\u0432\u0430\u043D\u044B \u043B\u0438 \u0430\u0432\u0442\u043E\u0442\u0440\u0430\u043D\u0441\u043F\u043E\u0440\u0442\u043D\u044B\u0435 \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0430 \u043D\u0430 \u043C\u043E\u043C\u0435\u043D\u0442 \u0437\u0430\u043F\u043E\u043B\u043D\u0435\u043D\u0438\u044F \u043D\u0430\u0441\u0442\u043E\u044F\u0449\u0435\u0439 \u0430\u043D\u043A\u0435\u0442\u044B? </label>\n                        <div class=\"row\">\n                            <div class=\"col-sm-1\">\n                                <div class=\"checkbox icheck-success\">\n                                    <input type=\"radio\" class=\"other_insurance-").concat(fieldNumber, "\" name=\"strtahovka-").concat(fieldNumber, "\" id=\"radioSuccess1-").concat(fieldNumber, "\" value=\"1\">\n                                    <label for=\"radioSuccess1-").concat(fieldNumber, "\">\u0414\u0430</label>\n                                </div>\n                                <div class=\"checkbox icheck-success\">\n                                    <input type=\"radio\" class=\"other_insurance-").concat(fieldNumber, "\" name=\"strtahovka-").concat(fieldNumber, "\" id=\"radioSuccess2-").concat(fieldNumber, "\" value=\"0\">\n                                    <label for=\"radioSuccess2-").concat(fieldNumber, "\">\u041D\u0435\u0442</label>\n                                </div>\n                            </div>\n                        </div>\n                    </div>\n                    <div class=\"form-group other_insurance_info-").concat(fieldNumber, "                    \" style=\"display:none\">\n                        <label>\u0423\u043A\u0430\u0436\u0438\u0442\u0435 \u043D\u0430\u0437\u0432\u0430\u043D\u0438\u0435 \u0438 \u0430\u0434\u0440\u0435\u0441 \u0441\u0442\u0440\u0430\u0445\u043E\u0432\u043E\u0439 \u043E\u0440\u0433\u0430\u043D\u0438\u0437\u0430\u0446\u0438\u0438 \u0438 \u043D\u043E\u043C\u0435\u0440 \u041F\u043E\u043B\u0438\u0441\u0430</label>\n                        <input class=\"form-control\" type=\"text\" name=\"other_insurance_info").concat(fieldNumber, "\">\n                    </div>\n                </form>\n            </div>\n        </div>\n\n        <div class=\"card card-success\">\n            <div class=\"card-header\">\n                <h3 class=\"card-title\">\u0421\u0442\u0440\u0430\u0445\u043E\u0432\u044B\u0435 \u043F\u043E\u043A\u0440\u044B\u0442\u0438\u044F \u043F\u043E \u0432\u0438\u0434\u0430\u043C \u043E\u043F\u0430\u0441\u043D\u043E\u0441\u0442\u0435\u0439 </h3>\n                <div class=\"card-tools\">\n                    <button type=\"button\" class=\"btn btn-tool\" data-card-widget=\"collapse\" data-toggle=\"tooltip\" title=\"Collapse\">\n                        <i class=\"fas fa-minus\"></i>\n                    </button>\n                </div>\n            </div>\n            <div class=\"card-body\">\n                <form method=\"POST\" id=\"product-fields-").concat(fieldNumber, "-4\">\n                    <div class=\"form-group\">\n                        <label>\u0420\u0430\u0437\u0434\u0435\u043B I. \u0413\u0438\u0431\u0435\u043B\u044C \u0438\u043B\u0438 \u043F\u043E\u0432\u0440\u0435\u0436\u0434\u0435\u043D\u0438\u0435 \u0442\u0440\u0430\u043D\u0441\u043F\u043E\u0440\u0442\u043D\u043E\u0433\u043E \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0430</label>\n                        <div class=\"row\">\n                            <div class=\"col-md-1\">\n                                <div class=\"checkbox icheck-success\">\n                                    <input type=\"radio\" name=\"vehicle_damage-").concat(fieldNumber, "\" class=\"r-1-").concat(fieldNumber, "\" id=\"radioSuccess3-").concat(fieldNumber, "\" value=\"1\">\n                                    <label for=\"radioSuccess3-").concat(fieldNumber, "\">\u0414\u0430</label>\n                                </div>\n                                <div class=\"checkbox icheck-success\">\n                                    <input type=\"radio\" name=\"vehicle_damage-").concat(fieldNumber, "\" class=\"r-1-").concat(fieldNumber, "\" id=\"radioSuccess4-").concat(fieldNumber, "\" value=\"0\">\n                                    <label for=\"radioSuccess4-").concat(fieldNumber, "\">\u041D\u0435\u0442</label>\n                                </div>\n                            </div>\n                            <div class=\"row r-1-show-").concat(fieldNumber, "\" style=\"display: none;\">\n                                <div class=\"col-md-4\">\n                                    <div class=\"form-group\">\n                                        <div class=\"input-group mb-3\">\n                                            <div class=\"input-group-prepend\">\n                                                <span class=\"input-group-text\">\u0421\u0443\u043C\u043C\u0430</span>\n                                            </div>\n                                            <input type=\"text\" class=\"form-control r-1-sum-").concat(fieldNumber, "\" name=\"one-sum-").concat(fieldNumber, "\" id=\"vehicle_damage_sum-").concat(fieldNumber, "\">\n                                        </div>\n                                    </div>\n                                </div>\n                                <div class=\"col-md-4\">\n                                    <div class=\"form-group\">\n                                        <div class=\"input-group mb-3\">\n                                            <div class=\"input-group-prepend\">\n                                                <span class=\"input-group-text\">\u0421\u0442\u0440\u0430\u0445\u043E\u0432\u0430\u044F \u043F\u0440\u0435\u043C\u0438\u044F</span>\n                                            </div>\n                                            <input type=\"text\" class=\"form-control r-1-premia-").concat(fieldNumber, "\" name=\"one-premia-").concat(fieldNumber, "\" id=\"vehicle_damage_sum-").concat(fieldNumber, "\">\n                                        </div>\n                                    </div>\n                                </div>\n                                <div class=\"col-md-4\">\n                                    <div class=\"form-group\">\n                                        <div class=\"input-group mb-3\">\n                                            <div class=\"input-group-prepend\">\n                                                <span class=\"input-group-text\">\u0424\u0440\u0430\u043D\u0448\u0438\u0437\u0430</span>\n                                            </div>\n                                            <input type=\"text\" class=\"form-control r-1-frnshiza-").concat(fieldNumber, "\" name=\"one-franshiza-").concat(fieldNumber, "\" id=\"vehicle_damage_sum-").concat(fieldNumber, "\">\n                                        </div>\n                                    </div>\n                                </div>\n                            </div>\n                        </div>\n                    </div>\n                </form>\n                <form method=\"POST\" id=\"product-fields-").concat(fieldNumber, "-5\">\n                    <div class=\"form-group\">\n                        <label class=>\u0420\u0430\u0437\u0434\u0435\u043B II. \u0410\u0432\u0442\u043E\u0433\u0440\u0430\u0436\u0434\u0430\u043D\u0441\u043A\u0430\u044F \u043E\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043D\u043D\u043E\u0441\u0442\u044C</label>\n                        <div class=\"row\">\n                            <div class=\"col-sm-1\">\n                                <div class=\"checkbox icheck-success\">\n                                    <input type=\"radio\" name=\"civil_liability-").concat(fieldNumber, "\" class=\"r-2-").concat(fieldNumber, "\" id=\"radioSuccess5-").concat(fieldNumber, "\" value=\"1\">\n                                    <label for=\"radioSuccess5-").concat(fieldNumber, "\">\u0414\u0430</label>\n                                </div>\n                                <div class=\"checkbox icheck-success\">\n                                    <input type=\"radio\" name=\"civil_liability-").concat(fieldNumber, "\" class=\"r-2-").concat(fieldNumber, "\" id=\"radioSuccess6-").concat(fieldNumber, "\" value=\"0\">\n                                    <label for=\"radioSuccess6-").concat(fieldNumber, "\">\u041D\u0435\u0442</label>\n                                </div>\n                            </div>\n                            <div class=\"row r-2-show-").concat(fieldNumber, "\" style=\"display: none;\">\n                                <div class=\"col-md-6\">\n                                    <div class=\"form-group\">\n                                        <div class=\"input-group mb-3\">\n                                            <div class=\"input-group-prepend\">\n                                                <span class=\"input-group-text\">\u0421\u0443\u043C\u043C\u0430</span>\n                                            </div>\n                                            <input type=\"text\" class=\"form-control r-2-sum-").concat(fieldNumber, "\" name=\"tho_sum-").concat(fieldNumber, "\" id=\"vehicle_damage_sum-").concat(fieldNumber, "\">\n                                        </div>\n                                    </div>\n                                </div>\n                                <div class=\"col-md-6\">\n                                    <div class=\"form-group\">\n                                        <div class=\"input-group mb-3\">\n                                            <div class=\"input-group-prepend\">\n                                                <span class=\"input-group-text\">\u0421\u0442\u0440\u0430\u0445\u043E\u0432\u0430\u044F \u043F\u0440\u0435\u043C\u0438\u044F</span>\n                                            </div>\n                                            <input type=\"text\" class=\"form-control r-2-premia-").concat(fieldNumber, "\" name=\"two-preim-").concat(fieldNumber, "\" id=\"vehicle_damage_sum-").concat(fieldNumber, "\">\n                                        </div>\n                                    </div>\n                                </div>\n                            </div>\n                        </div>\n                    </div>\n                </form>\n\n                <form method=\"POST\" id=\"product-fields-").concat(fieldNumber, "-6\">\n                    <div class=\"form-group\">\n                        <label>\u0420\u0430\u0437\u0434\u0435\u043B III. \u041D\u0435\u0441\u0447\u0430\u0441\u0442\u043D\u044B\u0435 \u0441\u043B\u0443\u0447\u0430\u0438 \u0441 \u0417\u0430\u0441\u0442\u0440\u0430\u0445\u043E\u0432\u0430\u043D\u043D\u044B\u043C\u0438 \u043B\u0438\u0446\u0430\u043C\u0438</label>\n                        <div class=\"row\">\n                            <div class=\"col-md-1\">\n                                <div class=\"checkbox icheck-success\">\n                                    <input type=\"radio\" name=\"accidents-").concat(fieldNumber, "\" class=\"r-3-").concat(fieldNumber, "\" id=\"radioSuccess7-").concat(fieldNumber, "\" value=\"1\">\n                                    <label for=\"radioSuccess7-").concat(fieldNumber, "\">\u0414\u0430</label>\n                                </div>\n                                <div class=\"checkbox icheck-success\">\n                                    <input type=\"radio\" name=\"accidents-").concat(fieldNumber, "\" class=\"r-3-").concat(fieldNumber, "\" id=\"radioSuccess8-").concat(fieldNumber, "\" value=\"0\">\n                                    <label for=\"radioSuccess8-").concat(fieldNumber, "\">\u041D\u0435\u0442</label>\n                                </div>\n                            </div>\n                        </div>\n                    </div>\n                    <div class=\"table-responsive p-0 r-3-show-").concat(fieldNumber, "\" style=\"display: none;\">\n                        <form method=\"POST\" id=\"product-fields-").concat(fieldNumber, "-7\">\n                            <table class=\"table table-hover table-head-fixed\">\n                                <thead>\n                                    <tr>\n                                        <th>\u041E\u0431\u044A\u0435\u043A\u0442\u044B \u0441\u0442\u0440\u0430\u0445\u043E\u0432\u0430\u043D\u0438\u044F </th>\n                                        <th>\u041A\u043E\u043B\u0438\u0447\u0435\u0441\u0442\u0432\u043E \u0432\u043E\u0434\u0438\u0442\u0435\u043B\u0435\u0439 /\u043F\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u043E\u0432</th>\n                                        <th>\u0421\u0442\u0440\u0430\u0445\u043E\u0432\u0430\u044F \u0441\u0443\u043C\u043C\u0430 \u043D\u0430 \u043E\u0434\u043D\u043E\u0433\u043E \u043B\u0438\u0446\u0430</th>\n                                        <th>\u0421\u0442\u0440\u0430\u0445\u043E\u0432\u0430\u044F \u0441\u0443\u043C\u043C\u0430</th>\n                                        <th>\u0421\u0442\u0440\u0430\u0445\u043E\u0432\u0430\u044F \u043F\u0440\u0435\u043C\u0438\u044F</th>\n                                    </tr>\n                                </thead>\n                                <tbody>\n                                    <tr>\n                                        <td><label>\u0412\u043E\u0434\u0438\u0442\u0435\u043B\u044C(\u0438)</label></td>\n                                        <td><input type=\"number\" class=\"form-control r-3-pass-").concat(fieldNumber, "\" value=\"1\" readonly name=\"driver_quantity-").concat(fieldNumber, "\"></td>\n                                        <td>\n                                            <div class=\"input-group mb-4\">\n                                                <input type=\"text\" class=\"form-control r-3-one-").concat(fieldNumber, "\" name=\"driver_one_sum-").concat(fieldNumber, "\">\n                                                <div class=\"input-group-append\">\n                                                    <select class=\"form-control success\" name=\"driver_currency-\" style=\"width: 100%;\">\n                                                        <option selected=\"selected\">UZS</option>\n                                                        <option>USD</option>\n                                                    </select>\n                                                </div>\n                                            </div>\n                                        </td>\n                                        <td><input type=\"number\" class=\"form-control r-3-sum-").concat(fieldNumber, "\" name=\"driver_total_sum-").concat(fieldNumber, "\" id=\"driver_total_sum-").concat(fieldNumber, "\"></td>\n                                        <td><input type=\"number\" class=\"form-control r-3-premia-").concat(fieldNumber, "\" name=\"driver_preim_sum-").concat(fieldNumber, "\" id=\"driver_total_sum-").concat(fieldNumber, "\"></td>\n                                    </tr>\n                                    <tr>\n                                        <td><label>\u041F\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u044B</label></td>\n                                        <td><input type=\"number\" class=\"form-control r-3-pass-1-").concat(fieldNumber, "\" name=\"passenger_quantity-").concat(fieldNumber, "\"></td>\n                                        <td>\n                                            <div class=\"input-group mb-4\">\n                                                <input type=\"text\" class=\"form-control r-3-one-1-").concat(fieldNumber, "\" name=\"passenger_one_sum-").concat(fieldNumber, "\">\n                                                <div class=\"input-group-append\">\n                                                    <select class=\"form-control success\" name=\"passenger_currency\" style=\"width: 100%;\">\n                                                        <option selected=\"selected\">UZS</option>\n                                                        <option>USD</option>\n                                                    </select>\n                                                </div>\n                                            </div>\n                                        </td>\n                                        <td><input type=\"number\" class=\"form-control r-3-sum-1-").concat(fieldNumber, "\" name=\"passenger_total_sum-").concat(fieldNumber, "\" id=\"passenger_total_sum-").concat(fieldNumber, "\"></td>\n                                        <td><input type=\"number\" class=\"form-control r-3-premia-1-").concat(fieldNumber, "\" name=\"passenger_preim_sum-").concat(fieldNumber, "\" id=\"passenger_total_sum-").concat(fieldNumber, "\"></td>\n                                    </tr>\n                                    <tr>\n                                        <td><label class=\"text-bold\">\u041E\u0431\u0449\u0438\u0439 \u041B\u0438\u043C\u0438\u0442</label></td>\n                                        <td><input type=\"number\" class=\"form-control r-3-pass-2-").concat(fieldNumber, "\" name=\"limit_quantity-").concat(fieldNumber, "\"></td>\n                                        <td>\n                                            <div class=\"input-group mb-4\">\n                                                <input type=\"text\" class=\"form-control r-3-one-2-").concat(fieldNumber, "\" name=\"limit_one_sum-").concat(fieldNumber, "\">\n                                                <div class=\"input-group-append\">\n                                                    <select class=\"form-control success\" name=\"limit_currency\" style=\"width: 100%;\">\n                                                        <option selected=\"selected\">UZS</option>\n                                                        <option>USD</option>\n                                                    </select>\n                                                </div>\n                                            </div>\n                                        </td>\n                                        <td><input type=\"number\" class=\"form-control r-3-sum-2-").concat(fieldNumber, "\" name=\"limit_total_sum-").concat(fieldNumber, "\"></td>\n                                        <td><input type=\"number\" class=\"form-control r-3-premia-2-").concat(fieldNumber, "\" name=\"limit_preim_sum-").concat(fieldNumber, "\"></td>\n                                    </tr>\n                                    <tr>\n                                        <td colspan=\"3\"><label class=\"text-bold\">\u0418\u0442\u043E\u0433\u043E</label></td>\n                                        <td><input type=\"number\" class=\"form-control r-summ-").concat(fieldNumber, "\"></td>\n                                        <td><input type=\"number\" class=\"form-control r-summ-premia-").concat(fieldNumber, "\"></td>\n                                    </tr>\n                                </tbody>\n                            </table>\n                        </form>\n                    </div>\n                    <div class=\"form-group col-sm-8\">\n                        <label>\u041E\u0431\u0449\u0438\u0439 \u043B\u0438\u043C\u0438\u0442 \u043E\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043D\u043D\u043E\u0441\u0442\u0438 </label>\n                        <div class=\"input-group mb-4\">\n                            <input type=\"text\" class=\"form-control\" id=\"totalLimit-").concat(fieldNumber, "\" name=\"total_liability_limit-").concat(fieldNumber, "\">\n                            <div class=\"input-group-append\">\n                                <select class=\"form-control success\" name=\"total_liability_limit_currency-").concat(fieldNumber, "\" style=\"width: 100%;\">\n                                    <option selected=\"selected\">UZS</option>\n                                    <option>USD</option>\n                                </select>\n                            </div>\n                        </div>\n                    </div>\n                </form>\n            </div>\n        </div>\n\n        <div class=\"card card-info polis\" id=\"polis-container\">\n            <div class=\"card-header\">\n                <h3 class=\"card-title\">\u041F\u043E\u043B\u0438\u0441</h3>\n                <div class=\"card-tools\">\n                    <button type=\"button\" class=\"btn btn-tool\" data-card-widget=\"collapse\" data-toggle=\"tooltip\" title=\"Collapse\">\n                    <i class=\"fas fa-minus\"></i>\n                </button>\n                </div>\n            </div>\n            <div class=\"card payment\">\n                <div class=\"card-body\">\n                    <form method=\"POST\" id=\"polis-fields-").concat(fieldNumber, "\">\n                        <div class=\"row policy\">\n                            <div class=\"col-sm-4\">\n                                <div class=\"form-group\">\n                                    <label for=\"polises\">\u041F\u043E\u043B\u0438\u0441</label>\n                                    <select class=\"form-control polises\" id=\"polises\" name=\"policy-").concat(fieldNumber, "\" style=\"width: 100%;\">\n                                        <option selected=\"selected\"></option>\n                                    </select>\n                                    <div class=\"input-group mb-3\">\n                                        <div class=\"input-group-prepend\">\n                                        </div>\n                                    </div>\n                                </div>\n                            </div>\n                            <div class=\"col-sm-4\">\n                                <div class=\"form-group\">\n                                    <div class=\"input-group mb-3\" style=\"margin-top: 33px\">\n                                        <div class=\"input-group-prepend\">\n                                            <span class=\"input-group-text\">\u043E\u0442</span>\n                                        </div>\n                                        <input type=\"date\" class=\"form-control\" name=\"from_date-").concat(fieldNumber, "\">\n                                    </div>\n                                </div>\n                            </div>\n                            <div class=\"col-sm-4\">\n                                <div class=\"form-group\">\n                                    <label>\u041E\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043D\u043D\u044B\u0439 \u0410\u0433\u0435\u043D\u0442</label>\n                                    <select class=\"form-control select2\" name=\"agent-").concat(fieldNumber, "\" style=\"width: 100%;\">\n                                        <option selected=\"selected\">\u0424.\u0418.\u041E \u0430\u0433\u0435\u043D\u0442\u0430</option>\n                                        <option></option>\n                                    </select>\n                                </div>\n                            </div>\n                        </div>\n                        <div class=\"row\">\n                            <div class=\"col-md-6\">\n                                <div class=\"form-group\">\n                                    <label>\u041E\u043F\u043B\u0430\u0442\u0430 \u0441\u0442\u0440\u0430\u0445\u043E\u0432\u043E\u0439 \u043F\u0440\u0435\u043C\u0438\u0438</label>\n                                    <select class=\"form-control select2\" name=\"payment-").concat(fieldNumber, "\" style=\"width: 100%;\">\n                                        <option selected=\"selected\">\u0421\u0443\u043C</option>\n                                        <option>\u0414\u043E\u043B\u043B\u0430\u0440</option>\n                                        <option>\u0415\u0432\u0440\u043E</option>\n                                    </select>\n                                </div>\n                            </div>\n                            <div class=\"col-md-6\">\n                                <div class=\"form-group\">\n                                    <label>\u041F\u043E\u0440\u044F\u0434\u043E\u043A \u043E\u043F\u043B\u0430\u0442\u044B</label>\n                                        <select class=\"form-control select2\" name=\"payment-order-").concat(fieldNumber, "\" style=\"width: 100%;\">\n                                        <option selected=\"selected\">\u0421\u0443\u043C</option>\n                                        <option>\u0414\u043E\u043B\u043B\u0430\u0440</option>\n                                        <option>\u0415\u0432\u0440\u043E</option>\n                                    </select>\n                                </div>\n                            </div>\n                        </div>\n                    </form>\n                </div>\n            </div>\n            <div class=\"card card-info polis\" id=\"Overall\">\n                <div class=\"card-header\">\n                    <h3 class=\"card-title\">\u0418\u0442\u043E\u0433\u043E</h3>\n                    <div class=\"card-tools\">\n                        <button type=\"button\" class=\"btn btn-tool\" data-card-widget=\"collapse\" data-toggle=\"tooltip\" title=\"Collapse\">\n                        <i class=\"fas fa-minus\"></i>\n                    </button>\n                    </div>\n                </div>\n                <div class=\"card-body\">\n                    <div class=\"form-group\">\n                        <div class=\"input-group mb-3\">\n                            <div class=\"input-group-prepend\">\n                                <span class=\"input-group-text\">\u041E\u0431\u0449\u0430\u044F \u0441\u0442\u0440\u0430\u0445\u043E\u0432\u0430\u044F \u0441\u0443\u043C\u043C\u0430</span>\n                            </div>\n                            <input type=\"text\" class=\"form-control\" readonly id=\"overall-sum-").concat(fieldNumber, "\">\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n        ");
  generalProductFields.append(fields);
}