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
            if (columnName === 'insurance_cost-') {
                ele.setAttribute('class', 'form-control forsum2');
                console.log(columnName);
            } else if (columnName === 'insurance_sum-') {
                ele.setAttribute('class', 'form-control forsum insurance_sum-' + productFieldNumber);
                ele.setAttribute('data-field-number', productFieldNumber);
                console.log(columnName);
            } else if (columnName === 'insurance_premium-') {
                ele.setAttribute('class', 'form-control forsum3 insurance_premium-' + productFieldNumber);
                ele.setAttribute('readonly', 'true');
                console.log(columnName);
            } else if (columnName === 'overall_insurance_sum-') {
                ele.setAttribute('class', 'form-control forsum4 overall_insurance_sum-' + productFieldNumber);
                ele.setAttribute('readonly', 'true');
                console.log(columnName);
            } else {
                ele.setAttribute('class', 'form-control');
                console.log(columnName);
            }
            console.log(columnName);
            td.appendChild(ele);
        }
    }

    addProductFields(productFieldNumber);
}

$(document).ready(function() {
    $(document).on("keyup", ".forsum", calculateSum);
    $(document).on("keyup", ".forsum2", calculateSum2);
    $(document).on("keyup", ".forsum3", calculateSum3);
    $(document).on("change", ".forsum4", calculateSum4);
    $(document).on("keyup", ".forsum4", calculateSum4);
});

$(document).on("keyup", ".modal", function() {
    let fieldNumber = $(this).data('field-number');
    overallSum = parseFloat($('#insurance_sum-' + fieldNumber).val() || 0) + parseFloat($('#civil_liability_sum-' + fieldNumber).val() || 0) +
        parseFloat($('#passenger_total_sum-' + fieldNumber).val() || 0) + parseFloat($('#driver_total_sum-' + fieldNumber).val() || 0) +
        parseFloat($('#vehicle_damage_sum-' + fieldNumber).val() || 0);
    $('#overall-sum-' + fieldNumber).val(overallSum);
    overAllInsurenceSumByField(fieldNumber);
});

function overAllInsurenceSumByField(fieldNumber) {
    let overallSum = $('#overall-sum-' + fieldNumber).val() || 0;
    Osum = parseFloat(overallSum) + parseFloat($('.insurance_sum-' + fieldNumber).val() || 0);
    $('.overall_insurance_sum-' + fieldNumber).val(Osum);
    $('.insurance_premium-' + fieldNumber).val(Osum * 0.01); // франшиза 1% -> премия 1% от общей суммы
    calculateSum3();
    calculateSum4();
}


function calculateSum() {

    let sum = 0;
    $('.forsum').each(function() {

        if (!isNaN(this.value) && this.value.length != 0) {
            sum += parseFloat(this.value);
        }

    });
    $('.overall-sum').val(sum.toFixed(2));
    let fieldNumber = $(this).data('field-number');
    overAllInsurenceSumByField(fieldNumber);
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

function calculateSum4() {

    let sum = 0;
    $('.forsum4').each(function() {

        if (!isNaN(this.value) && this.value.length != 0) {
            sum += parseFloat(this.value);
        }

    });
    $('.overall-sum4').val(sum.toFixed(2));
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

function otherInsurance() {
    // Get the checkbox
    let checkBox = document.getElementById("other_insurance");
    // Get the output text
    let text = document.getElementById("other_insurance_info");

    // If the checkbox is checked, display the output text
    if (checkBox.value === 'yes') {
        text.style.display = "block";
    } else {
        text.style.display = "none";
    }
}

$(document).ready(function() {
    $('.other_insurance').click(function() {
        let targetBox = $('.other_insurance_info');
        if ($(this).attr("value") === 'yes') {
            $(targetBox).show();
        } else {
            $(targetBox).hide();
        }
    });
});

$(document).ready(function() {
    $('.defects').click(function() {
        let targetBox = $('.defects_images');
        if ($(this).attr("value") === 'yes') {
            $(targetBox).show();
        } else {
            $(targetBox).hide();
        }
    });
});



//ToDo: delete one of the addproductfields function
function addProductFields(fieldNumber) {
    let fields = `
          <div id="product-field-modal-${fieldNumber}" class="modal" data-field-number="${fieldNumber}">
            <div class="modal-content" id="product-field-modal-content-${fieldNumber}">
              <span class="close product-fields-close" id="product-fields-close-${fieldNumber}" data-field-number="${fieldNumber}">&times;</span>
              <div class="card card-success">
                <div class="card-header">
                  <h3 class="card-title">Перечень дополнительного оборудования</h3>
                  <div class="card-tools">
                    <button type="button" class="btn btn-tool" data-card-widget="collapse" data-toggle="tooltip" title="Collapse">
                      <i class="fas fa-minus"></i></button>
                  </div>
                </div>
                <div class="card-body">
                  <div class="table-responsive p-0 " style="max-height: 300px;">
                    <form method="POST" id="product-fields-${fieldNumber}-1">
                      <table class="table table-hover table-head-fixed" id="empTable2">
                        <thead>
                        <tr>
                          <th class="text-nowrap">Марка, модель, модификация ТС</th>
                          <th>Наименование оборудования</th>
                          <th>Серийный номер</th>
                          <th>Страховая сумма</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                          <td><input type="text" class="form-control" name="mark_model"></td>
                          <td><input type="text" class="form-control" name="name"></td>
                          <td><input type="text" class="form-control" name="series_number"></td>
                          <td><input type="text" class="form-control" name="insurance_sum" id="insurance_sum-${fieldNumber}"></td>
                        </tr>
                        <tr>
                          <td colspan="3"><label class="text-bold">Итого</label></td>
                          <td><input type="text" class="form-control" name="total"></td>
                        </tr>
                        </tbody>
                      </table>
                    </form>
                  </div>
                </div>
              </div>

              <div class="card card-success">
                <div class="card-header">
                  <h3 class="card-title">Дополнительное страховое покрытие</h3>
                  <div class="card-tools">
                    <button type="button" class="btn btn-tool" data-card-widget="collapse" data-toggle="tooltip" title="Collapse">
                      <i class="fas fa-minus"></i></button>
                  </div>
                </div>

                <div class="card-body">
                  <form method="POST" id="product-fields-${fieldNumber}-2">
                    <div class="form-group">
                      <label>Покрытие террористических актов с ТС </label>
                      <div class="input-group mb-4">
                        <input type="text" class="form-control" name="cover_terror_attacks_sum">
                        <div class="input-group-append">
                          <select class="form-control success" name="cover_terror_attacks_currency" style="width: 100%;">
                            <option selected="selected">UZS</option>
                            <option>USD</option>
                          </select>
                        </div>
                      </div>
                    </div>
                    
                    <div class="form-group">
                      <label>Покрытие террористических актов с застрахованными лицами </label>
                       <div class="input-group mb-4">
                        <input type="text" class="form-control" name="cover_terror_attacks_insured_sum">
                        <div class="input-group-append">
                          <select class="form-control success" name="cover_terror_attacks_insured_currency" style="width: 100%;">
                            <option selected="selected">UZS</option>
                            <option>USD</option>
                          </select>
                        </div>
                      </div>
                    </div>
                    
                    <div class="form-group">
                      <label>Покрытие расходы по эвакуации</label>
                      <div class="input-group mb-4">
                        <input type="text" class="form-control" name="coverage_evacuation_cost">
                        <div class="input-group-append">
                          <select class="form-control success" name="coverage_evacuation_currency" style="width: 100%;">
                            <option selected="selected">UZS</option>
                            <option>USD</option>
                          </select>
                        </div>
                      </div>
                    </div>
                  </form>
                </div>
              </div>

              <div class="card card-success">
                <div class="card-header">
                  <h3 class="card-title">Сведени о трансортных средствах</h3>
                  <div class="card-tools">
                    <button type="button" class="btn btn-tool" data-card-widget="collapse" data-toggle="tooltip" title="Collapse">
                      <i class="fas fa-minus"></i></button>
                  </div>
                </div>
                <div class="card-body">
                  <form method="POST" id="product-fields-${fieldNumber}-3">
                    <div class="form-group">
                      <label>Застрахованы ли автотранспортные средства на момент заполнения настоящей анкеты? </label>
                      <div class="form-check">
                        <input class="form-check-input other_insurance" type="radio" name="other_insurance" id="other_insurance-${fieldNumber}" value="1">
                        <label class="form-check-label">Да</label>
                      </div>
                      <div class="form-check">
                        <input class="form-check-input other_insurance" type="radio" name="other_insurance" value="0">
                        <label class="form-check-label">Нет</label>
                      </div>
                    </div>
                    <div class="form-group other_insurance_info" style="display:none">
                      <label>Укажите название и адрес страховой организации и номер Полиса</label>
                      <input class="form-control" type="text" name="other_insurance_info">
                    </div>
                  </form>
                </div>
              </div>

              <div class="card card-success">
                <div class="card-header">
                  <h3 class="card-title">Страховые покрытия по видам опасностей </h3>
                  <div class="card-tools">
                    <button type="button" class="btn btn-tool" data-card-widget="collapse" data-toggle="tooltip" title="Collapse">
                      <i class="fas fa-minus"></i></button>
                  </div>
                </div>
                <div class="card-body">
                  <form method="POST" id="product-fields-${fieldNumber}-4">
                    <div class="form-group">
                      <label>Раздел I. Гибель или повреждение транспортного средства</label>
                      <div class="row">
                        <div class="col-sm-1">
                          <div class="checkbox icheck-success">
                            <input type="radio" name="vehicle_damage" checked id="radioSuccess3-${fieldNumber}" value="1">
                            <label for="radioSuccess3-${fieldNumber}">Да</label>
                          </div>
                          <div class="checkbox icheck-success">
                            <input type="radio" name="vehicle_damage" id="radioSuccess4-${fieldNumber}" value="0">
                            <label for="radioSuccess4-${fieldNumber}">Нет</label>
                          </div>
                        </div>
                      <div class="col-sm-3">
                        <div class="form-group">
                          <div class="input-group mb-3">
                            <div class="input-group-prepend">
                              <span class="input-group-text">Сумма</span>
                            </div>
                            <input type="text" class="form-control" name="vehicle_damage_sum" id="vehicle_damage_sum-${fieldNumber}">
                          </div>
                        </div>
                      </div>

                    
                      </div>
                    </div>
                  </form>

                  <form method="POST" id="product-fields-${fieldNumber}-5">
                    <div class="form-group">
                      <label class=>Раздел II. Автогражданская ответственность</label>
                      <div class="row">
                        <div class="col-sm-1">
                          <div class="checkbox icheck-success">
                            <input type="radio" name="civil_liability" checked id="radioSuccess5-${fieldNumber}" value="1">
                            <label for="radioSuccess5-${fieldNumber}">Да</label>
                          </div>
                          <div class="checkbox icheck-success">
                            <input type="radio" name="civil_liability" id="radioSuccess6-${fieldNumber}" value="0">
                            <label for="radioSuccess6-${fieldNumber}">Нет</label>
                          </div>
                        </div>
                        <div class="col-sm-4">
                          <div class="form-group">
                            <div class="input-group mb-3">
                              <div class="input-group-prepend">
                                <span class="input-group-text">Сумма</span>
                              </div>
                              <input type="text" class="form-control" name="civil_liability_sum" id="civil_liability_sum-${fieldNumber}">
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </form>

                  <form method="POST" id="product-fields-${fieldNumber}-6">
                    <div class="form-group">
                      <label>Раздел III. Несчастные случаи с Застрахованными лицами</label>
                      <div class="row">
                        <div class="col-sm-1">
                          <div class="checkbox icheck-success">
                            <input type="radio" name="accidents" checked id="radioSuccess7-${fieldNumber}" value="1">
                            <label for="radioSuccess3-${fieldNumber}">Да</label>
                          </div>
                          <div class="checkbox icheck-success">
                            <input type="radio" name="vehicle_damage" id="radioSuccess8-${fieldNumber}" value="0">
                            <label for="radioSuccess4-${fieldNumber}">Нет</label>
                          </div>
                        </div>
                      <div class="col-sm-3">
                        <div class="form-group">
                          <div class="input-group mb-3">
                            <div class="input-group-prepend">
                              <span class="input-group-text">Сумма</span>
                            </div>
                            <input type="text" class="form-control" name="vehicle_damage_sum" id="vehicle_damage_sum-${fieldNumber}">
                          </div>
                        </div>
                      </div>

                    
                      </div>
                    </div>
                  </form>

                  <div class="table-responsive p-0 ">
                    <form method="POST" id="product-fields-${fieldNumber}-7">
                      <table class="table table-hover table-head-fixed">
                        <thead>
                        <tr>
                          <th>Объекты страхования </th>
                          <th>Количество водителей /пассажиров</th>
                          <th>Страховая сумма на одного лица</th>
                          <th>Страховая сумма</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                          <td><label>Водитель(и)</label></td>
                          <td><input type="number" class="form-control" name="driver_quantity"></td>
                          <td><div class="input-group mb-4">
                            <input type="text" class="form-control" name="driver_one_sum">
                            <div class="input-group-append">
                              <select class="form-control success" name="driver_currency" style="width: 100%;">
                                <option selected="selected">UZS</option>
                                <option>USD</option>
                              </select>
                            </div>
                          </div></td>
                          <td><input type="number" class="form-control" name="driver_total_sum"  id="driver_total_sum-${fieldNumber}"></td>
                        </tr>
                        <tr>
                          <td><label>Пассажиры</label></td>
                          <td><input type="number" class="form-control" name="passenger_quantity"></td>
                          <td><div class="input-group mb-4">
                            <input type="text" class="form-control" name="passenger_one_sum">
                            <div class="input-group-append">
                              <select class="form-control success" name="passenger_currency" style="width: 100%;">
                                <option selected="selected">UZS</option>
                                <option>USD</option>
                              </select>
                            </div>
                          </div>
                          </td>
                          <td><input type="number" class="form-control" name="passenger_total_sum" id="passenger_total_sum-${fieldNumber}"></td>
                        </tr>
                        <tr>
                          <td><label class="text-bold">Общий Лимит</label></td>
                          <td><input type="number" class="form-control" name="limit_quantity"></td>
                          <td><div class="input-group mb-4">
                            <input type="text" class="form-control" name="limit_one_sum">
                            <div class="input-group-append">
                              <select class="form-control success" name="limit_currency" style="width: 100%;">
                                <option selected="selected">UZS</option>
                                <option>USD</option>
                              </select>
                            </div>
                          </div></td>
                          <td><input type="number" class="form-control" name="limit_total_sum" id="limit_total_sum-${fieldNumber}"></td>
                        </tr>
                        <tr>
                          <td colspan="3"><label class="text-bold">Итого</label></td>
                          <td><input type="number" readonly class="form-control" name="total"></td>
                        </tr>
                        </tbody>
                      </table>
                    </form>
                  </div>
                  <div class="form-group col-sm-8">
                    <label>Общий лимит ответственности </label>
                    <div class="input-group mb-4">
                      <input type="text" class="form-control" name="total_liability_limit">
                      <div class="input-group-append">
                        <select class="form-control success" name="total_liability_limit_currency" style="width: 100%;">
                          <option selected="selected">UZS</option>
                          <option>USD</option>
                        </select>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="card card-info polis" id="polis-container">
                <div class="card-header">
                  <h3 class="card-title">Полис</h3>
                  <div class="card-tools">
                    <button type="button" class="btn btn-tool" data-card-widget="collapse" data-toggle="tooltip" title="Collapse">
                      <i class="fas fa-minus"></i></button>
                  </div>
                </div>
                <div class="card-body">
                  <!-- Default box -->
                  <div class="card card-success">
                    <div class="card-header">
                      <h3 class="card-title">Общие Сведения:</h3>
                      <div class="card-tools">
                        <button type="button" class="btn btn-tool" data-card-widget="collapse" data-toggle="tooltip" title="Collapse">
                          <i class="fas fa-minus"></i></button>
                      </div>
                    </div>
                    <div class="card-body">
                      <form method="POST" id="polis-fields-${fieldNumber}">
                        <div class="row policy">
                          <div class="col-sm-4">
                            <div class="form-group">
                              <label for="polises">Полис</label>
                              <select class="form-control polises" id="polises" name="policy" style="width: 100%;">
                                <option selected="selected"></option>
                              </select>
                              <div class="input-group mb-3">
                                <div class="input-group-prepend">
                                </div>
                              </div>
                            </div>
                          </div>
                          <div class="col-sm-4">
                            <div class="form-group">
                              <div class="input-group mb-3" style="margin-top: 33px">
                                <div class="input-group-prepend">
                                  <span class="input-group-text">от</span>
                                </div>
                                <input type="date" class="form-control" name="from_date">
                              </div>
                            </div>
                          </div>
                          <div class="col-sm-4">
                            <div class="form-group">
                              <label>Ответственный Агент</label>
                              <select class="form-control select2" name="agent" style="width: 100%;">
                                <option selected="selected">Ф.И.О агента</option>
                                <option></option>
                              </select>
                            </div>
                          </div>
                        </div>
                      </form>

                      <!-- /.card-footer-->
                    </div>
                    <!-- /.card -->
                  </div>
                </div>
                <div class="card-footer">
                  <button type="submit" class="btn btn-primary float-right">Сохранить</button>
                </div>
              </div>
              <div class="card payment">
                <div class="card-body">
                  <div class="row">
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Оплата страховой премии</label>
                        <select class="form-control select2" name="payment" style="width: 100%;">
                          <option selected="selected">Сум</option>
                          <option>Доллар</option>
                          <option>Евро</option>
                        </select>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Порядок оплаты</label>
                        <select class="form-control select2" name="payment-order" style="width: 100%;">
                          <option selected="selected">Сум</option>
                          <option>Доллар</option>
                          <option>Евро</option>
                        </select>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="card card-info " id="Overall">
                <div class="card-header">
                  <h3 class="card-title">Итого</h3>
                  <div class="card-tools">
                    <button type="button" class="btn btn-tool" data-card-widget="collapse" data-toggle="tooltip" title="Collapse">
                      <i class="fas fa-minus"></i></button>
                  </div>
                </div>
                <div class="card-body">
                   <div class="form-group">
                      <div class="input-group mb-3">
                            <div class="input-group-prepend">
                              <span class="input-group-text">Общая страховая сумма</span>
                            </div>
                            <input type="text" class="form-control" readonly id="overall-sum-${fieldNumber}">
                      </div>
                   </div>
                </div>
             
              </div>
            </div>
          </div>
        `;

    generalProductFields.append(fields);
}