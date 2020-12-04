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
            url: '/api/' + (insurerIndividualClient ? 'client-individual' : 'client-legal') + '/',
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
            url: '/api/' + (beneficiaryIndividualClient ? 'client-individual' : 'client-legal') + '/',
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


});
