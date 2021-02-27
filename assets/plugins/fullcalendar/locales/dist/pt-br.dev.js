"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales['pt-br'] = factory()));
})(void 0, function () {
  'use strict';

  var ptBr = {
    code: "pt-br",
    buttonText: {
      prev: "Anterior",
      next: "Próximo",
      today: "Hoje",
      month: "Mês",
      week: "Semana",
      day: "Dia",
      list: "Lista"
    },
    weekLabel: "Sm",
    allDayText: "dia inteiro",
    eventLimitText: function eventLimitText(n) {
      return "mais +" + n;
    },
    noEventsMessage: "Não há eventos para mostrar"
  };
  return ptBr;
});