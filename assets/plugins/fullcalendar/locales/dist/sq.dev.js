"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.sq = factory()));
})(void 0, function () {
  'use strict';

  var sq = {
    code: "sq",
    week: {
      dow: 1,
      doy: 4 // The week that contains Jan 4th is the first week of the year.

    },
    buttonText: {
      prev: "mbrapa",
      next: "Përpara",
      today: "sot",
      month: "Muaj",
      week: "Javë",
      day: "Ditë",
      list: "Listë"
    },
    weekLabel: "Ja",
    allDayHtml: "Gjithë<br/>ditën",
    eventLimitText: function eventLimitText(n) {
      return "+më tepër " + n;
    },
    noEventsMessage: "Nuk ka evente për të shfaqur"
  };
  return sq;
});