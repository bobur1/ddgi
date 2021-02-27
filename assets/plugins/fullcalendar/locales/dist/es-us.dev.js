"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales['es-us'] = factory()));
})(void 0, function () {
  'use strict';

  var esUs = {
    code: "es",
    week: {
      dow: 0,
      doy: 6 // The week that contains Jan 1st is the first week of the year.

    },
    buttonText: {
      prev: "Ant",
      next: "Sig",
      today: "Hoy",
      month: "Mes",
      week: "Semana",
      day: "Día",
      list: "Agenda"
    },
    weekLabel: "Sm",
    allDayHtml: "Todo<br/>el día",
    eventLimitText: "más",
    noEventsMessage: "No hay eventos para mostrar"
  };
  return esUs;
});