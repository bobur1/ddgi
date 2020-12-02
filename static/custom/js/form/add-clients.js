$(document).ready(function () {
    insurerFormButton.click(function (e) {
        e.preventDefault();

        let forms = {};
        let params = {}
        forms.csrfmiddlewaretoken = csrftoken;
        forms.action = 'create';
        let serializedForm = insurerForm.serializeArray();
        for (let i = 0; i < serializedForm.length; i++) {
            params[serializedForm[i]['name']] = serializedForm[i]['value'];
        }
        forms.params = params;

        $.ajax({
            url: '/api/' + (individualClient ? 'client-individual' : 'client-legal') + '/',
            data: JSON.stringify(forms),
            contentType: 'application/json',
            dataType: 'json',
            type: "POST",
            success: function (data) {
                if (data.success === true) {
                    console.log(data);
                    insurerId.append(`<option value="${data.id}">${data.name}</option`);
                    insurerId.val(data.id);
                    alert('Клиент успешно добавлен!');
                } else {
                    alert('Клиент не добавлен!!!');
                }
            }
        });
    });

    beneficiaryFormButton.click(function (e) {
        e.preventDefault();

        let forms = {};
        let params = {}
        forms.csrfmiddlewaretoken = csrftoken;
        forms.action = 'create';
        let serializedForm = beneficiaryForm.serializeArray();
        for (let i = 0; i < serializedForm.length; i++) {
            params[serializedForm[i]['name']] = serializedForm[i]['value'];
        }
        forms.params = params;

        $.ajax({
            url: '/api/client-legal/',
            data: JSON.stringify(forms),
            contentType: 'application/json',
            dataType: 'json',
            type: "POST",
            success: function (data) {
                if (data.success === true) {
                    console.log(data);
                    beneficiaryId.append(`<option value="${data.id}">${data.name}</option`);
                    beneficiaryId.val(data.id);
                    alert('Клиент успешно добавлен!');
                } else {
                    alert('Клиент не добавлен!!!');
                }
            }
        });
    });

    pledgerFormButton.click(function (e) {
        e.preventDefault();

        let forms = {};
        let params = {}
        forms.csrfmiddlewaretoken = csrftoken;
        forms.action = 'create';
        let serializedForm = pledgerForm.serializeArray();
        for (let i = 0; i < serializedForm.length; i++) {
            params[serializedForm[i]['name']] = serializedForm[i]['value'];
        }
        forms.params = params;

        $.ajax({
            url: '/api/client-legal/',
            data: JSON.stringify(forms),
            contentType: 'application/json',
            dataType: 'json',
            type: "POST",
            success: function (data) {
                if (data.success === true) {
                    console.log(data);
                    pledgerId.append(`<option value="${data.id}">${data.name}</option`);
                    pledgerId.val(data.id);
                    alert('Клиент успешно добавлен!');
                } else {
                    alert('Клиент не добавлен!!!');
                }
            }
        });
    });

    $('.beneficiary-type-radio').click(function () {
        clientType = $(this).val();
        $.ajax({
            url: '/api/client_' + clientType + '/',
            method: "GET",
            success: function (data) {
                if (data.success === true) {
                    beneficiaryId.empty().append('<option selected="selected"></option>');
                    const clients = data.data;
                    const length = clients.length;
                    for (let i = 0; i < length; i++) {
                        beneficiaryId.append(`<option value="${clients[i].id}">${clients[i].name}</option>`);
                    }
                }
            },
            error: function () {
                console.log('error');
            }
        });

        let clientType = $("input:radio[name='beneficiary_type_radio']:checked").val();
        // {#getPolicyList(clientType === 'individual' ? 1 : 2);#}

        if (clientType === 'individual') {
            beneficiaryLegalClientRow.hide();
            beneficiaryName.prop('disabled', true);
            beneficiaryOkonh.prop('disabled', true);
            beneficiaryIndividualClientRow.show();
            beneficiaryFirstName.prop('disabled', false);
            beneficiaryLastName.prop('disabled', false);
            beneficiaryMiddleName.prop('disabled', false);
            beneficiaryIndividualClient = true;
        } else {
            beneficiaryLegalClientRow.show();
            beneficiaryName.prop('disabled', false);
            beneficiaryOkonh.prop('disabled', false);
            beneficiaryIndividualClientRow.hide();
            beneficiaryFirstName.prop('disabled', true);
            beneficiaryLastName.prop('disabled', true);
            beneficiaryMiddleName.prop('disabled', true);
            beneficiaryIndividualClient = false;
        }
    });
});
