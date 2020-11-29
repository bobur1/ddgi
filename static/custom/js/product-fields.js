function addRow() {
    let empTab = document.getElementById('empTable');

    let rowCnt = empTab.rows.length;    // get the number of rows.
    let tr = empTab.insertRow(rowCnt - 1); // table row.

    for (let c = 0; c < $("#empTable tr th").length; c++) {
        let td = document.createElement('td');          // TABLE DEFINITION.
        td = tr.insertCell(c);

        if (c == ($("#empTable tr th").length - 1)) {   // if its the first column of the table.
            // add a button control.
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

function addRow3() {
    let empTab = document.getElementById('empTable3');

    let rowCnt = empTab.rows.length;    // get the number of rows.
    let tr = empTab.insertRow(rowCnt); // table row.

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
            } else {
                ele.setAttribute('type', 'text');
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
