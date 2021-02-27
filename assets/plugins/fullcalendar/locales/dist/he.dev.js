"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.he = factory()));
})(void 0, function () {
  'use strict';

  var he = {
    code: "he",
    dir: 'rtl',
    buttonText: {
      prev: "הקודם",
      next: "הבא",
      today: "היום",
      month: "חודש",
      week: "שבוע",
      day: "יום",
      list: "סדר יום"
    },
    allDayText: "כל היום",
    eventLimitText: "אחר",
    noEventsMessage: "אין אירועים להצגה",
    weekLabel: "שבוע"
  };
  return he;
});