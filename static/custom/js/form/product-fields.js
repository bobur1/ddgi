function addRow() {
    let empTab = document.getElementById('empTable');
    var fieldNames = ['mark_model-',
                      'release_year-',
                      'country_number-',
                      'tech_passport_number-',
                      'engine_number-',
                      'carcase_number-',
                      'lifting_capacity-',
                      'number_of_seats-',
                      'insurance_cost-',
                      'insurance_sum-',
                      'insurance_premium-',
    ];
    let rowCnt = empTab.rows.length;    // get the number of rows.
    let tr = empTab.insertRow(rowCnt - 1); // table row.

    productFieldNumber++;

    var rowsAmount = $("#empTable tr th").length - 1;

    for (let c = 0; c < rowsAmount; c++) {
        let td = document.createElement('td');          // TABLE DEFINITION.
        td = tr.insertCell(c);

        if (c == (rowsAmount - 1)) {   // if its the last column of the table.
            // add delete a button
            let button = document.createElement('input');

            // set the attributes.
            button.setAttribute('type', 'button');
            button.setAttribute('value', 'Удалить');

            // add button's "onclick" event.
            button.setAttribute('onclick', 'removeRow(this)');
            button.setAttribute('class', 'btn btn-warning');

            td.appendChild(button);
        } else {
            // all except the last colum will have input field.
            let ele = document.createElement('input');

            let fieldIndex = c + 1;
            ele.setAttribute('name', fieldNames[c] + productFieldNumber);

            if (c === 1) {
                ele.setAttribute('type', 'date');
            } else {
                ele.setAttribute('type', 'text');
            }
            if (c == ($("#empTable tr th").length - 3)) {
                ele.setAttribute('class', 'form-control forsum2');
            } else if (c == ($("#empTable tr th").length - 2)) {
                ele.setAttribute('class', 'form-control forsum');
            } else {
                ele.setAttribute('class', 'form-control');
            }
            td.appendChild(ele);
        }
    }

    addProductFields(productFieldNumber);
}

$(document).ready(function () {
    $(document).on("keyup", ".forsum", calculateSum);
    $(document).on("keyup", ".forsum2", calculateSum2);
});

function calculateSum() {

    let sum = 0;
    $('.forsum').each(function () {

        if (!isNaN(this.value) && this.value.length != 0) {
            sum += parseFloat(this.value);
        }

    });
    $('.overall-sum').val(sum.toFixed(2));
}

function calculateSum2() {

    let sum = 0;
    $('.forsum2').each(function () {

        if (!isNaN(this.value) && this.value.length != 0) {
            sum += parseFloat(this.value);
        }

    });
    $('.overall-sum2').val(sum.toFixed(2));
}

// function to delete a row.
function removeRow(oButton) {
    let empTab = document.getElementById('empTable');
    empTab.deleteRow(oButton.parentNode.parentNode.rowIndex); // buttton -> td -> tr
    calculateSum();
    calculateSum2();
}

// function to add new row.
function addRow2() {
    let empTab = document.getElementById('empTable2');

    let rowCnt = empTab.rows.length;    // get the number of rows.
    let tr = empTab.insertRow(rowCnt - 1); // table row.

    for (let c = 0; c < $("#empTable2 tr th").length; c++) {
        let td = document.createElement('td');          // TABLE DEFINITION.
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

function addRow3(fieldNumber,) {
    let empTab = document.getElementById('empTable3');

    let rowCnt = empTab.rows.length;    // get the number of rows.
    let tr = empTab.insertRow(rowCnt); // table row.

    paymentTypeFieldNumber++;

    for (let c = 0; c < $("#empTable3 tr th").length; c++) {
        let td = document.createElement('td');          // TABLE DEFINITION.
        td = tr.insertCell(c);

        if (c == ($("#empTable3 tr th").length - 1)) {   // if its the first column of the table.
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

$(document).ready(function () {
    $('.other_insurance').click(function () {
        let targetBox = $('.other_insurance_info');
        if ($(this).attr("value") === 'yes') {
            $(targetBox).show();
        } else {
            $(targetBox).hide();
        }
    });
});

$(document).ready(function () {
    $('.defects').click(function () {
        let targetBox = $('.defects_images');
        if ($(this).attr("value") === 'yes') {
            $(targetBox).show();
        } else {
            $(targetBox).hide();
        }
    });
});


function addProductFields(fieldNumber) {
    let fields = `
          <div id="product-field-modal-${fieldNumber}" class="modal" data-field-number="${fieldNumber}">
            <div class="modal-content" id="product-field-modal-content-${fieldNumber}">
              <span class="close product-fields-close" id="product-fields-close-${fieldNumber}" data-field-number="0">&times;</span>
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
                          <th>Страховая премия</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                          <td><input type="text" class="form-control" name="mark_model-${fieldNumber}"></td>
                          <td><input type="text" class="form-control" name="name-${fieldNumber}"></td>
                          <td><input type="text" class="form-control" name="series_number-${fieldNumber}"></td>
                          <td><input type="text" class="form-control" name="insurance_sum-${fieldNumber}"></td>
                          <td><input type="text" class="form-control" name="insurance_premium-${fieldNumber}"></td>
                        </tr>
                        <tr>
                          <td colspan="4"><label class="text-bold">Итого</label></td>
                          <td><input type="text" class="form-control" name="total-${fieldNumber}"></td>
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
                        <input type="text" class="form-control" name="cover_terror_attacks_sum-${fieldNumber}">
                        <div class="input-group-append">
                          <select class="form-control success" name="cover_terror_attacks_currency-${fieldNumber}" style="width: 100%;">
                            <option selected="selected">UZS</option>
                            <option>USD</option>
                          </select>
                        </div>
                      </div>
                    </div>
                    
                    <div class="form-group">
                      <label>Покрытие террористических актов с застрахованными лицами </label>
                       <div class="input-group mb-4">
                        <input type="text" class="form-control" name="cover_terror_attacks_insured_sum-${fieldNumber}">
                        <div class="input-group-append">
                          <select class="form-control success" name="cover_terror_attacks_insured_currency-${fieldNumber}" style="width: 100%;">
                            <option selected="selected">UZS</option>
                            <option>USD</option>
                          </select>
                        </div>
                      </div>
                    </div>
                    
                    <div class="form-group">
                      <label>Покрытие расходы по эвакуации</label>
                      <div class="input-group mb-4">
                        <input type="text" class="form-control" name="coverage_evacuation_cost-${fieldNumber}">
                        <div class="input-group-append">
                          <select class="form-control success" name="coverage_evacuation_currency-${fieldNumber}" style="width: 100%;">
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
                        <input class="form-check-input other_insurance" type="radio" name="other_insurance" id="other_insurance" value="yes">
                        <label class="form-check-label">Да</label>
                      </div>
                      <div class="form-check">
                        <input class="form-check-input other_insurance" type="radio" name="other_insurance" value="no">
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
                            <input type="radio" name="ch1" checked id="radioSuccess3">
                            <label for="radioSuccess3">Да</label>
                          </div>
                          <div class="checkbox icheck-success">
                            <input type="radio" name="ch1" id="radioSuccess4">
                            <label for="radioSuccess4">Нет</label>
                          </div>
                        </div>
                      <div class="col-sm-3">
                        <div class="form-group">
                          <div class="input-group mb-3">
                            <div class="input-group-prepend">
                              <span class="input-group-text">Сумма</span>
                            </div>
                            <input type="text" class="form-control" name="vehicle_damage_sum">
                          </div>
                        </div>
                      </div>

                      <div class="col-sm-4">
                        <div class="form-group">
                          <div class="input-group mb-3">
                            <div class="input-group-prepend">
                              <span class="input-group-text">Премия</span>
                            </div>
                            <input type="text" class="form-control" name="vehicle_damage_premium">
                          </div>
                        </div>
                      </div>
                      <div class="col-sm-4">
                        <div class="form-group">
                          <div class="input-group mb-3">
                            <div class="input-group-prepend">
                              <span class="input-group-text">Франшиза</span>
                            </div>
                            <input type="text" class="form-control" name="vehicle_damage_franchise">
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
                            <input type="radio" name="ch2" checked id="radioSuccess5">
                            <label for="radioSuccess5">Да</label>
                          </div>
                          <div class="checkbox icheck-success">
                            <input type="radio" name="ch2" id="radioSuccess6">
                            <label for="radioSuccess6">Нет</label>
                          </div>
                        </div>
                        <div class="col-sm-4">
                          <div class="form-group">
                            <div class="input-group mb-3">
                              <div class="input-group-prepend">
                                <span class="input-group-text">Сумма</span>
                              </div>
                              <input type="text" class="form-control" name="civil_liability_sum">
                            </div>
                          </div>
                        </div>

                        <div class="col-sm-4">
                          <div class="form-group">
                            <div class="input-group mb-3">
                              <div class="input-group-prepend">
                                <span class="input-group-text">Премия</span>
                              </div>
                              <input type="text" class="form-control" name="civil_liability_premium">
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </form>

                  <form method="POST" id="product-fields-${fieldNumber}-6">
                    <div class="form-group">
                      <label class=>Раздел III. Несчастные случаи с Застрахованными лицами</label>
                      <div class="form-check">
                        <input class="form-check-input" type="radio" name="ch3" value="yes">
                        <label class="form-check-label">Да</label>
                      </div>
                      <div class="form-check">
                        <input class="form-check-input" type="radio" name="ch3" value="no">
                        <label class="form-check-label">Нет</label>
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
                          <th>Страховая премия</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                          <td><label>Водитель(и)</label></td>
                          <td><input type="number" class="form-control"></td>
                          <td><div class="input-group mb-4">
                            <input type="text" class="form-control">
                            <div class="input-group-append">
                              <select class="form-control success" style="width: 100%;">
                                <option selected="selected">UZS</option>
                                <option>USD</option>
                              </select>
                            </div>
                          </div></td>
                          <td><input type="number" class="form-control"></td>
                          <td><input type="number" class="form-control"></td>
                        </tr>
                        <tr>
                          <td><label>Пассажиры</label></td>
                          <td><input type="number" class="form-control"></td>
                          <td><div class="input-group mb-4">
                            <input type="text" class="form-control">
                            <div class="input-group-append">
                              <select class="form-control success" style="width: 100%;">
                                <option selected="selected">UZS</option>
                                <option>USD</option>
                              </select>
                            </div>
                          </div>
                          </td>
                          <td><input type="number" class="form-control"></td>
                          <td><input type="number" class="form-control"></td>
                        </tr>
                        <tr>
                          <td><label class="text-bold">Общий Лимит</label></td>
                          <td><input type="number" class="form-control"></td>
                          <td><div class="input-group mb-4">
                            <input type="text" class="form-control">
                            <div class="input-group-append">
                              <select class="form-control success" style="width: 100%;">
                                <option selected="selected">UZS</option>
                                <option>USD</option>
                              </select>
                            </div>
                          </div></td>
                          <td><input type="number" class="form-control"></td>
                          <td><input type="number" class="form-control"></td>
                        </tr>
                        <tr>
                          <td colspan="3"><label class="text-bold">Итого</label></td>
                          <td><input type="number" class="form-control"></td>
                        </tr>
                        </tbody>
                      </table>
                    </form>
                  </div>
                  <div class="form-group col-sm-8">
                    <label>Общий лимит ответственности </label>
                    <div class="input-group mb-4">
                      <input type="text" class="form-control">
                      <div class="input-group-append">
                        <select class="form-control success" style="width: 100%;">
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
                      <form method="POST" id="polis-field-${fieldNumber}">
                        <div class="row policy">
                          <div class="col-sm-4">
                            <div class="form-group">
                              <label for="polises">Полис</label>
                              <select class="form-control polises" id="polises-${fieldNumber}" name="policy" style="width: 100%;">
                                <option selected="selected"></option>
                                {% for polis in polises %}
                                  <option value="{{ polis.id }}">{{ polis.policy_number }} - {{ polis.income_session.act_number }}</option>
                                {% endfor %}
                              </select>
                            </div>
                          </div>
                          <div class="col-sm-4">
                            <div class="form-group">
                              <div class="input-group mb-3" style="margin-top: 33px">
                                <div class="input-group-prepend">
                                  <span class="input-group-text">от</span>
                                </div>
                                <input type="date" class="form-control">
                              </div>
                            </div>
                          </div>
                        </div>

                        <div class="form-group">
                          <label>Ответственный Агент</label>
                          <select class="form-control select2" style="width: 100%;">
                            <option selected="selected">Ф.И.О агента</option>
                            <option></option>
                          </select>
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
            </div>
          </div>
        `;

    generalProductFields.append(fields);
}
