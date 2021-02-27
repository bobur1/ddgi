"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.hi = factory()));
})(void 0, function () {
  'use strict';

  var hi = {
    code: "hi",
    week: {
      dow: 0,
      doy: 6 // The week that contains Jan 1st is the first week of the year.

    },
    buttonText: {
      prev: "पिछला",
      next: "अगला",
      today: "आज",
      month: "महीना",
      week: "सप्ताह",
      day: "दिन",
      list: "कार्यसूची"
    },
    weekLabel: "हफ्ता",
    allDayText: "सभी दिन",
    eventLimitText: function eventLimitText(n) {
      return "+अधिक " + n;
    },
    noEventsMessage: "कोई घटनाओं को प्रदर्शित करने के लिए"
  };
  return hi;
});