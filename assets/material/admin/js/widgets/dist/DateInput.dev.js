"use strict";

(function () {
  'use strict';

  window.addEventListener('load', function () {
    var todayIcons = document.querySelectorAll('i.today');

    if (todayIcons.length) {
      var _iteratorNormalCompletion = true;
      var _didIteratorError = false;
      var _iteratorError = undefined;

      try {
        for (var _iterator = todayIcons[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
          var todayIcon = _step.value;
          var myDate = document.querySelector(myDate);
          var today = new Date();
          todayIcon.addEventListener('click', function () {
            var input = this.closest('.date-input').querySelector('.datepicker');
            input.value = today.strftime(get_format('DATE_INPUT_FORMATS')[0]);
          });
        }
      } catch (err) {
        _didIteratorError = true;
        _iteratorError = err;
      } finally {
        try {
          if (!_iteratorNormalCompletion && _iterator["return"] != null) {
            _iterator["return"]();
          }
        } finally {
          if (_didIteratorError) {
            throw _iteratorError;
          }
        }
      }
    }

    var calendars = document.querySelectorAll('i.calendar');

    if (calendars.length) {
      var _iteratorNormalCompletion2 = true;
      var _didIteratorError2 = false;
      var _iteratorError2 = undefined;

      try {
        for (var _iterator2 = calendars[Symbol.iterator](), _step2; !(_iteratorNormalCompletion2 = (_step2 = _iterator2.next()).done); _iteratorNormalCompletion2 = true) {
          var calendar = _step2.value;
          calendar.addEventListener('click', function () {
            var input = this.closest('.date-input').querySelector('.datepicker');
            input.click();
          });
        }
      } catch (err) {
        _didIteratorError2 = true;
        _iteratorError2 = err;
      } finally {
        try {
          if (!_iteratorNormalCompletion2 && _iterator2["return"] != null) {
            _iterator2["return"]();
          }
        } finally {
          if (_didIteratorError2) {
            throw _iteratorError2;
          }
        }
      }
    }
  });
})();