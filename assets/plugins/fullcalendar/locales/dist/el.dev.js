"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.el = factory()));
})(void 0, function () {
  'use strict';

  var el = {
    code: "el",
    week: {
      dow: 1,
      doy: 4 // The week that contains Jan 4st is the first week of the year.

    },
    buttonText: {
      prev: "Προηγούμενος",
      next: "Επόμενος",
      today: "Σήμερα",
      month: "Μήνας",
      week: "Εβδομάδα",
      day: "Ημέρα",
      list: "Ατζέντα"
    },
    weekLabel: "Εβδ",
    allDayText: "Ολοήμερο",
    eventLimitText: "περισσότερα",
    noEventsMessage: "Δεν υπάρχουν γεγονότα προς εμφάνιση"
  };
  return el;
});