function addRow() {
    let empTab = document.getElementById('empTable');
    var fieldNames = [
        'polis-num-',
        'polis-series-',
        'period_polis-',
        'polis-agent-',
        'polis-id-',
        'polis-mark-',
        'polis-model-',
        'polis-modification-',
        'polis-gos-num-',
        'polis-teh-passport-',
        'polis-num-engine-',
        'polis-num-body-',
        'polis-payload-',
        'polis-places-',
        'insurance_sum-',
        'overall_insurance_sum-',
        'insurance_premium-',
    ];
    let rowCnt = empTab.rows.length; // get the number of rows.
    let tr = empTab.insertRow(rowCnt - 1); // table row.

    productFieldNumber++;

    var rowsAmount = $("#empTable thead tr th").length + 1;

    for (let c = 0; c < rowsAmount; c++) {
        let td = document.createElement('td'); // TABLE DEFINITION.
        td = tr.insertCell(c);

        if (c == (rowsAmount - 1)) { // if its the last column of the table.
            // add delete a button
            let button = document.createElement('input');

            // set the attributes.
            button.setAttribute('type', 'button');
            button.setAttribute('value', 'Удалить');

            // add button's "onclick" event.
            button.setAttribute('onclick', 'removeRow(this)');
            button.setAttribute('data-field-number', productFieldNumber);
            button.setAttribute('class', 'btn btn-warning');

            td.appendChild(button);

            // add delete a button
            let button2 = document.createElement('input');
            button2.setAttribute('type', 'button');
            button2.setAttribute('value', 'Заполнить');
            button2.setAttribute('class', 'btn btn-success product-fields-button');
            button2.setAttribute('id', 'product-fields-button-' + productFieldNumber);
            button2.setAttribute('data-field-number', productFieldNumber);

            let td2 = document.createElement('td'); // TABLE DEFINITION.
            let fieldNumer = c + 1;
            td2 = tr.insertCell(fieldNumer);
            td2.appendChild(button2);
        } else {
            // all except the last colum will have input field.
            let ele = document.createElement('input');

            let fieldIndex = c + 1;
            let columnName = fieldNames[c];
            ele.setAttribute('name', columnName + productFieldNumber);

            if (c === 1) {
                ele = document.createElement('select');
            } else if (c === 3) {
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


let num1 = 1;
let num2 = 1;
$('#insurer-modal-button').on('click', function() {

    let clone = $('#clone-insurance:last').clone();
    clone.insertAfter('#clone-insurance:last');

    clone.find('#insurer-name').attr('name', `insurer-name${num1}`);
    clone.find('#insurer-address').attr('name', `insurer-address${num1}`);
    clone.find('#insurer-tel').attr('name', `insurer-tel${num1}`);
    clone.find('#insurer-schet').attr('name', `insurer-schet${num1}`);
    clone.find('#insurer-inn').attr('name', `insurer-inn${num1}`);
    clone.find('#insurer-mfo').attr('name', `insurer-mfo${num1}`);
    clone.find('#insurer-bank').attr('name', `insurer-bank${num1}`);
    clone.find('#insurer-okonh').attr('name', `insurer-okonh${num1}`);
    clone.find('#insurer-name').attr('id', `insurer-name${num1}`)
    clone.find('#insurer-address').attr('id', `insurer-address${num1}`)
    clone.find('#insurer-tel').attr('id', `insurer-tel${num1}`)
    clone.find('#insurer-schet').attr('id', `insurer-schet${num1}`)
    clone.find('#insurer-inn').attr('id', `insurer-inn${num1}`)
    clone.find('#insurer-mfo').attr('id', `insurer-mfo${num1}`)
    clone.find('#insurer-bank').attr('id', `insurer-bank${num1}`)
    clone.find('#insurer-okonh').attr('id', `insurer-okonh${num1}`)
    clone.find('#insurer-name').prev().attr('for', `insurer-name${num1}`)
    clone.find('#insurer-address').prev().attr('for', `insurer-address${num1}`)
    clone.find('#insurer-tel').prev().attr('for', `insurer-tel${num1}`)
    clone.find('#insurer-schet').prev().attr('for', `insurer-schet${num1}`)
    clone.find('#insurer-inn').prev().attr('for', `insurer-inn${num1}`)
    clone.find('#insurer-mfo').prev().attr('for', `insurer-mfo${num1}`)
    clone.find('#insurer-bank').prev().attr('for', `insurer-bank${num1}`)
    clone.find('#insurer-okonh').prev().attr('for', `insurer-okonh${num1}`)
    num1++;
    clone.find('.card-title').html(`Страхователь №${num1}`)
    clone.find('#insurer-modal-button').html(`Удалить`).attr('class', 'btn btn-warning')
    clone.find('#insurer-modal-button').on('click', function() {
        $(this).parent().parent().parent().remove();
        num1--;
    })
});

$('#beneficiary-modal-button').on('click', function() {

    let clone = $('#clone-beneficiary:last').clone();
    clone.insertAfter('#clone-beneficiary:first');

    clone.find('#beneficiary-name').attr('name', `beneficiary-name${num2}`);
    clone.find('#beneficiary-address').attr('name', `beneficiary-address${num2}`);
    clone.find('#beneficiary-tel').attr('name', `beneficiary-tel${num2}`);
    clone.find('#beneficiary-schet').attr('name', `beneficiary-schet${num2}`);
    clone.find('#beneficiary-inn').attr('name', `beneficiary-inn${num2}`);
    clone.find('#beneficiary-mfo').attr('name', `beneficiary-mfo${num2}`);
    clone.find('#beneficiary-bank').attr('name', `beneficiary-bank${num2}`);
    clone.find('#beneficiary-okonh').attr('name', `beneficiary-okonh${num2}`);
    clone.find('#beneficiary-name').attr('id', `beneficiary-name${num2}`)
    clone.find('#beneficiary-address').attr('id', `beneficiary-address${num2}`)
    clone.find('#beneficiary-tel').attr('id', `beneficiary-tel${num2}`)
    clone.find('#beneficiary-schet').attr('id', `beneficiary-schet${num2}`)
    clone.find('#beneficiary-inn').attr('id', `beneficiary-inn${num2}`)
    clone.find('#beneficiary-mfo').attr('id', `beneficiary-mfo${num2}`)
    clone.find('#beneficiary-bank').attr('id', `beneficiary-bank${num2}`)
    clone.find('#beneficiary-okonh').attr('id', `beneficiary-okonh${num2}`)
    clone.find('#beneficiary-name').prev().attr('for', `beneficiary-name${num2}`)
    clone.find('#beneficiary-address').prev().attr('for', `beneficiary-address${num2}`)
    clone.find('#beneficiary-tel').prev().attr('for', `beneficiary-tel${num2}`)
    clone.find('#beneficiary-schet').prev().attr('for', `beneficiary-schet${num2}`)
    clone.find('#beneficiary-inn').prev().attr('for', `beneficiary-inn${num2}`)
    clone.find('#beneficiary-mfo').prev().attr('for', `beneficiary-mfo${num2}`)
    clone.find('#beneficiary-bank').prev().attr('for', `beneficiary-bank${num2}`)
    clone.find('#beneficiary-okonh').prev().attr('for', `beneficiary-okonh${num2}`)
    num2++;
    clone.find('.card-title').html(`Выгодоприобретатель №${num2}`)
    clone.find('#beneficiary-modal-button').html(`Удалить`).attr('class', 'btn btn-warning')
    clone.find('#beneficiary-modal-button').on('click', function() {
        $(this).parent().parent().parent().remove();
        num2--;
    })

});

$(document).ready(function() {
    $(document).on("keyup", ".forsum", calculateSum);
    $(document).on("keyup", ".forsum2", calculateSum2);
    $(document).on("keyup", ".forsum3", calculateSum3);
    $(document).on("keyup", ".forsum4", calculateSum4);
    $(document).on("keyup", ".forsum5", calculateSum5);
    $('.defects').on('change', function() {
        console.log('sa');
        let targetBox = $('.defects_images');
        if ($(this).attr("value") === '1') {
            $(targetBox).show(400);
        } else {
            $(targetBox).hide(400);
        }
    });
});
$(document).on('keyup', function() {
    if ($('.overall-sum4').val() < $('.overall-sum').val()) {
        alert('Страховая стоимость не должна превышать страховую сумму')
        $('#form-save-button').attr('disabled', true)
    } else {
        $('#form-save-button').removeAttr('disabled');
    }
});

$(document).on("keyup", ".modal", function() {
    let fieldNumber = $(this).data('field-number');
    overallSum =
        parseFloat($('#insurance_sum-' + fieldNumber).val() || 0) +
        parseFloat($('.terror-tc-' + fieldNumber).val() || 0) +
        parseFloat($('.terror-zl-' + fieldNumber).val() || 0) +
        parseFloat($('.evocuation-' + fieldNumber).val() || 0) +
        parseFloat($('.r-1-sum-' + fieldNumber).val() || 0) +
        parseFloat($('.r-2-sum-' + fieldNumber).val() || 0) +
        parseFloat($('.r-3-sum-' + fieldNumber).val() || 0) +
        parseFloat($('.r-3-sum-1-' + fieldNumber).val() || 0) +
        parseFloat($('.r-3-sum-2-' + fieldNumber).val() || 0);
    let modalTableSum2 =
        parseFloat($('.r-3-sum-' + fieldNumber).val() || 0) +
        parseFloat($('.r-3-sum-1-' + fieldNumber).val() || 0) +
        parseFloat($('.r-3-sum-2-' + fieldNumber).val() || 0);
    let modalTableSum3 =
        parseFloat($('.r-3-premia-' + fieldNumber).val() || 0) +
        parseFloat($('.r-3-premia-1-' + fieldNumber).val() || 0) +
        parseFloat($('.r-3-premia-2-' + fieldNumber).val() || 0);
    $('#overall-sum-' + fieldNumber).val(overallSum);
    $('.r-summ-' + fieldNumber).val(modalTableSum2);
    $('.r-summ-premia-' + fieldNumber).val(modalTableSum3);

    $('#totalLimit-' + fieldNumber).on('keyup', function() {
        if ($('.r-summ-' + fieldNumber).val() >= $('#totalLimit-' + fieldNumber).val()) {
            $('#form-save-button').attr('disabled', true)
                // alert('Общий лимит ответственности не может превышать страховую сумму по видам опасностей');
        } else {
            $('#form-save-button').removeAttr('disabled');

        }
    });

    calculateSum4(fieldNumber);
});

$(document).on("change", ".modal", function() {
    let fieldNumber = $(this).data('field-number');

    $('.other_insurance-' + fieldNumber).on('change', function() {
        let targetBox = $(this).parent().parent().parent().parent().parent().find('.other_insurance_info-' + fieldNumber);
        if ($(this).attr("value") === '1') {
            $(targetBox).show(400);
        } else {
            $(targetBox).hide(400);
        }
    });
    $('.r-1-' + fieldNumber).on('change', function() {
        let targetBox = $('.r-1-show-' + fieldNumber);
        if ($(this).attr("value") === '1') {
            $(targetBox).show(400);
        } else {
            $(targetBox).hide(400);
        }
    });
    $('.r-2-' + fieldNumber).on('change', function() {
        let targetBox = $(`.r-2-show-${fieldNumber}`);
        if ($(this).attr("value") === '1') {
            $(targetBox).show(400);
        } else {
            $(targetBox).hide(400);
        }
    });
    $('.r-3-' + fieldNumber).on('change', function() {
        let targetBox = $(`.r-3-show-${fieldNumber}`);
        if ($(this).attr("value") === '1') {
            $(targetBox).show(400);
        } else {
            $(targetBox).hide(400);
        }
    });
    $('.r-3-one-' + fieldNumber).on('keyup', function() {
        let numOne = $(this).val() * $(`.r-3-pass-${fieldNumber}`).val();
        $(document).find(`.r-3-sum-${fieldNumber}`).val(numOne);
    });
    $('.r-3-pass-1-' + fieldNumber).on('keyup', function() {
        let numOne = $(this).val() * $(`.r-3-one-1-${fieldNumber}`).val();
        $(document).find(`.r-3-sum-1-${fieldNumber}`).val(numOne);
    });
    $('.r-3-one-1-' + fieldNumber).on('keyup', function() {
        let numOne = $(this).val() * $(`.r-3-pass-1-${fieldNumber}`).val();
        $(document).find(`.r-3-sum-1-${fieldNumber}`).val(numOne);
    });
    $('.r-3-pass-2-' + fieldNumber).on('keyup', function() {
        let numOne = $(this).val() * $(`.r-3-one-2-${fieldNumber}`).val();
        $(document).find(`.r-3-sum-2-${fieldNumber}`).val(numOne);
    });
    $('.r-3-one-2-' + fieldNumber).on('keyup', function() {
        let numOne = $(this).val() * $(`.r-3-pass-2-${fieldNumber}`).val();
        $(document).find(`.r-3-sum-2-${fieldNumber}`).val(numOne);
    });

});



function calculateSum() {
    let sum = 0;
    $('.forsum').each(function() {
        if (!isNaN(this.value) && this.value.length != 0) {
            sum += parseFloat(this.value);
        }
    });
    $('.overall-sum').val(sum.toFixed(2));
}

function calculateSum2() {
    let sum = 0;
    $('.forsum2').each(function() {
        if (!isNaN(this.value) && this.value.length != 0) {
            sum += parseFloat(this.value);
        }
    });
    $('.overall-sum2').val(sum.toFixed(2));
}

function calculateSum3() {
    let sum = 0;
    $('.forsum3').each(function() {
        if (!isNaN(this.value) && this.value.length != 0) {
            sum += parseFloat(this.value);
        }
    });
    $('.overall-sum3').val(sum.toFixed(2));
}

function calculateSum4(fieldNumber) {
    let sum = 0;
    try {
        $('.forsum4').each(function() {
            if (!isNaN(this.value) && this.value.length != 0) {
                sum = parseFloat(this.value) + parseFloat($('#overall-sum-' + fieldNumber).val())
            }
        });
    } catch {
        $('.forsum4').each(function() {
            if (!isNaN(this.value) && this.value.length != 0) {
                sum = parseFloat(this.value)
            }
        });
    }
    $('.overall-sum4').val(sum.toFixed(2));
}

function calculateSum5() {
    let sum = 0;
    $('.forsum5').each(function() {
        if (!isNaN(this.value) && this.value.length != 0) {
            sum += parseFloat(this.value);
        }
    });
    $('.overall-sum5').val(sum.toFixed(2));
}


// function to delete a row.
function removeRow(oButton) {
    let empTab = document.getElementById('empTable');
    empTab.deleteRow(oButton.parentNode.parentNode.rowIndex); // buttton -> td -> tr
    let id = oButton.dataset.fieldNumber;
    $("#product-field-modal-" + id).remove();
    calculateSum();
    calculateSum2();
    calculateSum3();
    calculateSum5();
}

// function to add new row.
function addRow2() {
    let empTab = document.getElementById('empTable2');

    let rowCnt = empTab.rows.length; // get the number of rows.
    let tr = empTab.insertRow(rowCnt - 1); // table row.

    for (let c = 0; c < $("#empTable2 tr th").length; c++) {
        let td = document.createElement('td'); // TABLE DEFINITION.
        td = tr.insertCell(c);

        let ele = document.createElement('input');

        ele.setAttribute('type', 'text');
        ele.setAttribute('class', 'form-control');

        td.appendChild(ele);
    }
}

// function to delete a row.
function removeRow2(oButton) {
    let empTab = document.getElementById('empTable2');
    empTab.deleteRow(oButton.parentNode.parentNode.rowIndex); // buttton -> td -> tr
}

function showDiv(divId, element) {
    document.getElementById(divId).style.display = element.value == 'other' ? 'block' : 'none';
}

function addRow3(fieldNumber, ) {
    let empTab = document.getElementById('empTable3');

    let rowCnt = empTab.rows.length; // get the number of rows.
    let tr = empTab.insertRow(rowCnt); // table row.

    paymentTypeFieldNumber++;

    for (let c = 0; c < $("#empTable3 tr th").length; c++) {
        let td = document.createElement('td'); // TABLE DEFINITION.
        td = tr.insertCell(c);

        if (c == ($("#empTable3 tr th").length - 1)) { // if its the first column of the table.
            // add a button control.
            let button = document.createElement('input');

            // set the attributes.
            button.setAttribute('type', 'button');
            button.setAttribute('value', 'Удалить');

            // add button's "onclick" event.
            button.setAttribute('onclick', 'removeRow3(this)');
            button.setAttribute('class', 'btn btn-warning');

            td.appendChild(button);
        } else {
            // all except the last colum will have input field.
            let ele = document.createElement('input');

            if (c === 1) {
                ele.setAttribute('type', 'date');
                ele.setAttribute('id', `payment_from-${fieldNumber}-${paymentTypeFieldNumber}`);
            } else {
                ele.setAttribute('type', 'text');
                ele.setAttribute('id', `payment_sum-${fieldNumber}-${paymentTypeFieldNumber}`);
            }

            ele.setAttribute('class', 'form-control');
            td.appendChild(ele);
        }
    }
}

// function to delete a row.
function removeRow3(oButton) {
    let empTab = document.getElementById('empTable3');
    empTab.deleteRow(oButton.parentNode.parentNode.rowIndex); // buttton -> td -> tr
}

// function to extract and submit table data.
function submit() {
    let myTab = document.getElementById('empTable');
    let arrValues = [];

    // loop through each row of the table.
    for (row = 1; row < myTab.rows.length - 1; row++) {
        // loop through each cell in a row.
        for (c = 0; c < myTab.rows[row].cells.length; c++) {
            let element = myTab.rows.item(row).cells[c];
            if (element.childNodes[0].getAttribute('type') == 'text') {
                arrValues.push("'" + element.childNodes[0].value + "'");
            }
        }
    }
}
$('#form-save-button').on('click', function() {
    $('#mainFormKasko').submit();
})

//ToDo: delete one of the addproductfields function
function addProductFields(fieldNumber) {
    let fields = `
    <div id="product-field-modal-${fieldNumber}" class="modal" data-field-number="${fieldNumber}">
        <div class="modal-content" id="product-field-modal-content-${fieldNumber}">
            <span class="close product-fields-close" id="product-fields-close-"
                data-field-number="${fieldNumber}">&times;</span>

                <div class="card card-success">
                    <div class="card-header">
                        <h3 class="card-title">Сведени о трансортных средствах</h3>
                        <div class="card-tools">
                            <button type="button" class="btn btn-tool" data-card-widget="collapse"
                                data-toggle="tooltip" title="Collapse">
                                <i class="fas fa-minus"></i>
                            </button>
                        </div>
                    </div>
                           
                    <div class="card-body">
                        <div id="product-fields-${fieldNumber}-3">
                            <div class="form-group">
                                <label>Утрата (Гибель) или повреждение ТС</label>
                                <div class="row">
                                    <div class="col-sm-1">
                                        <div class="checkbox icheck-success">
                                            <input type="radio" class="other_insurance-${fieldNumber}"
                                                name="strtahovka-${fieldNumber}" id="radioSuccess1-${fieldNumber}" value="1">
                                            <label for="radioSuccess1-${fieldNumber}">Да</label>
                                        </div>
                                        <div class="checkbox icheck-success">
                                            <input type="radio" class="other_insurance-${fieldNumber}"
                                                name="strtahovka-${fieldNumber}" id="radioSuccess2-${fieldNumber}" value="0">
                                            <label for="radioSuccess2-${fieldNumber}">Нет</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group other_insurance_info-${fieldNumber}" style="display:none">
                                <label>Укажите название и адрес страховой организации и номер
                                    Полиса</label>
                                <input class="form-control" type="text" name="other_insurance_info">
                            </div>
                        </div>
                    </div>


                    <div class="card-body">
                        <div id="product-fields-${fieldNumber}-3">
                            <div class="form-group">
                                <label>Несчастные случаи с Застрахованными лицами</label>
                                <div class="row">
                                    <div class="col-sm-1">
                                        <div class="checkbox icheck-success">
                                            <input type="radio" class="other_insurance-${fieldNumber}"
                                                name="strtahovka-${fieldNumber}" id="radioSuccess3-${fieldNumber}" value="1">
                                            <label for="radioSuccess3-${fieldNumber}">Да</label>
                                        </div>
                                        <div class="checkbox icheck-success">
                                            <input type="radio" class="other_insurance-${fieldNumber}"
                                                name="strtahovka-${fieldNumber}" id="radioSuccess4-${fieldNumber}" value="0">
                                            <label for="radioSuccess4-${fieldNumber}">Нет</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group other_insurance_info-${fieldNumber}" style="display:none">
                                <label>Укажите название и адрес страховой организации и номер
                                    Полиса</label>
                                <input class="form-control" type="text" name="other_insurance_info">
                            </div>
                        </div>
                    </div>

                    <div class="card-body">
                        <div id="product-fields-${fieldNumber}-3">
                            <div class="form-group">
                                <label>Автогражданская ответственность
                                </label>
                                <div class="row">
                                    <div class="col-sm-1">
                                        <div class="checkbox icheck-success">
                                            <input type="radio" class="other_insurance-${fieldNumber}"
                                                name="strtahovka-${fieldNumber}" id="radioSuccess5-${fieldNumber}" value="1">
                                            <label for="radioSuccess5-${fieldNumber}">Да</label>
                                        </div>
                                        <div class="checkbox icheck-success">
                                            <input type="radio" class="other_insurance-${fieldNumber}"
                                                name="strtahovka-${fieldNumber}" id="radioSuccess6-${fieldNumber}" value="0">
                                            <label for="radioSuccess6-${fieldNumber}">Нет</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group other_insurance_info-${fieldNumber}" style="display:none">
                                <label>Укажите название и адрес страховой организации и номер
                                    Полиса</label>
                                <input class="form-control" type="text" name="other_insurance_info">
                            </div>
                        </div>
                    </div>

                    <div class="card-body">
                        <div id="product-fields-${fieldNumber}-3">
                            <div class="form-group">
                                <label>Застрахованы ли автотранспортные средства на момент заполнения настоящей анкеты?
                                </label>
                                <div class="row">
                                    <div class="col-sm-1">
                                        <div class="checkbox icheck-success">
                                            <input type="radio" class="other_insurance-${fieldNumber}"
                                                name="strtahovka-${fieldNumber}" id="radioSuccess7-${fieldNumber}" value="1">
                                            <label for="radioSuccess7-${fieldNumber}">Да</label>
                                        </div>
                                        <div class="checkbox icheck-success">
                                            <input type="radio" class="other_insurance-${fieldNumber}"
                                                name="strtahovka-${fieldNumber}" id="radioSuccess8-${fieldNumber}" value="0">
                                            <label for="radioSuccess8-${fieldNumber}">Нет</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group other_insurance_info-${fieldNumber}" style="display:none">
                                <label>Укажите название и адрес страховой организации и номер
                                    Полиса</label>
                                <input class="form-control" type="text" name="other_insurance_info">
                            </div>
                        </div>
                    </div>

                    
                    <div class="card-body">
                        <div id="product-fields-${fieldNumber}-3">
                            <div class="form-group">
                                <label>Гибель или повреждение транспортного средства</label>
                                <div class="row">
                                    <div class="col-sm-1">
                                        <div class="checkbox icheck-success">
                                            <input type="radio" class="other_insurance-${fieldNumber}"
                                                name="strtahovka-${fieldNumber}" id="radioSuccess9-${fieldNumber}" value="1">
                                            <label for="radioSuccess9-${fieldNumber}">Да</label>
                                        </div>
                                        <div class="checkbox icheck-success">
                                            <input type="radio" class="other_insurance-${fieldNumber}"
                                                name="strtahovka-${fieldNumber}" id="radioSuccess10-${fieldNumber}" value="0">
                                            <label for="radioSuccess10-${fieldNumber}">Нет</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group other_insurance_info-${fieldNumber}" style="display:none">
                                <label>Укажите название и адрес страховой организации и номер
                                    Полиса</label>
                                <input class="form-control" type="text" name="other_insurance_info">
                            </div>
                        </div>
                    </div>

                          
                    <div class="card-body">
                        <div id="product-fields-${fieldNumber}-3">
                            <div class="form-group">
                                <label>Несчастные случаи с Застрахованными лицами</label>
                                <div class="row">
                                    <div class="col-sm-1">
                                        <div class="checkbox icheck-success">
                                            <input type="radio" class="other_insurance-${fieldNumber}"
                                                name="strtahovka-${fieldNumber}" id="radioSuccess11-${fieldNumber}" value="1">
                                            <label for="radioSuccess11-${fieldNumber}">Да</label>
                                        </div>
                                        <div class="checkbox icheck-success">
                                            <input type="radio" class="other_insurance-${fieldNumber}"
                                                name="strtahovka-${fieldNumber}" id="radioSuccess12-${fieldNumber}" value="0">
                                            <label for="radioSuccess12-${fieldNumber}">Нет</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group other_insurance_info-${fieldNumber}" style="display:none">
                                <label>Укажите название и адрес страховой организации и номер
                                    Полиса</label>
                                <input class="form-control" type="text" name="other_insurance_info">
                            </div>
                        </div>
                    </div>
                </div>
        </div>
    </div>
        `;

    generalProductFields.append(fields);
}