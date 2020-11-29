function addRow() {
    var empTab = document.getElementById('empTable');

    var rowCnt = empTab.rows.length;    // get the number of rows.
    var tr = empTab.insertRow(rowCnt-1); // table row.

    for (var c = 0; c < $("#empTable tr th").length; c++) {
      var td = document.createElement('td');          // TABLE DEFINITION.
      td = tr.insertCell(c);

      if (c == ($("#empTable tr th").length - 1)) {   // if its the first column of the table.
        // add a button control.
        var button = document.createElement('input');

        // set the attributes.
        button.setAttribute('type', 'button');
        button.setAttribute('value', 'Удалить');

        // add button's "onclick" event.
        button.setAttribute('onclick', 'removeRow(this)');
        button.setAttribute('class', 'btn btn-warning');

        td.appendChild(button);
      }
      else {
        // all except the last colum will have input field.
        var ele = document.createElement('input');

        if (c === 1) {
          ele.setAttribute('type', 'date');
        }
        else {
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

  // function to delete a row.
  function removeRow(oButton) {
    var empTab = document.getElementById('empTable');
    empTab.deleteRow(oButton.parentNode.parentNode.rowIndex); // buttton -> td -> tr
    calculateSum();
    calculateSum2();
  }

  // function to add new row.
  function addRow2() {
    var empTab = document.getElementById('empTable2');

    var rowCnt = empTab.rows.length;    // get the number of rows.
    var tr = empTab.insertRow(rowCnt-1); // table row.

    for (var c = 0; c < $("#empTable2 tr th").length; c++) {
      var td = document.createElement('td');          // TABLE DEFINITION.
      td = tr.insertCell(c);

      if (c == ($("#empTable2 tr th").length - 1)) {   // if its the first column of the table.
        // add a button control.
        var button = document.createElement('input');

        // set the attributes.
        button.setAttribute('type', 'button');
        button.setAttribute('value', 'Удалить');

        // add button's "onclick" event.
        button.setAttribute('onclick', 'removeRow2(this)');
        button.setAttribute('class', 'btn btn-warning');

        td.appendChild(button);
      }
      else {
        // all except the last colum will have input field.
        var ele = document.createElement('input');

        ele.setAttribute('type', 'text');
        ele.setAttribute('class', 'form-control');

        td.appendChild(ele);
      }
    }
  }

  // function to delete a row.
  function removeRow2(oButton) {
    var empTab = document.getElementById('empTable2');
    empTab.deleteRow(oButton.parentNode.parentNode.rowIndex); // buttton -> td -> tr
  }

  function showDiv(divId, element)
  {
    document.getElementById(divId).style.display = element.value == 'other' ? 'block' : 'none';
  }

  function addRow3() {
    var empTab = document.getElementById('empTable3');

    var rowCnt = empTab.rows.length;    // get the number of rows.
    var tr = empTab.insertRow(rowCnt); // table row.

    for (var c = 0; c < $("#empTable3 tr th").length; c++) {
      var td = document.createElement('td');          // TABLE DEFINITION.
      td = tr.insertCell(c);

      if (c == ($("#empTable3 tr th").length - 1)) {   // if its the first column of the table.
        // add a button control.
        var button = document.createElement('input');

        // set the attributes.
        button.setAttribute('type', 'button');
        button.setAttribute('value', 'Удалить');

        // add button's "onclick" event.
        button.setAttribute('onclick', 'removeRow3(this)');
        button.setAttribute('class', 'btn btn-warning');

        td.appendChild(button);
      }
      else {
        // all except the last colum will have input field.
        var ele = document.createElement('input');

        if (c === 1) {
          ele.setAttribute('type', 'date');
        }
        else {
          ele.setAttribute('type', 'text');
        }

          ele.setAttribute('class', 'form-control');
        td.appendChild(ele);
      }
    }
  }

  // function to delete a row.
  function removeRow3(oButton) {
    var empTab = document.getElementById('empTable3');
    empTab.deleteRow(oButton.parentNode.parentNode.rowIndex); // buttton -> td -> tr
  }

  // function to extract and submit table data.
  function submit() {
    var myTab = document.getElementById('empTable');
    var arrValues = [];

    // loop through each row of the table.
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

  function otherInsurance() {
    // Get the checkbox
    var checkBox = document.getElementById("other_insurance");
    // Get the output text
    var text = document.getElementById("other_insurance_info");

    // If the checkbox is checked, display the output text
    if (checkBox.value === 'yes'){
      text.style.display = "block";
    } else {
      text.style.display = "none";
    }
  }

  $(document).ready(function(){
    $('.other_insurance').click(function(){
      var targetBox = $('.other_insurance_info');
      if ($(this).attr("value") === 'yes') {
        $(targetBox).show();
      } else {
        $(targetBox).hide();
      }
    });
  });

  $(document).ready(function(){
    $('.defects').click(function(){
      var targetBox = $('.defects_images');
      if ($(this).attr("value") === 'yes') {
        $(targetBox).show();
      } else {
        $(targetBox).hide();
      }
    });
  });
