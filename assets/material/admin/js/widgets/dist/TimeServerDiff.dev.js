"use strict";

(function () {
  'use strict';

  window.addEventListener('load', function () {
    var timezoneOffset = null;
    var body = document.getElementsByTagName('body')[0];
    var serverOffset = body.getAttribute('data-admin-utc-offset');

    if (serverOffset) {
      var localOffset = new Date().getTimezoneOffset() * -60;
      timezoneOffset = localOffset - serverOffset;
    }

    var inputs = document.getElementsByTagName('input');
    var timezoneOffset = timezoneOffset / 3600;

    if (!timezoneOffset) {
      return;
    }

    var message;

    if (timezoneOffset > 0) {
      message = ngettext('Note: You are %s hour ahead of server time.', 'Note: You are %s hours ahead of server time.', timezoneOffset);
    } else {
      timezoneOffset *= -1;
      message = ngettext('Note: You are %s hour behind server time.', 'Note: You are %s hours behind server time.', timezoneOffset);
    }

    message = interpolate(message, [timezoneOffset]);
    var warnItems = document.getElementsByClassName('time-difference');
    var _iteratorNormalCompletion = true;
    var _didIteratorError = false;
    var _iteratorError = undefined;

    try {
      for (var _iterator = warnItems[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
        var elem = _step.value;
        elem.innerText = message;
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
  });
})();