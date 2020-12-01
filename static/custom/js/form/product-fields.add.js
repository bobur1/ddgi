$(document).ready(function () {
    //better use on() event handler for dynamically creating elements
    $(document).on('click','.product-fields-button', function(e){
        let productForm = $(this);
        let fieldNumber = productForm.data('field-number');
        let field = $('#product-field-modal-' + fieldNumber);
        let content = $('#product-field-modal-content-' + fieldNumber);
        field.show();
        field.css('overflow', 'scroll');
        field.css('padding', '10px');
        content.css('padding', '10px');
    });

    $(document).on('click','.product-fields-close', function(e){
        let productForm = $(this);
        let fieldNumber = productForm.data('field-number');

        $('#product-field-modal-' + fieldNumber).hide();
    });

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
                          <th>Страховая премия</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                          <td><input type="text" class="form-control" name="mark_model"></td>
                          <td><input type="text" class="form-control" name="name"></td>
                          <td><input type="text" class="form-control" name="series_number"></td>
                          <td><input type="text" class="form-control" name="insurance_sum"></td>
                          <td><input type="text" class="form-control" name="insurance_premium"></td>
                        </tr>
                        <tr>
                          <td colspan="4"><label class="text-bold">Итого</label></td>
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
                  <div class="form-group">
                    <label>Покрытие террористических актов с ТС </label>
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

                  <div class="form-group">
                    <label>Покрытие террористических актов с застрахованными лицами </label>
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

                  <div class="form-group">
                    <label>Покрытие расходы по эвакуации</label>
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

              <div class="card card-success">
                <div class="card-header">
                  <h3 class="card-title">Сведени о трансортных средствах</h3>
                  <div class="card-tools">
                    <button type="button" class="btn btn-tool" data-card-widget="collapse" data-toggle="tooltip" title="Collapse">
                      <i class="fas fa-minus"></i></button>
                  </div>
                </div>
                <div class="card-body">
                  <form method="POST" id="product-fields-${fieldNumber}-2">
                    <div class="form-group">
                      <label>Застрахованы ли автотранспортные средства на момент заполнения настоящей анкеты? </label>
                      <div class="form-check">
                        <input class="form-check-input other_insurance" type="radio" name="other_insurance" value="1">
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
                  <form method="POST" id="product-fields-${fieldNumber}-3">
                    <div class="form-group">
                      <label>Раздел I. Гибель или повреждение транспортного средства</label>
                      <div class="row">
                        <div class="col-sm-1">
                          <div class="checkbox icheck-success">
                            <input type="radio" name="vehicle_damage" checked id="radioSuccess3" value="1">
                            <label for="radioSuccess3">Да</label>
                          </div>
                          <div class="checkbox icheck-success">
                            <input type="radio" name="vehicle_damage" id="radioSuccess4" value="0">
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

                  <form method="POST" id="product-fields-${fieldNumber}-4">
                    <div class="form-group">
                      <label class=>Раздел II. Автогражданская ответственность</label>
                      <div class="row">
                        <div class="col-sm-1">
                          <div class="checkbox icheck-success">
                            <input type="radio" name="civil_liability" checked id="radioSuccess5" value="1">
                            <label for="radioSuccess5">Да</label>
                          </div>
                          <div class="checkbox icheck-success">
                            <input type="radio" name="civil_liability" id="radioSuccess6" value="0">
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

                  <form method="POST" id="product-fields-${fieldNumber}-5">
                    <div class="form-group">
                      <label class=>Раздел III. Несчастные случаи с Застрахованными лицами</label>
                      <div class="form-check">
                        <input class="form-check-input" type="radio" name="accidents" value="1">
                        <label class="form-check-label">Да</label>
                      </div>
                      <div class="form-check">
                        <input class="form-check-input" type="radio" name="accidents" value="0">
                        <label class="form-check-label">Нет</label>
                      </div>
                    </div>
                  </form>

                  <div class="table-responsive p-0 ">
                    <form method="POST" id="product-fields-${fieldNumber}-6">
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
                          <td><input type="number" class="form-control" name="driver_total_sum"></td>
                          <td><input type="number" class="form-control" name="driver_premium"></td>
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
                          <td><input type="number" class="form-control" name="passenger_total_sum"></td>
                          <td><input type="number" class="form-control" name="passenger_premium"></td>
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
                          <td><input type="number" class="form-control" name="limit_total_sum"></td>
                          <td><input type="number" class="form-control" name="limit_premium"></td>
                        </tr>
                        <tr>
                          <td colspan="3"><label class="text-bold">Итого</label></td>
                          <td><input type="number" class="form-control" name="total"></td>
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
                              <label for="polises-${fieldNumber}">Полис</label>
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
              </div>
            </div>
          </div>
        `;
    }

    // $('.client-type-radio').click(function () {
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
